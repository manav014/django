from django.http import HttpResponse
from django.utils.decorators import classonlymethod
from django.views.generic import View


def empty_view(request, *args, **kwargs):
    return HttpResponse()


def sensitive_fbv(request, *args, **kwargs):
    return HttpResponse()


sensitive_fbv._should_append_slash = False


class SensitiveCBV(View):
    def get(self, *args, **kwargs):
        return HttpResponse()

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._should_append_slash = False
        return view
