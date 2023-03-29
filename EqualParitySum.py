N = 2
array = []
result = []


def content(logicArray):
    even = 0
    odd = 0
    index = 0
    for item in range(1, len(logicArray) + 1):
        if item % 2 == 0:
            even += logicArray[index]
            index = index + 1
        else:
            odd += logicArray[index]
            index = index + 1
    return odd, even


def anotherLogic(logicArray):
    for item in range(1, len(logicArray)-1):
        logicArray[item] *= -1
    odd, even = content(logicArray)
    if odd == even:
        result.append("YES")
    else:
        result.append("NO")


def logic(logicArray):
    odd, even = content(logicArray)
    if odd == even:
        result.append("YES")
    else:
        anotherLogic(logicArray)


logic([1, 5, -2, 3, -1])
print(result)
# for i in range(0, N):
#     k = [5, 4]
#     j = [{1, 5, -2, 3, -1}, [-10, 7, 9, -3]]
#     for j in range(0, k):
#         array.append(int(input()))
#     logic(array)
#     print(result)
