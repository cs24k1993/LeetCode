class A(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return 'A '+self.name

a=A.getName('hello')
print(a)