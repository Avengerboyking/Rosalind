with open("rosalind_rna.txt", "r") as f:
    dna = f.read()

rna = dna.replace("T", "U")
print(rna)