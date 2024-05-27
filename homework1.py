example = 'Апельсин'
text1 = ['Первый вариант.\n', 'Второй вариант.\n','Третий вариант.\n']
text2 = ['Строка: ', 'Первый символ строки: ', 'Последний символ строки: ', 'Вторая половина строки: ', 'Cлово наоборот: ', 'Каждый второй символ строки: ']
a = '\n'
b = len(example) // 2
c = ''.join(reversed(example))
d = '\033[1m'
e = '\033[0m'
answer1 = str(text2[0]  + example + a + text2[1] + example[0] + a + text2[2] + example[-1] + a + text2[3] + example[b:] + a + text2[4] + example[::-1] + a + text2[5] + example[1::2])
answer2 = str(text2[0]  + example + a + text2[1] + example[0] + a + text2[2] + example[-1] + a + text2[3] + example[b:] + a + text2[4] + c  + a + text2[5] + example[1::2])
f = [example, example[0], example[-1], example[b:], example[::-1], example[1::2]]
g = str(len(text2) * a)
answer3 = [i + j + k for i, j, k in zip(text2, f, g)]
print(str(d + text1[0] + e + answer1 + a*2 + d + text1[1] + e + answer2 + a*2 + d + text1[2] + e + ''.join(answer3)))