print("hello")
# commenting in the python
a = 3
print(a)
str = "hello world"
print(str)
b, c, d = 4, 5.3, "great"
print(b, c)

print(("{} {}".format("value is ", b)))
print(type(b))

# lists data types

values = [1, 2, "prjwal", 5.6777]
print(values)
print(values[1])
values.insert(3, "M")
print(values)
values.append("end")
print(values)
del values[-1]
print(values)

# tuple

val = (1, 2, "murthy")
print(val)

# dictionary

dic = {10: "abc", "p": 78}
print(dic)
print(dic[10])

dict = {}

dict["firstname"] = "prashanth"
dict["lastname"] = "M"
print(dict)

# Conditons

Greetings = "Good morning"

if Greetings == "Good morning":
    print("condition is true")
else:
    print("condition not satisfied")

print("line after if and else ")

# loops
# for loops

summ = 0
for i in range(1, 6):
    summ = summ + i
print(summ)

for j in range(1, 10, 2):
    print(j)

for k in range(10):
    print(k)

# while loop
print("****************************************")
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1


# function

def greet(name):
    print("good morning" + name)


greet("prajwal")

print("**************")


def add(a, b):
    return a + b


print(add(2, 3))


def add(a, b):
    print(a + b)


add(2, 3)


# oops

class calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print('i am called automatically')

    def getdata(self):
        print("i am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber+ calculator.num


obj1 = calculator(10,3)
obj1.getdata()
print(obj1.summation())

# self is the keyword mandatory for calling  varriable names into method
