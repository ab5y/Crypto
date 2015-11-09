import sys
import csv

def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def analyze(decoded):
	li_ch = []
	for ch in decoded:
		if ch >= 'A' and ch <= 'Z':
			li_ch.append(ch)
		elif ch == chr(0):
			li_ch.append('space')
		else:
			li_ch.append('null')
		li_ch.append(',')
	return li_ch

def main():
	for i in range(1, 11):
		li_xor = []
		with open('ct'+`i`+'.txt') as f:
			for line in f:
				output = ''
				for j in range(1,11):
					decoded = ''
					output = ''
					if i != j:
						with open('ct'+`j`+'.txt') as f2:
							for line2 in f2:
								xorCipher = strxor(line, line2).encode('hex')
								decoded = ''.join(chr(int(xorCipher[i:i+2], 16)) for i in range(0, len(xorCipher), 2))
								output = '#'+ `i` + ':' +line + '\n#' + `j` + ':' + line2 + '\n\n' + 'XOR #'+`i` + '+' + `j` +':\n' + xorCipher + '\nDecoded:\n' + decoded + '\n\n'
						with open('ct'+`i`+'XORs.txt', 'a') as the_file:
							the_file.write(output)
						li_xor.append(analyze(decoded))
		with open('ct'+`i`+'.csv', 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for row in li_xor:
				spamwriter.writerow(row)
main()