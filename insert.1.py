def insertion_sort(data):
    n = len(data)
    for i in range(n):
        val = data[i]
        j = i
        while j > 0 and data[j] > data[j - 1]:
            data[j],  data[j - 1] = data[j],  data[j - 1]
            i -= 1