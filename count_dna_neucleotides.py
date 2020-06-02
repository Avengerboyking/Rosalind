with open("rosalind_dna.txt", "r") as dna:
    dna = dna.read()
    count = {}
    for i in dna:
        count[i] = dna.count(i)
print(count["A"], count["C"], count["C"], count["T"])