import urllib.request, urllib.parse, urllib.error


# read from the url and save the content to the variable
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for each line decode, strip and print the results
#for line in fhand:
#    print(line.decode().strip())

counts = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
