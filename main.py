# ---------------------------------
p = 179
q = 191
o_binary_input = "111001010111011" # откр. текст
d_binary_output = "110010111001001" # заш. текст
e = 17
# ---------------------------------

# --------- start print ------------
# Функция для нахождения НОД двух чисел
def euclidean_algorithm(a, b):
    print(f"\nФункция для нахождения НОД({a},{b})")
    while b != 0:
        print(f'{a} = {a//b} * {b} + {a%b}')
        a, b = b, a % b
def extended_gcd(a, b):
    if a == 0:
        # print("a =", a, "b =", b)
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        # print(f"= (({b % a}) mod {a}) - ({b} / {a}) * {x}")
        print(f"{y} - ({b // a}) * {x} | => = {y - (b // a) * x}")
        return (g, y - (b // a) * x, x)
def modinv_algorithm(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    else:
        euclidean_algorithm(x, m)
# --------- end print ------------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    print(f"Найден обратный элемент: {x1} \n")
    return x1

print(f"Выбраны простые числа: p = {p}, q = {q}")
n = p * q
print(f"n = p * q = {p} * {q} = {n}")

phi_n = (p - 1) * (q - 1)
print(f"φ(n): φ(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_n}")

print(f"e = {e}")
euclidean_algorithm(e, phi_n)

if gcd(e, phi_n) != 1:
    raise ValueError("Выбранное значение e не взаимно просто с φ(n)")
print(f"Выбрано значение открытого экспонента e: {e}")
modinv_algorithm(e, phi_n)
d = modinv(e, phi_n)
print(f"Вычисление закрытого экспонента: \nd * e ≡ 1 (mod φ(n)) => \nd * {e} ≡ 1 (mod {phi_n})\nd = {d}")

# Функции шифрования и дешифрования
def encrypt(x):
    y = pow(x, e, n)
    print(f"Шифрование: y = x^e mod n = {x}^{e} mod {n} = {y}")
    return y

def decrypt(y):
    x = pow(y, d, n)
    print(f"Дешифрование: x = y^d mod n = {y}^{d} mod {n} = {x}")
    return x

print(f"\n---- ОТКРЫТЫЙ ТЕКСТ ----")
binary_input = o_binary_input
x = int(binary_input, 2)
print(f"Открытый текст (в двоичном виде): {binary_input}")
print("Преобразование двоичного числа в десятичное:")
decimal_value = 0
length = len(binary_input)
for i in range(length):
    bit = int(binary_input[length - 1 - i])
    contribution = bit * (2 ** i)
    decimal_value += contribution
    print(f"(2^{i}): {bit} * (2^{i}) = {contribution}")

print(f"Итоговое десятичное значение: {decimal_value}")
x_new = encrypt(x)
print(f"Зашифрованный текст (в десятичном виде): {x_new} (в двоичном виде: {bin(x_new)[2:]})")

print(f"\n---- ЗАШИФРОВАННЫЙ ТЕКСТ ----")
binary_output = d_binary_output
y = int(binary_output, 2)
print(f"Зашифрованный текст (в двоичном виде): {binary_output}")
print("Преобразование двоичного числа в десятичное:")
decimal_value = 0
length = len(binary_output)
for i in range(length):
    bit = int(binary_output[length - 1 - i])
    contribution = bit * (2 ** i)
    decimal_value += contribution
    print(f"(2^{i}): {bit} * (2^{i}) = {contribution}")
print(f"Итоговое десятичное значение: {decimal_value} ")
decrypted_x = decrypt(y)
print(f"Расшифрованный текст (в десятичном виде): {decrypted_x} (в двоичном виде: {bin(decrypted_x)[2:]})")
