from django.shortcuts import render,HttpResponse
import threading
import time
import redis
r = redis.Redis()





def index(request):
    
    return render(request,"index.html")

def start(request):
    t = threading.Thread(target=asynctask,args=["a"],daemon=True)
    t.start()
    return HttpResponse("ok")


def asynctask(s):
    a=0
    while a<=100:
        r.publish("name",a)
        a+=1
        time.sleep(0.01)