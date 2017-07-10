infile = open("complementing a strand of dna IN.txt", "r")
inputDNA = infile.readline()

reverseDNA = inputDNA[::-1]

revComplementDNA = ""
for letter in reverseDNA:
    if letter == "A":
        revComplementDNA += "T"
    elif letter == "T":
        revComplementDNA += "A"
    elif letter == "C":
        revComplementDNA += "G"
    elif letter == "G":
        revComplementDNA += "C"
    else:
        print("ERROR: Invalid DNA input")
        exit()

outfile = open("complementing a strand of dna OUT.txt", "w+")
outfile.write(revComplementDNA)