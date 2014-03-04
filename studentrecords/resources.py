from .models import StudyCenter, ProgramType, Course, CourseSpecialization, \
    CourseEnrollmentMode, EnrollmentType, Student, StudentAcademic, \
    DocumentType

from import_export import fields, resources, widgets


class StudyCenterResource(resources.ModelResource):
    center_name = fields.Field(column_name='Center Name', attribute="center_name")
    center_address = fields.Field(column_name='Center Address', attribute="center_address")
    center_phone = fields.Field(column_name='Center Phone', attribute="center_phone")
    class Meta:
        model = StudyCenter
        fields = ('center_name','center_address','center_phone')
        import_id_fields = ('center_name',)


class ProgramTypeResource(resources.ModelResource):
    program_type = fields.Field(column_name='Program Type', attribute="program_type")
    class Meta:
        model = ProgramType
        fields = ('program_type',)
        import_id_fields = ('program_type',)


class CourseResource(resources.ModelResource):
    course_type = fields.Field(column_name='Course Type', attribute="course_type", widget=widgets.ForeignKeyWidget(ProgramType))
    course_name = fields.Field(column_name='Course Name', attribute="course_name")
    course_duration = fields.Field(column_name='Course Duration', attribute="course_duration", widget=widgets.IntegerWidget())
    
    class Meta:
        model = Course
        import_id_fields = ('course_name', 'course_type')


class CourseSpecializationResource(resources.ModelResource):
    course_name = fields.Field(column_name='Course Name', attribute="course_name", widget=widgets.ForeignKeyWidget(Course))
    specialization = fields.Field(column_name='Specialization', attribute="specialization")
    class Meta:
        model = CourseSpecialization
        import_id_fields = ('specialization',)


class CourseEnrollmentModeResource(resources.ModelResource):
    mode = fields.Field(column_name='Mode', attribute="mode")
    class Meta:
        model = CourseEnrollmentMode
        fields = ('mode',)
        import_id_fields = ('mode',)


class EnrollmentTypeResource(resources.ModelResource):
    class Meta:
        model = EnrollmentType
        import_id_fields = ('enrollment_type',)


class StudentResource(resources.ModelResource):
    enrollment_id = fields.Field(column_name='Enrollment ID', attribute="enrollment_id")
    enrollment_type = fields.Field(column_name="Enrollment Type", attribute='enrollment_type', widget=widgets.ForeignKeyWidget(EnrollmentType))
    course_enrollment_mode = fields.Field(column_name="Enrollment Mode", attribute="course_enrollment_mode", widget=widgets.ForeignKeyWidget(CourseEnrollmentMode))
    student_name = fields.Field(column_name='Name', attribute="student_name")
    registered_for = fields.Field(column_name='UG/PG', attribute="registered_for", widget=widgets.ForeignKeyWidget(ProgramType))
    course_enrolled = fields.Field(column_name='Course', attribute="course_enrolled", widget=widgets.ForeignKeyWidget(Course))
    course_specialization = fields.Field(column_name='Specialization', attribute="course_specialization", widget=widgets.ForeignKeyWidget(CourseSpecialization))
    batch = fields.Field(column_name='Batch', attribute="batch", widget=widgets.IntegerWidget())
    father_name = fields.Field(column_name='Father Name', attribute="father_name")
    mother_name = fields.Field(column_name='Mother Name', attribute="mother_name")
    dob = fields.Field(column_name='DOB', attribute="dob", widget=widgets.DateWidget())
    address = fields.Field(column_name='Address', attribute="address")
    study_center = fields.Field(column_name='Study Center', attribute="study_center", widget=widgets.ForeignKeyWidget(StudyCenter))

    class Meta:
        model = Student
        import_id_fields = ('enrollment_id',)

    def before_save_instance(self, instance, dry_run):
        print 'before save instance'


class DocumentTypeResource(resources.ModelResource):
    document_type = fields.Field(column_name='Document Type', attribute="document_type")

    class Meta:
        model = DocumentType
        import_id_fields = ('document_type',)


class StudentAcademicResource(resources.ModelResource):
    student = fields.Field(column_name="Enrollment ID", attribute="student", widget=widgets.ForeignKeyWidget(Student))
    course_year = fields.Field(column_name="Course Year", attribute="course_year")
    roll_number = fields.Field(column_name="Roll Number", attribute="roll_number", widget=widgets.IntegerWidget())
    certificate_type = fields.Field(column_name="Certificate Type", attribute="certificate_type", widget=widgets.ForeignKeyWidget(DocumentType))
    serial_number = fields.Field(column_name="Certificate Number", attribute="serial_number", widget=widgets.IntegerWidget())
    session_fee = fields.Field(column_name="Session Fee", attribute="session_fee", widget=widgets.IntegerWidget())
    ammount_paid = fields.Field(column_name="Fee Paid", attribute="ammount_paid", widget=widgets.IntegerWidget())

    class Meta:
        model = StudentAcademic
        exclude = (id,)
