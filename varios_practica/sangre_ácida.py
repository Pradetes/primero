ph = int(input("Qué nivel de ph en sangre tienes?: "))
if ph>7:
  print("Tienes un nivel básico")
elif ph<7:
  print("Nivel ácido")
else:
  print("Neutro")