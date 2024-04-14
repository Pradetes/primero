#El cálculo de la hipotenusa es la raíz cuadrada de a+b al cuadrado.
import numbers as nm
print("Vamos a calcular la hipotenusa. Por favor, introduce los siguientes valores: ")
Lado1 = int(input ("Introduce el lado A: "))
Lado2 = int(input ("Introduce el lado B: "))
import math
print("El resultado es",math.sqrt(round(Lado1**2+Lado2**2)))  #Cargamos "math" y ponemos la fórmula.