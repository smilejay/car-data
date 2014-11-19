from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse


@csrf_exempt
def demo_post(request):
    '''
    @author: xin.he@dianping.com
    @note: POST
    @return: a list of bug count and fixtime information
    '''
    if request.method == 'POST':
        req = Request(request)
        raw_data = req.DATA
        device_id = raw_data.get('device_id', default='default')
        acceleration = raw_data.get('acceleration', default=0)
        timestamp = raw_data.get('timestamp', default='2014-01-01')
        data = {'device_id': device_id, 'acceleration': acceleration,
                'timestamp': timestamp}
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP POST method.'},
            status=200)