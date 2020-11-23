def left_child(i):
    return (i * 2) + 1


def right_child(i):
    return (i * 2) + 2


def sift_down(i, arr, n):
    swaps, out = 0, []
    while True:
        mini = i
        left = left_child(i)
        right = right_child(i)
        if left < n and arr[left] < arr[mini]:
            mini = left
        if right < n and arr[right] < arr[mini]:
            mini = right
        if i != mini:
            arr[i], arr[mini] = arr[mini], arr[i]
            out.append((i, mini))
            swaps += 1
            i = mini
        else:
            break
    return swaps, out


def build_heap(n, arr):
    swaps = 0
    out = []
    for i in range((n - 1) // 2, -1, -1):
        res = sift_down(i, arr, n)
        swaps += res[0]
        out += res[1]
    return swaps, out


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    output = build_heap(n, arr)
    print(output[0])
    [print(*i) for i in output[1]]


if __name__ == '__main__':
    main()
