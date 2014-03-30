'''
Inception - a FireWire physical memory manipulation and hacking tool exploiting
IEEE 1394 SBP-2 DMA.
'''
from inception import cfg
import os.path
import subprocess

    
def play(filename):
    '''
    Crude interface for playing wav sounds - dies silently if something fails
    '''
    f = os.path.join(os.path.dirname(__file__),filename)

    try:
        if (filename.endswith('.wav') or filename.endswith('.mp3')) and os.path.exists(f):
            if cfg.os == cfg.LINUX:
                cmd = 'aplay'
            elif cfg.os == cfg.OSX:
                cmd = 'afplay'
            else:
                raise Exception
            with open(os.devnull, "w") as fnull:
                return subprocess.Popen([cmd,f], stdout = fnull, stderr = fnull)
    except:
        pass
