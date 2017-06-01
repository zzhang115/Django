from django.shortcuts import render_to_response
import os, datetime
# a simple way to use template, it can write python and html seperately
def disk(request):
    # d_usage = os.popen('df -h').read()#.split('\n')
    d_usage = os.popen('df -h').read().split('\n')
    return render_to_response("diskstatus.html", {"disk_usage" : d_usage})
