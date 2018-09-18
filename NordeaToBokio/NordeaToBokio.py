# Bokföringsdatum	Bokfört belopp (SEK)	Till/från konto	Till/från namn	Referens/meddelande	Utgående saldo	Utländskt belopp	Valutakod	Landkod	Betalkod	Egna anteckningar
def process(file):
	fields = file.split('\t')
	fields = [ x.strip() for x in fields ]
	del fields[5:]
	del fields[2]
	message = ': '.join(fields[2:])
	new_line = '\t'.join([fields[0], fields[1], message])
	print(new_line)
	output.write(new_line + '\n')

output = open('bokio.txt', 'w')
		  
with open('nordea.txt') as f:
	for line in f:
		process(line)
		



output.close()
f.close()
