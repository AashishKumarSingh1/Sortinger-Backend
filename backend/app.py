from flask import Flask, request, jsonify
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

def bubble_sort(array):
    steps = []
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            steps.append(array.copy())
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    steps.append(array.copy())
    return steps

def selection_sort(array):
    steps = []
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps.append(array.copy()) 
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    steps.append(array.copy()) 
    return steps

def insertion_sort(array):
    steps = []
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        steps.append(array.copy()) 
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    steps.append(array.copy()) 
    return steps

def merge_sort(array):
    steps = []

    def merge(left, right):
        result = []
        while left and right:
            steps.append(left + right) 
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def sort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = sort(array[:mid])
        right = sort(array[mid:])
        return merge(left, right)

    sorted_array = sort(array)
    steps.append(sorted_array) 
    return steps

def quick_sort(array):
    steps = []

    def sort(array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        steps.append(left + middle + right) 
        return sort(left) + middle + sort(right)

    sorted_array = sort(array)
    steps.append(sorted_array)  
    return steps

def heapify(array, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        steps.append(array.copy()) 
        heapify(array, n, largest, steps)

def heap_sort(array):
    steps = []
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, steps)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        steps.append(array.copy())  
        heapify(array, i, 0, steps)

    steps.append(array.copy())  
    return steps

def counting_sort(array):
    steps = []
    sorted_array = sorted(array)
    steps.append(sorted_array)  
    return steps

def radix_sort(array):
    steps = []
    sorted_array = sorted(array)
    steps.append(sorted_array) 
    return steps

def bucket_sort(array):
    steps = []
    sorted_array = sorted(array)
    steps.append(sorted_array) 
    return steps

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    numbers = data.get('numbers', [])
    algorithm = data.get('algorithm', 'bubble_sort')
    steps = []

    if algorithm == 'Bubble Sort':
        steps = bubble_sort(numbers.copy())
    elif algorithm == 'Selection Sort':
        steps = selection_sort(numbers.copy())
    elif algorithm == 'Insertion Sort':
        steps = insertion_sort(numbers.copy())
    elif algorithm == 'Merge Sort':
        steps = merge_sort(numbers.copy())
    elif algorithm == 'Quick Sort':
        steps = quick_sort(numbers.copy())
    elif algorithm == 'Heap Sort':
        steps = heap_sort(numbers.copy())
    elif algorithm == 'Counting Sort':
        steps = counting_sort(numbers.copy())
    elif algorithm == 'Radix Sort':
        steps = radix_sort(numbers.copy())
    elif algorithm == 'Bucket Sort':
        steps = bucket_sort(numbers.copy())

    return jsonify({"steps": steps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
