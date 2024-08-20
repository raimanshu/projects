
words = ["donkey", "kaddu", "mote"]
with open("1.txt") as f:
    cont = f.read()

for word in words:
    cont  = cont.replace(word, "######")

with open("1.txt", 'w') as f:
    f.write(cont)