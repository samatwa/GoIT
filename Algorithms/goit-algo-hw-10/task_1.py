import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_drink_production", pulp.LpMaximize)

# Визначення змінних(кількість виробленого лимонаду та фруктового соку)
limonade = pulp.LpVariable('Limonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Continuous')

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Додавання обмежень
model += (2 * limonade + 1 * fruit_juice <= water_limit, 'Water')
model += (1 * limonade <= sugar_limit, 'Sugar')
model += (1 * limonade <= lemon_juice_limit, 'Lemon_juice')
model += (2 * fruit_juice <= fruit_puree_limit, 'Fruit_puree')

# Оголошуєння цільової функції (максимізація загальної кількості напоїв)
model += (limonade + fruit_juice, 'Total_production')

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Optimal amount of 'Limonade' to produce: {limonade.varValue}")
print(f"Optimal amount of 'Fruit juice' to produce: {fruit_juice.varValue}")
print(f"Total production: {model.objective.value()}")
