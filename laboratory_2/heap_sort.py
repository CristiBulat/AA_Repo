import time
import tracemalloc
import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Function to test Heap Sort with different cases
def test_heap_sort(name, dataset):
    arr = dataset.copy()

    tracemalloc.start()  # Start memory tracking
    start_time = time.time()  # Start time

    heap_sort(arr)

    end_time = time.time()  # End time
    memory_used = tracemalloc.get_traced_memory()[1]  # Peak memory usage
    tracemalloc.stop()  # Stop memory tracking

    return {"Dataset": name, "Time (s)": round(end_time - start_time, 6), "Memory (KB)": round(memory_used / 1024, 3)}


# Generate Different Datasets
n = 100000

datasets = [
    ("Random Large Dataset", [random.randint(1, 1000000) for _ in range(n)]),
    ("Nearly Sorted Dataset", sorted([random.randint(1, 1000000) for _ in range(n)])),
    ("Small Dataset", [random.randint(1, 100) for _ in range(50)]),
    ("Integer Limited Range (1-100)", [random.randint(1, 100) for _ in range(n)]),
    ("Floating-Point Dataset", [random.uniform(0.0, 1000000.0) for _ in range(n)])
]


results = [test_heap_sort(name, data) for name, data in datasets]


df = pd.DataFrame(results)
print(df)


plt.figure(figsize=(10, 5))
plt.bar(df["Dataset"], df["Time (s)"], color=['blue', 'green', 'red', 'purple', 'yellow'])
plt.xlabel("Dataset Type")
plt.ylabel("Time (s)")
plt.title("Heap Sort Execution Time")
plt.xticks(rotation=15)
plt.show()
