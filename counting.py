# counting pattern
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# Defenitive Loops and Dictionaries
for key in counts:
    print(key, counts[key])

for k,v in counts.items():
    print(k, v)

# name = input('Enter file:')
# handle = open(name)

# counts = dict()
# for line in handle:
#   words = line.split()
#   for word in words:
#        counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#   if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count

# print(bitword, bigcount)
