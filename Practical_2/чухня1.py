score = int(input("Введіть число від 1 до 100:"))

# Варіант через if
if score > 90:
    grade = 'відмінно'
elif score > 50:
    grade = 'задовільно'
else:
    grade = 'незадовільно'

print(f'IF: Ви набрали {score} балів, оцінка - {grade}.')

# Варіант через тернарний оператор
grade = 'відмінно' if score > 90 else 'задовільно' if score > 50 else 'незадовільно'
print(f'TERN: Ви набрали {score} балів, оцінка - {grade}.')
