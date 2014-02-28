from django.contrib import admin
from .models import StudyCenter, ProgramType, Course, CourseSpecialization, \
    CourseEnrollmentMode, EnrollmentType, Student, StudentAcademic, \
    DocumentType
from .resources import StudentResource, StudyCenterResource, DocumentTypeResource

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportMixin, ImportExportModelAdmin


class StudyCenterAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StudyCenterResource


class DocumentTypeAdmin(ImportExportModelAdmin):
    resource_class = DocumentTypeResource
    pass



class StudentAcademicInline(admin.TabularInline):
    readonly_fields = ('fee_status',)
    model = StudentAcademic
    extra = 1


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('student_name', 'enrollment_id',
                    'dob')
    search_fields = ['student_name', 'enrollment_id']
    list_filter = ('registered_for__program_type',
                   'course_enrolled__course_name',
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
                    'course_enrolled', 'course_specialization',
                    'batch'),)
          }),
    )
admin.site.register(StudyCenter, StudyCenterAdmin)
admin.site.register(ProgramType)
admin.site.register(Course)
admin.site.register(CourseSpecialization)
admin.site.register(CourseEnrollmentMode)
admin.site.register(EnrollmentType)
admin.site.register(Student, StudentAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
