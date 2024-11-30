from string import ascii_letters, digits, punctuation
from itertools import product

for password in product(ascii_letters + digits + punctuation, repeat=8):
    print(password)
