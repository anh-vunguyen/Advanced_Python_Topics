# Errors and Exceptions
# What are differences between a syntax error and an exception?
# What are the msot common built-in exceptions?
# How can we raise and handle exceptions?
# How can we define our own exception?

## Exception
x = -5
# if x < 0:
#     raise Exception('x should be positive.')

## Assertion
# assert (x >= 0), "x is not positive."

## try-except block
try:
    a = 5 / 0
except:
    print("An error happened.")
print("Continue")

print("-----------------------")
# OR
try:
    a = 5 / 0
except Exception as e:
    print("An error happened II")
print("Continue II")
print("-----------------------")
# Be specific about the exception
try:
    # scenario 1
    # a = 5 / 1
    # b = a * '10'
    # scenario 2
    a = 1 / 1
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    # clean-up operation
    # run whether it has exception or not
    print("cleaning up...")

print("------------------------")
## Our own exception
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
