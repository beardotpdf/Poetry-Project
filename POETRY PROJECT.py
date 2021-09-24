import sys

#hiding actual directory for personal privacy, it ended on this file name in an undisclosed location
f = open("BaselineTestSpaceless.txt", "r")
# reads whole file into list; splits that list into new list with each index being an individual word
baseline = f.read()
f.close()

def permutations(elements):
    if len(elements) < 2:
        yield elements
    else:
        for i in range(len(elements)):
            for result in permutations(elements[:i] + elements[i+1:]):
                yield [elements[i]] + result

words = [baseline[2080],baseline[4],baseline[8],baseline[487]]

k = 0
for parts in list(permutations(words)):
    for i in range(k):
        for i in range(19):
            sys.stdout.write(' ')
    sys.stdout.write(' '.join(parts))
    sys.stdout.write("\n")
    k += 1

k = 0
for parts in list(permutations(words)):
    for i in range(30):
        sys.stdout.write(' ')
    sys.stdout.write(' '.join(parts))
    sys.stdout.write("\n")
    k += 1

k = 5
for parts in list(permutations(words)):
    for i in range(k):
        for i in range(19):
            sys.stdout.write(' ')
    sys.stdout.write(' '.join(parts))
    sys.stdout.write("\n")
    k -= 1

k = 0
for parts in list(permutations(words)):
    for i in range(55):
        sys.stdout.write(' ')
    sys.stdout.write(' '.join(parts))
    sys.stdout.write("\n")
    k += 1

k = 5
for parts in list(permutations(words)):
    for i in range(k):
        for i in range(19):
            sys.stdout.write(' ')
    sys.stdout.write(' '.join(parts))
    sys.stdout.write("\n")
    k -= 1

for parts in list(permutations(words)):
    print(' '.join(parts))