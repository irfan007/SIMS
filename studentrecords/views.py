from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from studentrecords.models import Student


def search(request, sname=None):
    ci = RequestContext(request)
    return render_to_response('index.html', ci)


def search_by_name(request):
    ci = RequestContext(request)
    query = request.POST.get('sname', '')
    offset = request.POST.get('offset', 0)
    limit = request.POST.get('limit', 5)


    if request.method == "POST":
        if request.is_ajax():
            query = request.POST.get('sname', '')
            offset = int(request.POST.get('offset', 0))

            students = Student.objects.all().filter(Q(student_name__icontains=query)
                |Q(enrollment_id__icontains=query))[offset:offset+5]

            kwargs = {'students':students, 'query': query}
            return render_to_response('load_ajax.html',kwargs)
        if query:
            students = Student.objects.all().filter(Q(student_name__icontains=query)
                |Q(enrollment_id__icontains=query))[offset:limit]
        else:
            students = ''
        kwargs = {'students':students, 'offset': offset+5, 'query': query}
        return render_to_response('search_by_name_result.html', kwargs, ci)
    return render_to_response('search_by_name_result.html', {'students':'', 'offset': offset, 'limit': limit, 'query': query}, ci)


def student_detail(request, eid=None):
    ci = RequestContext(request)
    eid = request.GET.get("eid", None)
    if eid is not None:
        student = Student.objects.get(pk=str(eid))
        if request.is_ajax():
            return render_to_response('student_detail_ajax.html', {'student': student}, ci)
        return render_to_response('student_detail.html', {'student':student}, ci)
    return HttpResponse('Not Found')
