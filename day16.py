#!/usr/bin/env python3
"""Problem - Day 16
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
class TailOrders():
    def __init__(self, n: int, ids: list=[]):
        self.n = n
        self._ids = ids
        self._ids_len = len(ids)

    def record(self, order_id: str):
        if self._ids_len < self.n:
            self._ids_len += 1
        else:
            del(self._ids[0])
        self._ids.append(order_id)

    def get_last(self, i: int) -> str:
        try:
            return self._ids[self.n - i]
        except IndexError:
            print('{0} is too large, must be {1} or less'.format(i, self.n))

if __name__ == '__main__':
    # create an empty TailOrders object
    n = int(input('number of order ids: '))
    t = TailOrders(n)

    # fill the empty object with ids using the record method
    ids = [input('order id: ') for _ in range(n)]
    [t.record(id) for id in ids]

    # get the record in the nth position from the end
    rec_id = t.get_last(int(input('get order (nth from last possition): ')))
    print(rec_id)

    # add a new record to the end, and confirm the oldest record is removed
    t.record(input('new record id: '))
    for i in range(n):
        print(t.get_last(i + 1))

    # alternatively, you can create the TailOrders object with the order ids in a list
    t2 = TailOrders(n, ids)
    print(t2._ids)

