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
	msg = ''
	cipher_list = cipher_text.split(' ')
	for item in range(len(cipher_list)):
		if len(cipher_list[item]) != 0 :
			for key, value in morse_code_dict.iteritems():
				if value == cipher_list[item]:
					msg += key
		else : 
			msg += ' '
	return msg
				
print encode_morse_cipher('Hello World')
print decode_morse_cipher('.... . .-.. .-.. ---  .-- --- .-. .-.. -..')
