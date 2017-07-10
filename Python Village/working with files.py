outfile = open("working with files OUT.txt", "w+")
with open("working with files IN.txt", "r") as infile:
    isEvenLine = 0
    for line in infile:
        if isEvenLine:
            outfile.write(line)
        isEvenLine = not isEvenLine