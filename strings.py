strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(0, 5):

    sentence = sentence + strings[i] + ' ' 

sentence += strings[6]
print (sentence)

print(' '.join(strings))
