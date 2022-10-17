def outer(func):
    counter = 0

    def inner():
        nonlocal counter
        print(f"Wurde bisher {counter} mal ausgeführt")
        counter += 1
        func()

    return inner


@outer
def do_something():
    print("do_something() wurde ausgeführt")


# do_something = outer(do_something)


do_something()
do_something()
do_something()
do_something()
