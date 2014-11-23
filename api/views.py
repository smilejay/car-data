from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
import data.acceleration as acceleration
import data.location as location
import ast


@csrf_exempt
def demo_post(request):
    '''
    @summary: just a demo for HTTP POST API.
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


@csrf_exempt
def save_acceleration(request):
    '''
    @summary: save the acceleration data.
    '''
    if request.method == 'POST':
        data = 'Hello'
        req = Request(request)
        raw_data = req.DATA
        key = raw_data.get('key', default='')
        input_data = raw_data.get('data', default='')
        if key_validation(key):
            accelerations = ast.literal_eval(input_data)
            if acceleration.add(accelerations):
                data = {'status': True,
                        'detail': 'your data is saved correctly.'}
            else:
                data = {'status': False,
                        'detail': 'invalid data. Not saved.' }
        else:
            data = {'status': False,
                    'detail': 'invalid key. you are not authorized.'}
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP POST method.'},
            status=200)


@csrf_exempt
def save_location(request):
    '''
    @summary: save the location data.
    '''
    if request.method == 'POST':
        data = 'Hello'
        req = Request(request)
        raw_data = req.DATA
        key = raw_data.get('key', default='')
        input_data = raw_data.get('data', default='')
        if key_validation(key):
            locations = ast.literal_eval(input_data)
            if location.add(locations):
                data = {'status': True,
                        'detail': 'your data is saved correctly.'}
            else:
                data = {'status': False,
                        'detail': 'invalid data. Not saved.' }
        else:
            data = {'status': False,
                    'detail': 'invalid key. you are not authorized.'}
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP POST method.'},
            status=200)
