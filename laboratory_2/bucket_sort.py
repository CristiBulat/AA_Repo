import time
import tracemalloc
import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr) // 10 + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) * (bucket_count - 1) // (max_val - min_val + 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

# Function to test Bucket Sort with different cases
def test_bucket_sort(name, dataset):
    arr = dataset.copy()

    tracemalloc.start()  # Start memory tracking
    start_time = time.time()  # Start time

    sorted_arr = bucket_sort(arr)

    end_time = time.time()  # End time
    memory_used = tracemalloc.get_traced_memory()[1]  # Peak memory usage
    tracemalloc.stop()  # Stop memory tracking

    return {"Dataset": name, "Time (s)": round(end_time - start_time, 6), "Memory (KB)": round(memory_used / 1024, 3)}

# Generate Different Datasets
n = 100000  # Large dataset size

datasets = [
    ("Random Large Dataset", [random.randint(1, 1000000) for _ in range(n)]),
    ("Nearly Sorted Dataset", sorted([random.randint(1, 1000000) for _ in range(n)])),
    ("Small Dataset", [random.randint(1, 100) for _ in range(50)]),
    ("Integer Limited Range (1-100)", [random.randint(1, 100) for _ in range(n)]),
    ("Floating-Point Dataset", [random.uniform(0.0, 1000000.0) for _ in range(n)])  # Works directly with floats
]

# Running Tests
results = [test_bucket_sort(name, data) for name, data in datasets]

# Convert to DataFrame and Display Results
df = pd.DataFrame(results)
print(df)

# Plot Results
plt.figure(figsize=(10, 5))
plt.bar(df["Dataset"], df["Time (s)"], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Dataset Type")
plt.ylabel("Time (s)")
plt.title("Bucket Sort Execution Time")
plt.xticks(rotation=15)
plt.show()
