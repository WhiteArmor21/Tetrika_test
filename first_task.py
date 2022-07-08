import math


def task(array):
    array = array[::-1]
    return int(math.log2(int(array, base=2)+1))


if __name__ == '__main__':
    print(task("111111111110000000000000000"))
