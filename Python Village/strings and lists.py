infile = open("strings and lists IN.txt", "r")

string = infile.readline()
locations = infile.readline()
a = int(locations.rsplit(" ")[0])
b = int(locations.rsplit(" ")[1])
c = int(locations.rsplit(" ")[2])
d = int(locations.rsplit(" ")[3])

outfile = open("strings and lists OUT.txt", "w+")
outfile.write(string[a:b + 1])
outfile.write(" ")
outfile.write(string[c:d + 1])