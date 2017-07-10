infile = open("conditions and loops IN.txt", "r")
numbers = infile.readline()

a = int(numbers.rsplit(" ")[0])
b = int(numbers.rsplit(" ")[1])
total = 0

for i in range(a, b):
    if i % 2 != 0:
        total += i

outfile = open("conditions and loops OUT.txt", "w+")
outfile.write(str(total))