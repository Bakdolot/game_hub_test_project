from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from .models import UserPassedLink
from .utils import url_check


@login_required(login_url="/admin/login/")
@require_GET
def link_list(request: HttpRequest) -> HttpResponse:
    queryset = UserPassedLink.objects.all()
    context = {"link_objects": queryset, "link_ids": queryset.values_list("id", flat=True)}
    return render(request, "index.html", context)


@require_GET
def check_link(request: HttpRequest, link_id: int) -> JsonResponse:
    link_obj = get_object_or_404(UserPassedLink, pk=link_id)
    response_status_code = url_check(link_obj.link)
    if link_obj.status != response_status_code:
        link_obj.status = response_status_code
        link_obj.save()
    else:
        link_obj.checked_at = timezone.now()
        link_obj.save()
    return JsonResponse({"status_code": response_status_code, "id": link_id})
