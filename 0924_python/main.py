###################################
# Calculator                      #
# Author: Justin Seong            #
###################################


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.sub(4))
print(cal1.mul(5))
print(cal1.div(7))
print(cal2.add(3))
print(cal2.div(7))
print(cal2.mul(5))
print(cal2.sub(5))



# 33 lines of code



