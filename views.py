from django.http import JsonResponse, HttpResponse
from collections import deque
import threading

queue = deque()  # 全局队列
queue_lock = threading.Lock()

def queuePop(request):
    global queue
    global queue_lock
    queue_lock.acquire()  # 获取锁

    try:
        if queue and len(queue) > 0:
            data = queue.popleft()
            return JsonResponse({'popContent':data})
        else:
            return JsonResponse({'retMsg':'queue empty'})
    finally:
        queue_lock.release()  # 释放锁


def queueInsert(request):
    global queue
    global queue_lock
    queue_lock.acquire()

    try:
        if request.method == 'POST':
            data = request.POST.get('insertContent')
            if data:
                queue.append(data)
                return JsonResponse({'insertContent':data})
            else:
                return JsonResponse({'retMsg':'need insertContent field'})
        else:
            return JsonResponse({'retMsg':'need POST request'})
    finally:
        queue_lock.release()
