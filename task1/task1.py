import sys

def circular_array_path(n, m):
    array = list(range(1, n + 1))
    print(array)
    path = []
    index = 0
    first = True
    while index != 0 or first:
        first = False
        path.append(array[index])
        index = (index + m-1) % n

    return ''.join(map(str, path))

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular_array_path(n, m))
