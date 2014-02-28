from django.db import models
from django.db.models import Sum

from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey


class StudyCenter(models.Model):
    """Model for Recording study center detail"""
    center_name = models.CharField(max_length=200, unique=True,
                                   primary_key=True)
    center_address = models.CharField(max_length=255, blank=True, null=True)
    center_phone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.center_name


class ProgramType(models.Model):
    """ Describe Course Type """
    program_type = models.CharField(max_length=20, unique=True,
                                    primary_key=True,
                                    help_text="eg:- 'UG', 'PG'")

    def __unicode__(self):
        return self.program_type


class Course(models.Model):
    """Model Describing Course """
    course_type = models.ForeignKey(ProgramType)
    course_name = models.CharField(max_length=50, unique=True,
                                   primary_key=True)
    course_duration = models.IntegerField(help_text='Course Duration in Years')

    def __unicode__(self):
        return self.course_name


class CourseSpecialization(models.Model):
    """ Describe Course Specialization"""
    course_name = models.ForeignKey(Course)
    specialization = models.CharField(max_length=50, unique=True,
                                      primary_key=True,
                                      help_text="eg:- 'Arts', 'Hindi', etc.")

    def __unicode__(self):
        return self.specialization


class CourseEnrollmentMode(models.Model):
    """ Course Enrollment Mode """
    mode = models.CharField(max_length=20, unique=True,
                            primary_key=True,
                            help_text="eg:- 'Yearly', 'Semester'")

    def __unicode__(self):
        return self.mode


class EnrollmentType(models.Model):
    """ Student Enrollment Type eg:-New, Re-Registration """
    enrollment_type = models.CharField(max_length=30, unique=True,
                                       primary_key=True)

    def __unicode__(self):
        return self.enrollment_type


class Student(models.Model):
    """Model Describing Student"""
    enrollment_id = models.CharField(max_length=100, unique=True,
                                     primary_key=True)
    enrollment_type = models.ForeignKey(EnrollmentType)
    course_enrollment_mode = models.ForeignKey(CourseEnrollmentMode)
    student_name = models.CharField(max_length=100)
    registered_for = models.ForeignKey(ProgramType, related_name='ProgramType')
    # course_enrolled = models.ForeignKey(Course, related_name='Course')
    course_enrolled = ChainedForeignKey(
        Course,
        chained_field='registered_for',
        chained_model_field='course_type',
        show_all=False,
        auto_choose=True
    )
    # course_specialization = models.ForeignKey(CourseSpecialization,
    #                                           related_name='Specialization')
    course_specialization = ChainedForeignKey(
        CourseSpecialization,
        chained_field='course_enrolled',
        chained_model_field='course_name'
    )
    batch = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    study_center = models.ForeignKey(StudyCenter, related_name='rel')

    def __unicode__(self):
        return self.student_name


class DocumentType(models.Model):
    """ Document Type eg:- 'Marksheet', 'Degree' """
    document_type = models.CharField(max_length=50, unique=True,
                                     primary_key=True)

    def __unicode__(self):
        return self.document_type


class StudentAcademic(models.Model):
    """Batch Information """
    YEAR = (('I', 'First Year'),
            ('II', 'Second Year'),
            ('III', 'Third Year'),
            ('IV', 'Fourth Year'),
            ('RA', 'Reappear'),)
    student = models.ForeignKey(Student, related_name='Student')
    course_year = models.CharField(max_length=3, choices=YEAR)
    roll_number = models.IntegerField(blank=True, null=True)
    certificate_type = models.ForeignKey(DocumentType, blank=True, null=True)
    serial_number = models.IntegerField(blank=True, null=True)
    session_fee = models.IntegerField(blank=True, null=True)
    ammount_paid = models.IntegerField(default=0, blank=True, null=True)

    def fee_status(self):
        if not self.session_fee:
            return ''

        current_total_fee = StudentAcademic.objects.filter(
            student=self.student,
            course_year=self.course_year).aggregate(Sum('session_fee'))

        current_fee_status = StudentAcademic.objects.filter(
            student=self.student,
            course_year=self.course_year).aggregate(Sum('ammount_paid'))

        if self.course_year == 'I':
            query = {'student': self.student, 'course_year': 'I'}
            total_fee = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('session_fee'))
            total_fee_paid = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('ammount_paid'))

        elif self.course_year == 'II':
            query = {'student': self.student, 'course_year__in': ['I', 'II']}
            total_fee = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('session_fee'))
            total_fee_paid = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('ammount_paid'))

        elif self.course_year == 'III':
            query = {'student': self.student,
                     'course_year__in': ['I', 'II', 'III']}
            total_fee = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('session_fee'))
            total_fee_paid = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('ammount_paid'))

        elif self.course_year == 'IV':
            query = {'student': self.student,
                     'course_year__in': ['I', 'II', 'III', 'IV']}
            total_fee = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('session_fee'))
            total_fee_paid = StudentAcademic.objects.filter(**query)\
                .aggregate(Sum('ammount_paid'))

        current_due = (current_total_fee['session_fee__sum'] -
                       current_fee_status['ammount_paid__sum'])
        overall_due = total_fee['session_fee__sum'] - \
            (total_fee_paid['ammount_paid__sum'] + current_due)
        total_current_due = current_due + overall_due

        if total_current_due < 0:
            overall_status_msg = 'Advance Paid'
        else:
            overall_status_msg = 'Total Unpaid'
        if total_current_due == 0 and overall_due == 0:
            msg = 'Nothing Due'
        else:
            msg = 'Current Paid = {0}\nTotal Paid = {1}\n{2} = {3}'\
                .format(current_fee_status['ammount_paid__sum'],
                        total_fee_paid['ammount_paid__sum'],
                        overall_status_msg,
                        abs(total_current_due))

        return '{0}'.format(msg)

    def __unicode__(self):
        return "{0}/{1}/{2}".format(self.student, self.course_year,
                                    self.roll_number)
