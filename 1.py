import pulp


model = pulp.LpProblem("Maximize Qnty", pulp.LpMaximize)


L = pulp.LpVariable('L', lowBound=0,  cat='Integer')  
J = pulp.LpVariable('J', lowBound=0,  cat='Integer')  

model += L + J
model += 2 * L + J <= 100 #Water
model += L <= 50 #Sugar
model += L <=30 #Lemon Juice
model += 2 * J <= 40 #Fruits

model.solve()

# Вивід результатів
print("Lemonade:", L.varValue)
print("Juice:", J.varValue)
