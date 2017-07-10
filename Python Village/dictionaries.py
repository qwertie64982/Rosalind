infile = open("dictionaries IN.txt", "r")
string = infile.readline()
count = dict()

for word in string.rsplit():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

outfile = open("dictionaries OUT.txt", "w+")
for key in count:
    outfile.write(key)
    outfile.write(" ")
    outfile.write(str(count[key]))
    outfile.write("\n")