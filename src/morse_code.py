morse_code_dict = {
	'A' :'.-','B' :'-...','C' :'-.-.',
	'D' :'-..','E' :'.','F' :'..-.',
	'G' :'--.','H' :'....','I' :'..',
	'J' :'.---','K' :'-.-','L' :'.-..',
	'M' :'--','N' :'-.','O' :'---',
	'P' :'.--.','Q' :'--.-','R' :'.-.',
	'S' :'...','T' :'-','U' :'..-',
	'V' :'...-','W' :'.--','X' :'-..-',
	'Y' :'-.--','Z':'--..','1' :'.---',
	'2' :'..---','3' :'...--','4' :'....-',
	'5' :'.....','6' :'-....','7' :'--...',
	'8' :'---..','9' :'----.','0' :'-----'
}

def encode_morse_cipher(msg):
	cipher_text = ''
	for letter in msg.upper() :
		if letter == ' ' :
			cipher_text += ' '
		else :
			cipher_text += morse_code_dict[letter]+ ' '
	return cipher_text


def decode_morse_cipher(cipher_text):
	pass

print encode_morse_cipher('shiva prasad')