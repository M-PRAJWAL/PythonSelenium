from Pythonbasics import calculator


class Childimpl(calculator):
    num2 = 900

    def __init__(self):
        calculator.__init__(self, 5, 7)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj = Childimpl()
print(obj.getcompletedata())
