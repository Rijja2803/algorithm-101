import random
import time


def sort(a):
    compare = 0
    swap = 0
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            compare += 1
            if a[j] < a[min]:
                min = j
        swap += 1
        a[i], a[min] = a[min], a[i]

    return compare, swap


if __name__ == '__main__':
    l = [x for x in range(10000)]
    # l = [x for x in range(9999, -1, -1)]

    print('shuffling')
    random.shuffle(l)

    print('calling sort')
    start = time.process_time()
    compares, swaps = sort(l)
    end = time.process_time()

    print(f'min\t\t\t{l[0]}')
    print(f'max\t\t\t{l[-1]}')
    print(f'compares\t{compares}')
    print(f'swaps\t\t{swaps}')
    print(f'cpu time\t{end - start}')
