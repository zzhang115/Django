from django.http import HttpResponse
import datetime, time
# import django
# django.http.HttpResponse()
def sayHi(request):
    now = datetime.datetime.now()
    newtime = time.strftime("%m-%d-%y", time.localtime())
    print newtime
    html = "<html><body>It is %s<br/>format time: %s</body></html>" %(now, newtime)
    return HttpResponse(html)
    #//it can output html