import random

def is_prime(n):
    for _ in range(10):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_prime(bits):
    while True:
        x = random.getrandbits(bits) | 1
        if x % 4 == 3 and is_prime(x):
            return x

p = generate_prime(810)
q = generate_prime(810)
m = p * q
seed = random.randint(2, m - 1)

x = pow(seed, 2, m)
bits = []
for _ in range(20000):
    x = pow(x, 2, m)
    bits.append(x % 2)

print("p =", p)
print("q =", q)
print("m =", m)
print("seed =", seed)

ones = sum(bits)
print("Monobit:", "PASSED" if abs(ones - (20000 - ones)) < 200 else "FAILED")

run = max_run = 1
for i in range(1, len(bits)):
    run = run + 1 if bits[i] == bits[i-1] else 1
    max_run = max(max_run, run)
print("Long Run:", "PASSED" if max_run < 26 else "FAILED")