import random

def monte_carlo_pi(n):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n

N = 1_000_000
pi_est = monte_carlo_pi(N)
print(f"Оцінка числа π: {pi_est}")
