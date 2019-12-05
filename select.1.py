def selection_sort(data): 
    n = len(data)
    for i in range(n):
        smallest = data[i]
        smallest_idx = i
        for j in range(i, n):
            if data[j] < smallest:
                smallest_idx = j
                smallest = data[j]
        data[i], data[smallest_idx] = data[smallest_idx], data[i]