import random

def isPrime(n) :
    return 2 in [n, 2**n%n]

def random_prime_num ():
    return random.choice([i for i in range (2,1000) if isPrime(i)])

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 

# def phi(n):
#     result = 1
#     for i in range(2, n):
#         if (gcd(i, n) == 1):
#             result+=1
#     return result

def encrypt (plain_text, e, n):
    return (plain_text**(e)) % n

def decrypt(cipher_text, d, n):
    return (cipher_text**(d)) % n

def find_e(start, z):
    while (start < z) :
        if (gcd(start, z) == 1) : 
            break
        else :
            start += 1
    return start 

# def rsa(plain_text, e, n, d):
    

#     cipher_text = encrypt(plain_text, e, n)
#     dechiper_text = decrypt(cipher_text, d, n)
    
    
#     return cipher_text
#     print(f'cipher text : {cipher_text}')
#     try :
#         print(f'decipher text : {dechiper_text}')
#     except :
#         print(f'd : {d}')
#         print(f'n : {n} and  e : {e}')


p = random_prime_num()
q = random_prime_num()
print(f"{p} and {q}")
n = p*q
z = (p-1)*(q-1)
print(f'n = {n}, z = {z}')
e = find_e(2, z)
d = pow(e, -1, z)

if __name__ == "__main__" :
    while (True) :
        print("RSA")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        try :
            choice = int(input(">>"))
        except :
            continue

        if choice == 3 :
            break

        if choice == 1 :
            plain_text = input("Input the Plain Text : ")
            cipher_text = []

            

            for p in plain_text :
                cipher_text.append(encrypt(ord(p), e, n))
            print(f'public key : {n} and {e}')
            print(f'private key : {n} and {d}')
            print(f'plain text : {plain_text}')
            print(f'cipher text : {cipher_text}')

            d_choice = input('Do you want to decrypt the result ? Y/N :')

            if d_choice.lower() == 'y' :
                plain_text = []
                for c in cipher_text :
                    plain_text.append(chr(decrypt(int(c), d, n)))
                print(f'plain text : {plain_text}')
            else :
                pass

        elif choice == 2 :
            cipher_text = input("Input the Cipher Text (ex. 42,24,12): ")
            plain_text = []
            pb_key = input("Input public key (n), (e): ")
            pr_key = input("Input private key (n), (d): ")
            cipher_list = cipher_text.split(',')

            n = int(pb_key.split(',')[0])
            e = int(pb_key.split(',')[1])
            d = int(pr_key.split(',')[1])

            for c in cipher_list :
                plain_text.append(chr(decrypt(int(c), d, n)))
            print(f'public key : {n} and {e}')
            print(f'private key : {n} and {d}')
            print(f'cipher text : {cipher_text}')
            print(f'plain text : {plain_text}')


        # else :
    #     pass

# import math
# print(math.fmod(3,2))
# print(3%2)
