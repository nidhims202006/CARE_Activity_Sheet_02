def LargeSmallSum(arr):

    if len(arr) <= 3:
        return 0

    even = []
    odd = []

    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    even.sort(reverse=True)
    odd.sort()

    return even[1] + odd[1]

arr = [3, 2, 1, 7, 5, 4]

print(LargeSmallSum(arr))
