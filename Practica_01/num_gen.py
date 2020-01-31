import os
import random

def rand_num():
    number = random.randint(0,100000)
    return number

path = "rand_numbers/"
aux = 1000

try:
    os.mkdir(path)
except OSError:
    print ("Directory already created %s" % path)
else:
    print ("Successfully created the directory %s" % path)

for i in range(1,101):
    file_name = "rand_numbers/rand_" + str(i) + "000"
    file = open(file_name, "w")
    for j in range(0,aux):
        file.write(str(rand_num()) + "\n")

    file.close()
    aux = aux + 1000