# --------- start print ------------
def print_gcd(a, b):
    print(f"\nФункция для нахождения НОД({a},{b})")
    while b != 0:
        print(f'{a} = {a//b} * {b} + {a%b}')
        a, b = b, a % b
# --------- end print ------------
def extended_gcd(a, b):
    """Расширенный алгоритм Евклида для нахождения GCD и коэффициентов x, y"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    print(f"{y1} - ({b} / {a}) * {x1} =")
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Находит мультипликативную обратную к e по модулю phi"""
    print_gcd(e, phi)
    print()
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Обратного элемента не существует")
    else:
        print(f"=> обратный элемент = {x % phi}\n")
        return x % phi

def chinese_remainder(m_p, m_q, p, q):
    """Решает систему линейных сравнений с помощью КТО"""
    print("Решает систему линейных сравнений с помощью КТО")
    print(f"n = p * q = {p} * {q} = {p * q}")
    n = p * q
    # Находим k
    inv_pq = mod_inverse(p, q)
    print(f"k = (m_q - m_p) * {inv_pq} mod q = ({m_q} - {m_p}) * {inv_pq} mod {q} = {(m_q - m_p) * inv_pq % q}")
    k = (m_q - m_p) * inv_pq % q
    # Находим m
    print(f"m = m_p + k * p = {m_p} + {k} * {p} = {m_p + k * p} =>\n")
    return m_p + k * p

# Исходные данные
p = 223
q = 149
e = 17
y = int('101010001010101', 2)  # Преобразование двоичного представления в десятичное

print(f"\nШифртекст (в двоичном виде): y_2 = {bin(y)[2:]}")
print(f"Шифртекст (в десятичном виде): y_10 = {y}\n")

# 1. Вычисляем n
print("[1.] Вычисляем n")
n = p * q
print(f"Вычисляем n: n = p * q = {p} * {q} = {n}")

# 2. Вычисляем φ(n)
print("\n[2.] Вычисляем φ(n)")
phi_n = (p - 1) * (q - 1)
print(f"Вычисляем φ(n): φ(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_n}")

# 3. Вычисляем d, обратный к e по модулю φ(n)
print("\n[3.] Вычисляем d, обратный к e по модулю φ(n)")
d = mod_inverse(e, phi_n)
print(f"Вычисляем d: d ≡ e^(-1) (mod φ(n)) => d ≡ {e}^(-1) (mod {phi_n}) => d = {d}")

# 4. Вычисляем d_p и d_q
print("\n[4.] Вычисляем d_p и d_q")
d_p = d % (p - 1)
d_q = d % (q - 1)
print(f"Вычисляем d_p и d_q:\nd_p = d mod (p-1) = {d} mod ({p}-1) = {d_p},\nd_q = d mod (q-1) = {d} mod ({q}-1) = {d_q}")

# 5. Расшифровка по модулю p и q
print("\n[5.] Расшифровка по модулю p и q")
m_p = pow(y, d_p, p)
m_q = pow(y, d_q, q)
print(f"Расшифровка по модулю p и q:\nm_p = y^d_p mod p = {y}^{d_p} mod {p} = {m_p},\nm_q = y^d_q mod q = {y}^{d_q} mod {q} = {m_q}\n")

# 6. Используем КТО для нахождения m
print("\n[6.] Используем КТО для нахождения m")
m = chinese_remainder(m_p, m_q, p, q)
print(f"Используем КТО для нахождения m:\nm ≡ m_p (mod p),\nm ≡ m_q (mod q) =>")
print(f"m ≡ {m_p} (mod {p}),\nm ≡ {m_q} (mod {q}) =>\nm = {m}")

# Получаем открытый текст в двоичном виде
plain_text_binary = bin(m)[2:]  # Убираем '0b' в начале

print(f"\nРасшифрованный текст (в двоичном виде): {plain_text_binary}")
print(f"Расшифрованный текст (в десятичном виде): {m}")
