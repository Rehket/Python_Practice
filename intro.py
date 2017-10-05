# Really need to refresh python, holy crap.

print('Hello World!' + '\n')


# Print something with a newline character appended.
def println(thing):
    print(thing + '\n')


# printing with repr()
def println_repr(thing):
    print(thing.__repr__() + '\n')


# printing with str()
def println_str(thing):
    print(thing.__str__() + '\n')


# Here we will do a Fizz Buzz.
def fizzbuzz(number):
    i = 0
    while i < number:
        if i % 3 == 0 and i % 5 == 0:
            println(i.__str__() + ': FizzBuzz')
        elif i % 3 == 0:
            println(i.__str__() + ': Fizz')
        elif i % 5 == 5:
            println(i.__str__() + ': Buzz')
        i += 1

# A note about the .__str__(), python has two methood of converting objects to strings, str() and repr(). repr() is
# used for used for sub-objects located in compound objects.
# https://stackoverflow.com/questions/12448175/confused-about-str-in-python


# A note regarding repr(),
#   It can be overload on object to define the string representation of that object when printed with .__repr__().
#   

# Main entry point.
def main():
    fizzbuzz(25)
    println_repr('This is printed using repr. :P')
    println_str('This is printed using str. :D')

    println_repr('Notice how ween repr is used, the single quotes are included. :P')
    println_str('When str is used, they are not. :D')


main()
