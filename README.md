# Cryptography

This repo is for cryptography using python

## 1. RSA Encryption/Decryption

This code implements RSA encryption and decryption using Python. RSA is a public-key cryptosystem widely used for secure data transmission.

### How it works

1. Two random prime numbers are generated.
2. The product of the two primes is calculated to obtain n.
3. The Euler totient function z is calculated using (p-1)*(q-1).
4. A random integer e is chosen such that it is coprime with z.
5. The private key d is calculated such that d is the modular multiplicative inverse of e mod z.
6. The plaintext message is encrypted using the public key (n, e) and the ciphertext is obtained.
7. The ciphertext is decrypted using the private key (n, d) and the original plaintext message is obtained.

### How to use

1. Run the Python script rsa.py.
2. Choose one of the following options:
3. Encrypt: Enter the plaintext message you want to encrypt. The script will output the public and private keys, as well as the ciphertext.
4. Decrypt: Enter the ciphertext you want to decrypt, along with the public and private keys. The script will output the plaintext message.

### Notes

* The script generates random prime numbers in the range [2, 1000]. You can modify this range by changing the arguments in the range function in the random_prime_num function.
* The isPrime function is used to check whether a number is prime. It uses the Fermat primality test.
* The gcd function is used to calculate the greatest common divisor of two numbers using the Euclidean algorithm.
* The encrypt and decrypt functions implement the RSA encryption and decryption algorithms, respectively.
* The find_e function is used to find a random integer e that is coprime with z. It starts from 2 and iterates until it finds a suitable value.
* The pow function is used to calculate the modular inverse of e mod z.
  
## 2. AES
