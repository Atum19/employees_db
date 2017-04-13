from .settings import PORTAL_URL


def employees_proc(request):
    return {'PORTAL_URL': PORTAL_URL}
