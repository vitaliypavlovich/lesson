class Parent:
    def do_something(self):
        print("Class parent")


class Child(Parent):
    def do_something(self):
       super().do_something()
       print("Class child")


c = Child()
c.do_something()
