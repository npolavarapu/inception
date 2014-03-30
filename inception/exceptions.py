'''
Inception - a FireWire physical memory manipulation and hacking tool exploiting
IEEE 1394 SBP-2 DMA.
'''

class InceptionException(Exception):
    '''
    Non... rien de rien
    Non je ne regrette rien
    Ni le bien... qu'on m'a fait
    Ni le mal, tout ça m'est bien égale...
    '''
    def __init__(self, message, Errors):

        # Call the base class constructor
        Exception.__init__(self, message)

        # Handle errors (for now assign to base class Errors)
        self.Errors = Errors
