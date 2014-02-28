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
    # course_type = fields.Field(column_name='Course Type', attribute="course_type", widget=widgets.ForeignKeyWidget)
    # course_name = fields.Field(column_name='Course Name', attribute="course_name")
    # course_duration = fields.Field(column_name='Course Duration', attribute="course_duration")
    
    class Meta:
        model = Course
        import_id_fields = ('course_name', 'course_type')


class CourseSpecializationResource(resources.ModelResource):
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
    enrollment_id = fields.Field(attribute="enrollment_id")
    enrollment_type = fields.Field(attribute="enrollment_type", widget=widgets.ForeignKeyWidget(EnrollmentType))
    course_enrollment_mode = fields.Field(attribute="course_enrollment_mode", widget=widgets.ForeignKeyWidget(CourseEnrollmentMode))
    course_enrolled = fields.Field(attribute="course_enrolled", widget=widgets.ForeignKeyWidget(Course))
    course_specialization = fields.Field(attribute="course_specialization", widget=widgets.ForeignKeyWidget(CourseSpecialization))

    class Meta:
        model = Student
        import_id_fields = ('enrollment_id',)


class DocumentTypeResource(resources.ModelResource):
    document_type = fields.Field(column_name='Document Type', attribute="document_type")

    class Meta:
        model = DocumentType
        import_id_fields = ('document_type',)
