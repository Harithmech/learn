arr = [10, 20, 30, 40, 50]
n = len(arr)
for i in range(n):
    temp = arr[i]
    arr[i] = arr[n - i -1]
    arr[n-i-1] = temp
print(arr)
