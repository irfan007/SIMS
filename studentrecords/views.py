from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from studentrecords.models import Student


def search(request, sname=None):
    ci = RequestContext(request)
    return render_to_response('index.html', ci)


def search_by_name(request, sname=None):
    ci = RequestContext(request)
    sname = request.POST.get('sname', '')
    if request.method == "POST":
        if sname:
            students = Student.objects.all().filter(student_name__icontains=sname)
        else:
            students = ''
        return render_to_response('search_by_name_result.html', {'students':students}, ci)
    return render_to_response('search_by_name_result.html', {'students':''}, ci)


def student_detail(request, eid=None):
    ci = RequestContext(request)
    eid = request.GET.get("eid", None)
    if eid is not None:
        student = Student.objects.get(pk=str(eid))
        if request.is_ajax():
            return render_to_response('student_detail_ajax.html', {'student': student}, ci)
        return render_to_response('student_detail.html', {'student':student}, ci)
    return HttpResponse('Not Found')
