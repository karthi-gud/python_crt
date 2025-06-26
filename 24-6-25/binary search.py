def BinarySearch(Arr, Target, offset=0):
    if len(Arr) == 0:
        print("Element does not exist")
        return
    Mid = len(Arr) // 2
    if Target == Arr[Mid]:
        print(f"Element Found at {offset + Mid} index")
    elif Target < Arr[Mid]:
        return BinarySearch(Arr[:Mid], Target, offset)
    else:
        return BinarySearch(Arr[Mid+1:], Target, offset + Mid + 1)

# Test the function
Output = BinarySearch([1, 2, 3, 4, 5], 5)