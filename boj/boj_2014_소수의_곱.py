import heapq
from copy import deepcopy

K,N = map(int, input().split())
Prime_lst = list(map(int,input().split()))

lst = deepcopy(Prime_lst)
ck = set()

heapq.heapify(lst)
ith = 0

while ith < N:
    min_num = heapq.heappop(lst)

    if min_num in ck:
        continue

    ith += 1
    ck.add(min_num)

    for i in Prime_lst:
        if min_num * i < 2 ** 31:
            heapq.heappush( lst, min_num * i )

print(min_num)