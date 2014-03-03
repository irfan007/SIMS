from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    (r'^search/$', 'studentrecords.views.search'),
    (r'^search/name/$', 'studentrecords.views.search_by_name'),
    (r'^detail/', 'studentrecords.views.student_detail'),
)
