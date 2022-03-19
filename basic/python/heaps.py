
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
    while(heap[_current] < heap[parent(_current)] and _current > 0):
        heap = swap(_current, parent(_current), heap)
        _current = parent(_current)

def pop(heap):
    _size = len(heap)
    _last = len(heap)-1
    _current = 0
    heap = swap(_current, _last, heap)

    while(_current <= _size//2):
        if(heap[_current] > heap[left(_current)] 
            or heap[_current] > heap[right(_current)]):
            if(heap[left(_current)] < heap[right(_current)]):
                heap = swap(_current, left(_current), heap)
                _current = left(_current)
            else:
                heap = swap(_current, right(_current), heap)
                _current = right(_current)
        else:
            break
    heap.pop()
heap = []

insert(0, heap)
insert(2, heap)
insert(3, heap)
insert(8, heap)
insert(-1, heap)
insert(10, heap)
print(heap)
pop(heap)
print(heap)