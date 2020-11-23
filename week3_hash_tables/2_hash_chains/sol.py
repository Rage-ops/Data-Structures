# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.find(data):
            n = Node(data)
            n.next = self.head
            self.head = n

    def find(self, data):
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next
        if temp and temp.data == data:
            return True
        return False

    def delete(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
            else:
                temp = self.head
                prev = None
                while temp and temp.data != data:
                    prev = temp
                    temp = temp.next
                if temp and temp.data == data:
                    prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [LinkedList() for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.elems[query.ind].display()
        else:
            key = self._hash_func(query.s)
            if query.type == "add":
                self.elems[key].add(query.s)
            elif query.type == "del":
                self.elems[key].delete(query.s)
            else:
                self.write_search_result(self.elems[key].find(query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()