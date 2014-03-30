'''
Inception - a FireWire physical memory manipulation and hacking tool exploiting
IEEE 1394 SBP-2 DMA.
'''
from inception import cfg
import pdb
import sys
import inspect
import logging

MAX_DEBUG = 3

def setup(level = 0):
    '''
    Sets up the global logging environment
    '''
    formatstr = '%(levelname)-8s: %(name)-20s: %(message)s'
    logging.basicConfig(format = formatstr)
    rootlogger = logging.getLogger('')
    rootlogger.setLevel(logging.DEBUG + 1 - level)
    for i in range(1, 9):
        logging.addLevelName(logging.DEBUG - i, 'DEBUG' + str(i))


def debug(msg, level = 1):
    '''
    Logs a message at the DEBUG level
    '''
    log(msg, logging.DEBUG + 1 - level)


def info(msg):
    '''
    Logs a message at the INFO level
    '''
    log(msg, logging.INFO)


def warn(msg):
    '''
    Logs a message at the WARNING level
    '''
    log(msg, logging.WARNING)


def error(msg):
    '''
    Logs a message at the ERROR level
    '''
    log(msg, logging.ERROR)
    sys.exit(1)


def critical(msg):
    '''
    Logs a message at the CRITICAL level
    '''
    log(msg, logging.CRITICAL)
    sys.exit(1)


def log(msg, level):
    '''
    Logs a message
    '''
    modname = 'inception'
    try:
        frm = inspect.currentframe()
        modname = 'inception.debug'
        while modname == 'inception.debug':
            frm = frm.f_back
            mod = inspect.getmodule(frm)
            modname = mod.__name__
    except AttributeError:
        pass
    finally:
        del frm
    _log(msg, modname, level)


def _log(msg, facility, loglevel):
    '''
    Outputs a debugging message
    '''
    logger = logging.getLogger(facility)
    logger.log(loglevel, msg)


def dbg(level = 1):
    '''
    Enters the debugger at the call point
    '''
    if cfg.DEBUG >= level:
        pdb.set_trace()


def post_mortem(level = 1):
    '''
    Provides a command line interface to python after an exception's occurred
    '''
    if cfg.DEBUG >= level:
        pdb.post_mortem()
