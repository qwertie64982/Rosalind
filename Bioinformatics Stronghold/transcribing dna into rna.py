infile = open("transcribing dna into rna IN.txt", "r")
DNA = infile.readline()
RNA = ""

for letter in DNA:
    if letter == "T":
        RNA += "U"
    else:
        RNA += letter

outfile = open("transcribing dna into rna OUT.txt", "w+")
outfile.write(RNA)