input = open("variables and some arithmetic IN.txt", "r")

line = input.read()
a = int(line.rsplit(" ")[0])
b = int(line.rsplit(" ")[1])

output = open("variables and some arithmetic OUT.txt", "w+")
out = str(a ** 2 + b ** 2)
output.write(out)