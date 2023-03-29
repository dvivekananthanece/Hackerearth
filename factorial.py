received_number = int(input())
result = 1
for i in range(received_number, 0, -1):
    result *= i
print(result)
