def qsort(arr, lo, hi):
    def _pivot(arr, lo, hi):
        return arr[(lo+hi)//2]  

    def _partition(arr, lo, hi):
        p = _pivot(arr, lo, hi)
        i = lo
        j = hi
        while(True):
            while(i<len(arr) and arr[i]< p):
                i+=1
            while(j>0 and arr[j]>p):
                j-=1
            if i>=j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    if lo<hi:
        p = _partition(arr, lo, hi)
        qsort(arr, lo, p)
        qsort(arr, p+1, hi)

a = [1,3,5,9,4]
qsort(a, 0, len(a)-1)
print(a)
