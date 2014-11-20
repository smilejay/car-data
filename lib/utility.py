'''
Created on Nov 19, 2014

@summary: some utilities in car-data system.
@author: Jay <smile665@gmail.com>
'''
security_key = 'car-data-2014'


def key_validation(key):
    '''
    @summary: validate the key used by the clients.
    '''
    ret = False
    if key.lower() == security_key:
        ret = True
    else:
        ret = False
    return ret


if __name__ == '__main__':
    print key_validation('haha')
    print key_validation(security_key)