
class Command(object):

    def __init__(self, methodName):
        self.action = methodName

    def Action(self):
        return self.action

    def Execute(self, subject):
        return getattr(subject, self.action)()


class CommandGroup(object):

    def __init__(self, commands=list()):
        self.commands = commands

    def AsList(self):
        return self.commands
