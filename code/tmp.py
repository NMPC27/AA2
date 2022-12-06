f = open("tmp.txt", "r")

fout = open("out.txt", "w")

for x in f:
    tmp=x.replace(".", ",")
    fout.write(tmp)

f.close()
fout.close()