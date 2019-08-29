import secrets
import string

def newPassword(characters = 20):
	alphabet = string.ascii_letters + string.digits
	return ''.join(secrets.choice(alphabet) for i in range(characters))

if __name__ == '__main__':
	print(newPassword())
