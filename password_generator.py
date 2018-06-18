import random

password_length_min = 8
password = ""
code = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'z', 'x', 'c',
        'v', 'b', 'n', 'm']
num = [i for i in range(10)]
code_1 = []
for i in code:
    code_1.append(i.upper())

for i, j in zip(code_1, num):
    code.append(i)
    code.append(j)


def generate_password():
    global password
    for i in range(int(password_length_min)):
        r = random.randint(0, len(code) - 1)
        password += str(code[r])
    print ( "Your new password : "+ password )

generate_password()
