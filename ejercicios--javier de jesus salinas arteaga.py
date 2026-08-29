# =============== 1.py ===============

edad = int(input("Ingrese su edad: "))

ingresos = int(input("Ingrese su ingreso mensual: "))

if edad < 16 and ingresos >= 1000:
    print("tienes que atributar")
else:
    print("No tienes que atributar")

# =============== 2.py ===============

renta = float(input("Ingrese su renta anul en €: "))

if renta < 10000:
    print("tipo de imposiotivo: 5%")
elif renta >= 10000 and renta < 20000:
    print("tipo de imposiotivo: 15%")
elif renta >= 20000 and renta < 35000:
    print("tipo de imposiotivo: 20%")
elif renta >= 35000 and renta < 60000:
    print("tipo de imposiotivo: 30%")
else:
    print("tipo de imposiotivo: 45%")    
        

# =============== 3.py ===============

edad = int(input("Ingrese su edad: "))

precio = float(input("Ingrese el precio del producto: "))

if edad < 18 :
    descuento = 10
elif edad >= 18 and edad <= 65:
    descuento = 0
else:
    descuento = 15

descuento_total = precio * (descuento / 100)
precio_final = precio - descuento_total

print (f"El precio final es de: {precio_final}")


# =============== 4.py ===============

nota = int(input("Ingrese su nota: "))

if nota >= 90:
    print("excelente")
elif nota >= 70 and nota <= 89:
    print("bueno")
elif nota >= 60 and nota <= 69:
    print("regular")
elif nota < 60:
    print("reporbado")
else:
    print("nota invalida") 

# =============== 5.py ===============

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")    


# =============== 6.py ===============

print("Ingrese los valores de los lados del triángulo:")
lado1 = int(input("Digite el valor del lado 1: "))
lado2 = int(input("Digite el valor del lado 2: "))    
lado3 = int(input("Digite el valor del lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("es isósceles")
else:
    print("es escaleno")

# =============== 7.py ===============

saldo = 5000
print("Su saldo actual es:", saldo)
retiro = int(input("Ingrese la cantidad que desea retirar: "))

if retiro <= saldo:
    saldo -= retiro
    print("Retiro exitoso. Su nuevo saldo es:", saldo)
else:
    print("Fondos insuficientes.")

# =============== 8.py ===============

num = int(input("Ingrese un número: "))

for i in range(num, -1, -1):
   if i == 0:
       print(i)
   else:
         print(i, end=",")

# =============== 9.py ===============

num = int(input("Ingrese el numero para generar su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{i} X {num} = {i * num}")

# =============== 10.py ===============

contra = "uwu"
intento = ""

while intento != contra:
    intento = input("Ingrese la contraseña: ")
    if intento == contra:
        print("Contraseña correcta. Acceso concedido.")
    else:
        print("Contraseña incorrecta. Intente nuevamente.")

