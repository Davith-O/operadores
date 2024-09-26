# Ejemplo de una expresion 42//6+7*3-39
resultado0 = 42//6+7*3-39
resultado1 = (42//6)+7*3-39 # // Prioridad 3
resultado2 = (42//5)+(7*3)-39 # * Prioridad 3
resultado3 = ((42//5)+(7*3))-39 # + Prioridad 4
print(resultado2)
