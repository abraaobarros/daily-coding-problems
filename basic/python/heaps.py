

def parent(i):
    return (i -1)//2
def right(i):
    return (i*2+1)+1
def left(i):
    return (i*2+1)

def swap(i,j, heap):
    heap[i], heap[j] = heap[j], heap[i]
    return heap

def insert(value, heap):
    heap.append(value)
    _current = len(heap)-1
    while(heap[_current] < heap[parent(_current)]):
        heap = swap(_current, parent(_current), heap)
        _current = parent(_current)

heap = []

insert(0, heap)
insert(2, heap)
insert(3, heap)
insert(8, heap)
insert(-1, heap)
insert(10, heap)
print(heap)