import random

#Euclid's algorithm for determining the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

#function to check if number is prime or not
def isPrime(n) :
    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

p = random.randrange(10, 100)
q = random.randrange(10, 100)

while not(isPrime(p) and isPrime(q)):
    p = random.randrange(10, 100)
    q = random.randrange(10, 100)
#Calculate N = P x Q.
n = p*q
#Compute: ø(n) = (p -1)(q -1)
#selecting at random the encryption key (public) e, where 1< e < ø(n), gcd(e,ø(n)) = 1
phi = (p-1)*(q-1)
e = random.randrange(1, phi)  #1<e<phi
while gcd(e, phi) != 1:
    e = random.randrange(1, phi)
#solving equation to find decryption key d, d * e = 1 mod ø(n) and 0 ≤ d ≤ n

def modInverse(e, phi) :
    e = e % phi;
    for d in range(1, phi) :
        if ((e * d) % phi == 1) :
            return d
    return 1

d = modInverse(e, phi)
print(d)

def encrypt(plaintext):

    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** e) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(ciphertext):
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** d) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)


print("###############################################################")
print("RSA Encrypter/ Decrypter")
message = input("Enter a message to encrypt with your public key: ")
encrypted_msg = encrypt(message)
print("Your encrypted message is: ", encrypted_msg)
print ("Decrypting message with private key ")
print("Your message is:")
print(decrypt(encrypted_msg))
print("################################################################")
print("ENCRYPTION INFO")
print("Your public key to encrypt the message is", e)
print("DECRYPTION INFO")
print("Your private key to decrypt the message is", d)
print("################################################################")
