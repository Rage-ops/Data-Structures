import random


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def process_queries(queries):
    table = [None for _ in range(10 ** 7)]
    result = []
    for cur_query in queries:
        key = cur_query.number
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if table[key]:
                table[key].name = cur_query.name
            else:
                table[key] = cur_query

        elif cur_query.type == 'del':
            table[key] = None
        else:
            response = 'not found'
            if table[key]:
                response = table[key].name
            result.append(response)
    return result


def write_responses(result):
    print('\n'.join(result))


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))