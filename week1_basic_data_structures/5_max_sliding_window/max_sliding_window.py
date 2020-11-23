# python3
from collections import deque, namedtuple


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


def max_sliding_window_eff(sequence, m):
    Element = namedtuple('Element', ['index', 'value'])
    dq = deque()
    for index, data in enumerate(sequence):
        if index - m >= 0:
            yield dq[0].value
        while dq and index - dq[0].index >= m:
            dq.popleft()
        while dq and dq[-1].value < data:
            dq.pop()
        dq.append(Element(index, data))
    yield dq[0].value


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_eff(input_sequence, window_size))

