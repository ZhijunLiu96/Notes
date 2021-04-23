Python Cookbook
Contents
## Chapter 1: Data Structures and Algorithms

----

# Chapter 1: Data Structures and Algorithms

## Unpack

#### tuple
```python
>>> p = (4, 5)
>>> x, y = p
>>> x
4
```

#### string
```python
>>> a, b, c, d, e = 'hello'
>>> a
'h'
```

#### star expression
```python
>>> record = ('David', 'david@gmail.com', '773-555-1212', '847-555-1212', 'New York')
>>> name, email, *phone_numbers, address = record
>>> phone_numbers
['773-555-1212', '847-555-1212']
>>> address
'New York'

>>> records = [("foo", 1, 2),("bar", 3, 4)]
>>> for tag, *args in records:
...

>>> items = [1, 2, 3, 4]
>>> def sum(items):
...     head, *tail = items
...     return head + sum(tail) if tail else head
```

#### discard some value
```python
>>> name = ["Jane", "Liu"]
>>> first, _ = name
>>> first
"Jane"
```

#### keep the last N items
Use the data structure queue
```python
>>> from collections import deque
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)

"""
Other operations: 
    q.apeendleft(n), 
    q.pop(), 
    q.popleft()
"""
```

#### the largest/smallest N items
```python
>>> import heapq
>>> nums = [1,4,2,4,7,4,2,8,9,10]
>>> print(heapq.nlargest(3, nums))
[10, 9, 8]
>>> print(heapq.nsmallest(3, nums))
[1, 2, 2]

>>> portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
>>> cheap = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> import heapq
>>> heap = list(nums)
>>> heapq.heapify(heap)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

>>> heapq.heappop(heap)
-4
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
2
```


