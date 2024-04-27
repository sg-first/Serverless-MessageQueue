from django.http import JsonResponse, HttpResponse
from collections import deque

queue = deque()  # 全局队列

def queuePop(request):
    if queue and len(queue) > 0:
        data = queue.popleft()
        return JsonResponse({'popContent':data})
    else:
        return JsonResponse({'retMsg':'queue empty'})

def queueInsert(request):
    if request.method == 'POST':
        data = request.POST.get('insertContent')
        if data:
            queue.append(request.POST.get('insertContent'))
            return JsonResponse({'insertContent':data})
        else:
            return JsonResponse({'retMsg':'need insertContent field'})
    else:
        return JsonResponse({'retMsg':'need POST request'})
    