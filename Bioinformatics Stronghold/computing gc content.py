infile = open("computing gc content IN.txt", "r")
strings = dict()
counts = dict()

# Dump infile into strings
title = ""
contents = ""
for line in infile:
    if ">" in line:
        strings[title] = contents # only adds to strings when new title is discovered
        title = line
        title = title[1:-1] # remove ">" and newline
        contents = ""
    else: # concatenate multiple lines of nucleotides
        newString = line
        newString = newString[:-1] # remove newline
        contents += newString
strings[title] = contents
del strings[""]

# Fill counts with GC content values
cgCount = 0.0
totalCount = 0.0
for sample in strings:
    counts[sample] = strings[sample]
    for letter in strings[sample]:
        if letter == "C" or letter == "G":
            cgCount += 1
        totalCount += 1
    counts[sample] = 100 * (cgCount / totalCount)

# Find largest GC content in counts
tempLargest = counts[counts.keys()[0]] # set tempLargest to the first element
for sample in counts:
    if counts[sample] > tempLargest:
        tempLargest = counts[sample]
print tempLargest

outfile = open("computing gc content OUT.txt", "w+")
outfile.write()