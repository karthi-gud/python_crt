def bubble_sort_smaller(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage for names, just like you showed for numbers:
my_names = ["Charlie", "Alice", "Bob", "David", "Eve"]
print(f"Original: {my_names}")
sorted_names = bubble_sort_smaller(my_names)
print(f"Sorted: {sorted_names}")