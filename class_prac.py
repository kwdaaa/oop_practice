class TestClass:
    a = 1
    b = 2

    def double(self):
        return self.a * 2


bob = TestClass()
tom = TestClass()
tom.a = 2
print(bob.a)
print(tom.a)
