from Tools.scripts.patchcheck import status


class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
    def status(age):
        if age < 0:
            raise NegativeAgeException("Only positive integers are allowed")
        if age>22:
            print("Eligible for mrg")
        else:
            print("not Eligible for mrg....")

try:
    num = int(input("Enter your age: "))
    status(num)
except NegativeAgeException:
    print("Only positive integers are allowed")
except:
    print("something is wrong")


#Enter your age: 20
#not eligible for mrg....
