import random
import time

# generation
def generate_random_sequence(n, initial_length=10, length_multiplier=10):
    sequences = []
    length = initial_length
    for _ in range(n):
        sequence = [random.randint(1, 1000) for _ in range(length)]
        sequences.append(sequence)
        length *= length_multiplier
    return sequences

# bubble_sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# selection_sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def compare_sorting_algorithms(sequences):
    algorithms = [bubble_sort, quick_sort, selection_sort]
    algorithm_names = ['Bubble Sort', 'Quick Sort', 'Selection Sort']
    
    for i, sequence in enumerate(sequences):
        print(f"Sequence {i+1} - Length: {len(sequence)}")
        for j, algorithm in enumerate(algorithms):
            arr = sequence[:]
            start_time = time.time()
            algorithm(arr)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{algorithm_names[j]} - Elapsed Time: {elapsed_time:.6f} seconds")
        print()
#main
if __name__ == "__main__":
    n = 5 
    sequences = generate_random_sequence(n)
    compare_sorting_algorithms(sequences)