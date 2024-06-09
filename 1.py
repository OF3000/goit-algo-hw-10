import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
W = pulp.LpVariable('W', lowBound=0, upBound=100, cat='Integer')  # Кількість продукту А
S = pulp.LpVariable('S', lowBound=0, upBound=50, cat='Integer')  # Кількість продукту Б
L = pulp.LpVariable('L', lowBound=0, upBound=30, cat='Integer')  # Кількість продукту Б
P = pulp.LpVariable('L', lowBound=0, upBound=40, cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += 2 * W + S + L, "Profit"
model += 2 * P + W
# Додавання обмежень
# model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
# model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)
print("Виробляти продуктів Б:", B.varValue)
