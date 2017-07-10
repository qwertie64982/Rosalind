infile = open("counting dna nucleotides IN.txt", "r")
string = infile.readline()
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for letter in string:
    count[letter] += 1

outfile = open("counting dna nucleotides OUT.txt", "w+")
outfile.write(str(count['A']))
outfile.write(" ")
outfile.write(str(count['C']))
outfile.write(" ")
outfile.write(str(count['G']))
outfile.write(" ")
outfile.write(str(count['T']))