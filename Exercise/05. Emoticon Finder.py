text = input()
symbol = ':'

for index, char in enumerate(text):
    if char == symbol:
        print(f'{symbol}{text[index + 1]}')