class MyClass:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def __eq__(self, other):
        if not isinstance(other, MyClass):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.foo == other.foo and self.bar == other.bar

x = MyClass('foo', 'bar')
y = MyClass('foo', 'bar')
print(x == y) #Python возвращает False
print(x, y)

