def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right= [x for x in arr if x>pivot]
    return quick_sort(left)+ middle +quick_sort(right)
print(quick_sort([5,3,8,6,2]))





def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Take input from user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted array:", quick_sort(arr))
