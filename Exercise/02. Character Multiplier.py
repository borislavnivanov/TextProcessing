text1, text2 = input().split(' ')
num1 = [ord(x) for x in text1]
num2 = [ord(x) for x in text2]

max_size = max(len(num1), len(num2))
if len(num1) < max_size:
    for t in range(max_size - len(num1)):
        num1.append(1)
else:
    for t in range(max_size - len(num2)):
        num2.append(1)

result = 0

for element in zip(num2, num1):
    result += element[0] * element[1]

print(result)
