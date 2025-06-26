def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Take input from user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"After comparing index {j} and {j+1}: {arr}")

# Take input from user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)