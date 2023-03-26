def generate_state(plaintext):
    return [[plaintext[i + 4*j]for j in range (4)]for i in range(4)]

def char2hex(char):
    return hex(ord(char))[2:]

def string2hex(string):
    return [char2hex(s) for s in string]

plaintext = 'didimus adhitya '
plain_hex = string2hex(plaintext)

key_text = 'adhitya didimus '
key_hex = string2hex(key_text)

state = generate_state(plain_hex)

key = generate_state(key_hex)

# subbytes

# shift row
for i in range(4):
    state[i] = state[i][i:] + state[i][:i]

# mix col

def byte(x, n = 8):
    return format(x, f'0{n}b')

def gal_mult(a, b):
    a = int(a,16)
    b = int(b,16)

    tmp = 0

    b_byte = bin(b)[2:]

    for i in range(len(b_byte)):
        tmp ^= int(b_byte[-1-i]) * (a << i)

    r_poly = int('100011011',2)

    r_poly_len = len(bin(r_poly)[2:])
    tmp_len = len(bin(tmp)[2:])

    diff = tmp_len - r_poly_len + 1

    for i in range(diff) :
        if (byte(tmp, tmp_len)[i] == '1') :
            tmp ^= r_poly << (diff - 1 - i)
    
    return tmp

def mix_col ():
    col_mixer = [
        [2,3,1,1],
        [1,2,3,1],
        [1,1,2,3],
        [3,1,1,2]
    ]

    res = []

    for i in range(4):
        for j in range(4):
            stack = []
            tmp = 0
            for k in range(4):
                a = state[k][i]
                b = hex(col_mixer[j][k])[2:]
                stack.append(gal_mult(a,b))
                # print(stack)
            for s in stack :
                tmp ^= s
            res.append(tmp)

    return generate_state(res)

for i in range(4):
    print(state[i])

print()

state = mix_col()

for i in range(4):
    for j in range(4):
        state[i][j] = hex(state[i][j])[2:]

for i in range(4):
    print(state[i])

print(state[1][2])
