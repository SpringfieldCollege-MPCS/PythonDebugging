import ipdb


# Break up functions into temporary variables
# use ipdb to inspect data
# now show with vscode


def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(a):
    return a^2

def divide(a, b):
    return a // b


def big_calc(a, b):
    """
    This function computer the following equation:
       ((a + b) * (a / b)) * ((a + b) * (a / b))
       which is squared((a + b) * (a / b)) [squared operator, power of 2]
    """
    return square(multiply(sum(a, b), divide(a,b)))


def main():
    print("Attempting a big calc")
    a, b = 1, 2
    import ipdb; ipdb.set_trace()
    value = big_calc(a, b)
    print(f"Value of (({a} + {b}) * ({a} / {b}))^2  is: {value}")


if __name__ == "__main__":
    main()