
class Strategy(object):

    def __init__(self, subject):
        self.subject = subject

    def Utility(self, subject):
        raise NotImplementedError('Function has not been implemented.')
