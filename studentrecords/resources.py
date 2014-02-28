from .models import StudyCenter, ProgramType, Course, CourseSpecialization, \
    CourseEnrollmentMode, EnrollmentType, Student, StudentAcademic, \
    DocumentType

from import_export import fields, resources


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ('enrollment_id',)


class StudyCenterResource(resources.ModelResource):
    center_name = fields.Field(column_name='Center Name', attribute="center_name")
    center_address = fields.Field(column_name='Address', attribute="center_address")
    center_phone = fields.Field(column_name='Phone', attribute="center_phone")
    class Meta:
        model = StudyCenter
        import_id_fields = ('center_name',)


class DocumentTypeResource(resources.ModelResource):
    document_type = fields.Field(column_name='Document Type', attribute="document_type")

    class Meta:
        model = DocumentType
        import_id_fields = ('document_type',)
