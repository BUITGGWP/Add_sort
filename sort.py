def itc_add_sort(data):
    for i in range(len(data)):
        j = i - 1 
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(*data)
    return data

n = int(input())
itc_add_sort(list(map(int, input().split())))
