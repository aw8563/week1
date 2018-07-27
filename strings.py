strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in strings:
    sentence +=  i + ' '

print(sentence.rstrip())

print(' '.join(strings))
