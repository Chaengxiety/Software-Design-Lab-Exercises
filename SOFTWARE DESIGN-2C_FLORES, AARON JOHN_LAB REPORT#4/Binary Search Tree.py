def binary_search(list1, low, high, n):
    
    if low <= high:
        mid = (low + high) // 2
        if list1[mid] == n:
            return mid
        elif list1[mid] > n:
            return binary_search(list1, low, mid - 1, n)
        else:
            return binary_search(list1, mid + 1, high, n)

    else:
        return -1

list1 = [2,7,13,22,20,1]
n = 20

res = binary_search(list1, 0, len(list1) - 1, n)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in list1")  
