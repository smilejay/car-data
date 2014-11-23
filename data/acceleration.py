'''
Created on Nov 19, 2014

@author: Jay <smile665@gmail.com>
'''
from data.serializers import AccelerationSerializer
from lib.logger import CarLogger
from datetime import datetime

logger = CarLogger().getLogger()


def add(data):
    '''
    @summary: add an acceleration record.
    @parm data: a dict for the Acceleration's serializer.
    @return: None.
    '''
    ret = False
    new_data = []
    for i in data:
        if not isinstance(i['timestamp'], datetime):
            i['timestamp'] = datetime.fromtimestamp(float(i['timestamp']))
        new_data.append(i)
    a_se = AccelerationSerializer(data=new_data, many=True)
    if a_se.is_valid():
        a_se.save()
        ret = True
    else:
        logger.info('invalid data for acceleration table.\n' +
                    'data: %s' % new_data)
        ret = False
    return ret


if __name__ == '__main__':
    pass
