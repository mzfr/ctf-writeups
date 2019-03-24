import requests
import string
import collections
import sets, sys

r = requests.get("https://www.ctfsecurinets.com/files/bbfe31808617c8c67fd9da96f1daa8bd/cipher.json").json()
ciphers = r['cipher_list']
target_cipher = r['cipher_flag']

def strxor(a, b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

final_key = [None]*150
known_key_positions = set()

for current_index, ciphertext in enumerate(ciphers):
    counter = collections.Counter()
    for index, ciphertext2 in enumerate(ciphers):
        if current_index != index:
            for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
                if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
    knownSpaceIndexes = []

    for ind, val in counter.items():
        if val >= 7: knownSpaceIndexes.append(ind)

    xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
    for index in knownSpaceIndexes:
        final_key[index] = xor_with_spaces[index].encode('hex')
        known_key_positions.add(index)

final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))

print("Fix this sentence:")
print(''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n")

target_plaintext = "I wanted to end the world, but I'll settle for ending yours"
print("Fixed:")
print(target_plaintext+"\n")

key = strxor(target_cipher.decode('hex'),target_plaintext)
print("key is", key)

print("Decrypted msg:")
for cipher in ciphers:
    print(strxor(cipher.decode('hex'),key))

print("\nPrivate key recovered: "+key+"\n")
