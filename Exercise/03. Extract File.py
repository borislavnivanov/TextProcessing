filepath = input().replace('.', '\\').split('\\')
print(f'File name: {filepath[-2]}\nFile extension: {filepath[-1]}')