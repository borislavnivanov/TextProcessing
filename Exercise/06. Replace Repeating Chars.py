text = input()
unique = [text[0]]
for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        unique.append(text[i])

print(''.join(unique))
