from django.http import Http404, HttpResponse
import datetime, time, os
# import django
# django.http.HttpResponse()
def sayHi(request):
    return HttpResponse("Hello World this is first pg")

def saytime(request):
    now = datetime.datetime.now()
    newtime = time.strftime("%m-%d-%y", time.localtime())
    print newtime
    html = "<html><body>It is %s<br/>format time: %s</body></html>" %(now, newtime)
    return HttpResponse(html)
    #//it can output html

def cpu(request):
    cpu_status = os.popen('sar 1 1').read()
    html = "<html><body><pre> %s</pre></body>" %cpu_status
    return HttpResponse(html)

def hours_ahead(request, offset):
   try:
       offset = int(offset)
   except ValueError:
       raise Http404()
   dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
   html = "<html><body>In %s hours, it will be %s.</body></html>" %(offset, dt)
   return HttpResponse(html)

