# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudyCenter'
        db.create_table(u'studentrecords_studycenter', (
            ('center_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
            ('center_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('center_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'studentrecords', ['StudyCenter'])

        # Adding model 'ProgramType'
        db.create_table(u'studentrecords_programtype', (
            ('program_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'studentrecords', ['ProgramType'])

        # Adding model 'Course'
        db.create_table(u'studentrecords_course', (
            ('course_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentrecords.ProgramType'])),
            ('course_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
            ('course_duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'studentrecords', ['Course'])

        # Adding model 'CourseSpecialization'
        db.create_table(u'studentrecords_coursespecialization', (
            ('course_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentrecords.Course'])),
            ('specialization', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
        ))
        db.send_create_signal(u'studentrecords', ['CourseSpecialization'])

        # Adding model 'CourseEnrollmentMode'
        db.create_table(u'studentrecords_courseenrollmentmode', (
            ('mode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'studentrecords', ['CourseEnrollmentMode'])

        # Adding model 'EnrollmentType'
        db.create_table(u'studentrecords_enrollmenttype', (
            ('enrollment_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, primary_key=True)),
        ))
        db.send_create_signal(u'studentrecords', ['EnrollmentType'])

        # Adding model 'DocumentType'
        db.create_table(u'studentrecords_documenttype', (
            ('document_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
        ))
        db.send_create_signal(u'studentrecords', ['DocumentType'])

        # Adding model 'Student'
        db.create_table(u'studentrecords_student', (
            ('enrollment_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, primary_key=True)),
            ('enrollment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentrecords.EnrollmentType'])),
            ('course_enrollment_mode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentrecords.CourseEnrollmentMode'])),
            ('student_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('registered_for', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ProgramType', to=orm['studentrecords.ProgramType'])),
            ('course_enrolled', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['studentrecords.Course'])),
            ('course_specialization', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['studentrecords.CourseSpecialization'])),
            ('batch', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mother_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('study_center', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rel', to=orm['studentrecords.StudyCenter'])),
        ))
        db.send_create_signal(u'studentrecords', ['Student'])

        # Adding model 'StudentAcademic'
        db.create_table(u'studentrecords_studentacademic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Student', to=orm['studentrecords.Student'])),
            ('course_year', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('roll_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('certificate_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentrecords.DocumentType'], null=True, blank=True)),
            ('serial_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('session_fee', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ammount_paid', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'studentrecords', ['StudentAcademic'])


    def backwards(self, orm):
        # Deleting model 'StudyCenter'
        db.delete_table(u'studentrecords_studycenter')

        # Deleting model 'ProgramType'
        db.delete_table(u'studentrecords_programtype')

        # Deleting model 'Course'
        db.delete_table(u'studentrecords_course')

        # Deleting model 'CourseSpecialization'
        db.delete_table(u'studentrecords_coursespecialization')

        # Deleting model 'CourseEnrollmentMode'
        db.delete_table(u'studentrecords_courseenrollmentmode')

        # Deleting model 'EnrollmentType'
        db.delete_table(u'studentrecords_enrollmenttype')

        # Deleting model 'DocumentType'
        db.delete_table(u'studentrecords_documenttype')

        # Deleting model 'Student'
        db.delete_table(u'studentrecords_student')

        # Deleting model 'StudentAcademic'
        db.delete_table(u'studentrecords_studentacademic')


    models = {
        u'studentrecords.course': {
            'Meta': {'object_name': 'Course'},
            'course_duration': ('django.db.models.fields.IntegerField', [], {}),
            'course_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'course_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentrecords.ProgramType']"})
        },
        u'studentrecords.courseenrollmentmode': {
            'Meta': {'object_name': 'CourseEnrollmentMode'},
            'mode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'primary_key': 'True'})
        },
        u'studentrecords.coursespecialization': {
            'Meta': {'object_name': 'CourseSpecialization'},
            'course_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentrecords.Course']"}),
            'specialization': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'})
        },
        u'studentrecords.documenttype': {
            'Meta': {'object_name': 'DocumentType'},
            'document_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'})
        },
        u'studentrecords.enrollmenttype': {
            'Meta': {'object_name': 'EnrollmentType'},
            'enrollment_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'})
        },
        u'studentrecords.programtype': {
            'Meta': {'object_name': 'ProgramType'},
            'program_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'primary_key': 'True'})
        },
        u'studentrecords.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'batch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'course_enrolled': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['studentrecords.Course']"}),
            'course_enrollment_mode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentrecords.CourseEnrollmentMode']"}),
            'course_specialization': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['studentrecords.CourseSpecialization']"}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enrollment_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'}),
            'enrollment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentrecords.EnrollmentType']"}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registered_for': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ProgramType'", 'to': u"orm['studentrecords.ProgramType']"}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'study_center': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rel'", 'to': u"orm['studentrecords.StudyCenter']"})
        },
        u'studentrecords.studentacademic': {
            'Meta': {'object_name': 'StudentAcademic'},
            'ammount_paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'certificate_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentrecords.DocumentType']", 'null': 'True', 'blank': 'True'}),
            'course_year': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roll_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'session_fee': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Student'", 'to': u"orm['studentrecords.Student']"})
        },
        u'studentrecords.studycenter': {
            'Meta': {'object_name': 'StudyCenter'},
            'center_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'center_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'}),
            'center_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['studentrecords']