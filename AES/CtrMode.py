from Crypto.Cipher import AES, XOR
from Crypto.Util import strxor
from Crypto import Random

class CtrMode:
	"""docstring for CtrMode"""
	# def __init__(self):

	def encrypt(self, message, key, iv = Random.new().read(AES.block_size)):
		# buffer_size = len(message) % 16
		# if buffer_size != 0:
		# 	for i in range(0, buffer_size):
		# 		message.append(`buffer_size`)
		begin = 0
		end = 16
		enc_msg = iv
		while begin < len(message):
			cipher = AES.new(key, AES.MODE_ECB, iv)
			enc_msg += cipher.encrypt(message[begin:end])
			begin = end
			end = end + 16
			iv = '{:X}'.format((int(iv, 16) + 1))
		return enc_msg

	def decrypt(self, ciphertext, key):
		dec_msg = ''
		iv = ciphertext[0:16]
		begin = 16
		end = 32
		counter = 0
		while begin < len(ciphertext):
			cipher = AES.new(key, AES.MODE_ECB, iv)
			if end > len(ciphertext):
				buffer_size = len(ciphertext[begin:end]) % 16
				if buffer_size != 0:
					i = 0
					while i < buffer_size:
						ciphertext += `buffer_size`
						i += 1
			dec_msg += cipher.encrypt(ciphertext[begin:end])
			begin = end
			end = end + 16
			iv = '{:X}'.format((int(iv, 16) + 1))
			counter += 1
		return dec_msg