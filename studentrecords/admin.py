from django.contrib import admin
from .models import StudyCenter, ProgramType, Course, CourseSpecialization, \
    CourseEnrollmentMode, EnrollmentType, Student, StudentAcademic, \
    DocumentType


class StudentAcademicInline(admin.TabularInline):
    readonly_fields = ('fee_status',)
    model = StudentAcademic
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'enrollment_id',
                    'dob')
    search_fields = ['student_name', 'enrollment_id']
    list_filter = ('registered_for__program_type',
                   'couse_enrolled__course_name',
                   'course_enrollment_mode__mode',
                   'study_center__center_name', 'batch')
    inlines = [StudentAcademicInline]
    fieldsets = (
        ('Enrollment Info', {
          'fields': (('enrollment_id', 'enrollment_type'),)
          }),
        ('Student Info', {
          'fields': (('student_name','father_name', 'mother_name'),
                    ('dob', 'address', 'study_center'),)
          }),
        ('Course Info', {
          'fields': (('course_enrollment_mode','registered_for',
                    'couse_enrolled', 'course_specialization',
                    'batch'),)
          }),
    )
admin.site.register(StudyCenter)
admin.site.register(ProgramType)
admin.site.register(Course)
admin.site.register(CourseSpecialization)
admin.site.register(CourseEnrollmentMode)
admin.site.register(EnrollmentType)
admin.site.register(Student, StudentAdmin)
admin.site.register(DocumentType)
