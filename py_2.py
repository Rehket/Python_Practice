
# Lets play with some Lists.
# TODO: go through https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range.
# TODO: Then go through https://docs.python.org/3.6/faq/programming.html#faq-multidimensional-list
# Tired now...

# Print something with a newline character appended.
def println(thing):
    print(thing.__str__() + '\n')


def main():
    # Here we are asking if the substring "gg" is contained within "eggs"
    println("gg" in "eggs")

    # no regex for you
    println("*g" in "eggs")


# Main program entry point.
main()

