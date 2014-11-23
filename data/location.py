'''
Created on Nov 23, 2014

@author: Jay <smile665@gmail.com>
'''
from data.serializers import LocationSerializer
from lib.logger import CarLogger

logger = CarLogger().getLogger()


def add(data):
    '''
    @summary: add an location record.
    @parm data: a dict for the Locaiton's serializer.
    @return: None.
    '''
    ret = False
    a_se = LocationSerializer(data=data, many=True)
    if a_se.is_valid():
        a_se.save()
        ret = True
    else:
        logger.info('invalid data for acceleration table.\n' +
                    'data: %s' % data)
        ret = False
    return ret


if __name__ == '__main__':
    pass
