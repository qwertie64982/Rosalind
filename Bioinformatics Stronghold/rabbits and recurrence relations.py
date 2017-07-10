infile = open("rabbits and recurrence relations IN.txt", "r")
input = infile.readline()
months = int(input.rsplit(" ")[0])
offspring = int(input.rsplit(" ")[1])

numberAdults = 0
numberBabies = 1

for month in xrange(months):
    print numberAdults
    print numberBabies
    
    # setting current babies aside so they can be added to adults at the end
    numberGrowing = numberBabies
    numberBabies = 0
    
    # each adult has 3 babies
    numberBabies = offspring * numberAdults
    
    # previous babies grow up
    numberAdults += numberGrowing

print numberAdults
print numberBabies

outfile = open("rabbits and recurrence relations OUT.txt", "w+")
outfile.write(str(numberAdults))