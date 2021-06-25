class ToyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


new = ToyClass()
print(new.instancemethod(), new.classmethod(), new.staticmethod() )
