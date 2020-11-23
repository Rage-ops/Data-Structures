class Node:
    def __init__(self, parent, rank, size):
        self.parent = parent
        self.rank = rank
        self.size = size

    def __str__(self):
        return 'Node(parent = {}, rank = {}, size = {})'.format(self.parent, self.rank, self.size)


class UnionFind:
    def __init__(self, arr):
        self.data = []
        self.max_count = max(arr)
        for index, value in enumerate(arr):
            self.data.append(Node(index, 0, value))

    def get_root(self, node):
        while self.data[node].parent != node:
            node = self.data[node].parent
        return node

    def union(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)

        if root_a == root_b:
            return self.max_count

        elif self.data[root_a].rank > self.data[root_b].rank:
            self.data[root_b].parent = root_a
            self.data[root_a].size += self.data[root_b].size
            self.max_count = max(self.max_count, self.data[root_a].size)

        elif self.data[root_a].rank == self.data[root_b].rank:
            self.data[root_b].parent = root_a
            self.data[root_a].rank += 1
            self.data[root_a].size += self.data[root_b].size
            self.max_count = max(self.max_count, self.data[root_a].size)

        else:
            self.data[root_a].parent = root_b
            self.data[root_b].size += self.data[root_a].size
            self.max_count = max(self.max_count, self.data[root_b].size)
        return self.max_count


def main():
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    tables = UnionFind(arr)
    for _ in range(m):
        a, b = map(int, input().split())
        print(tables.union(a-1, b-1))


if __name__ == '__main__':
    main()
