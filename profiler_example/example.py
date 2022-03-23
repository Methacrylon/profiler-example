from time import sleep


def long_function():
    sleep(0.5)


def simple_print(i: int):
    print(f"Iteration n°: {i}")

def big_loop():
    for _ in range(1_000_000):
        ...


def outer_function(iteration: int):
    for i in range(iteration):
        long_function()
        simple_print(i)
        big_loop()


def main():
    outer_function(10)


if __name__ == "__main__":
    main()
