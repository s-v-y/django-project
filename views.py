from django.http import HttpResponse


def index(request):
    import datetime
    now = datetime.datetime.now()
    html = '<html><body>index.. time : %s.</body></html>' % now
    return HttpResponse(html)




def error_url(request):
    return HttpResponse('error_url')