#Tenemos que preguntar cuánto queda en cada moneda y dar el resultado en dólares.
print("Vamos a calcular cuánto te queda de dinero después del viaje a sudamérica, dando el resultado en dólares: ")
Pesos = int(input("Cuántos pesos mexicanos: "))    #1 peso mexicano son 0'06 dólares
Soles = int(input("Cuántos soles peruanos: "))    #1 real son 0'27 dólares
Reales = int(input("Cuántos reales brasileños: "))  #1 real brasileño con 0'20 dólares
print("Los pesos equivalen a: ",Pesos*0.06)
print("Los soles peruanos suman: ",Soles*0.27)
print("Y los reales son: ",Reales*0.20)
print("Te quedan un total de",Pesos*0.06+Soles*0.27+Reales*0.20,"dólares americanos")
#Soy un puto crack = )