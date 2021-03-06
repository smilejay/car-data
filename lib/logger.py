'''
Created on Nov 19, 2014

@author: Jay <smile665@gmail.com>
'''

import logging


class CarLogger:
    '''
    The common logger for car-data project.
    '''

    logger = None

    def __init__(self, logfile='car-data.log', level=logging.INFO,
                 name='car-data'):
        FORMAT = '%(asctime)-15s  %(message)s'
        logging.basicConfig(filename=logfile, format=FORMAT, level=level)
        self.logger = logging.getLogger(name=name)

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    mylogger = CarLogger().getLogger()
    mylogger.info('hello')
