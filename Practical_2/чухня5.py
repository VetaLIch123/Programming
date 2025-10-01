import math

# А) для заданої кількості членів ряду
def pi_series(n):
    s = 0
    for k in range(n):
        s += (-1)**k / (2*k + 1)
    return 4*s

N = 10000
pi_est = pi_series(N)
print(f"Обчислене π = {pi_est}, похибка = {abs(math.pi - pi_est)}")

# Б) для заданої похибки
def pi_for_error(err):
    s = 0
    k = 0
    while True:
        s += (-1)**k / (2*k + 1)
        pi_est = 4*s
        if abs(math.pi - pi_est) < err:
            return k+1, pi_est
        k += 1

terms, value = pi_for_error(1e-4)
print(f"Щоб отримати похибку < 1e-4, потрібно {terms} членів ряду. π ≈ {value}")
