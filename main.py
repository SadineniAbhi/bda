import sys 

for lines in sys.stdin:
    words = lines.strip().split()
    for word in words:
        print(word, 1)

