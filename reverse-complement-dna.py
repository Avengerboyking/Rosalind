with open("rosalind_revc.txt", "r") as f:
	file = f.read()
	reverse = file[::-1]
	n = reverse.replace('A', 't')
	n.replace('T','a')
	n.replace('G', 'c')
	n.replace('C', 'g')
print(n.upper())