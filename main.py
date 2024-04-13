mensaje = "hola mundo"

print(mensaje)

#jercicio 1 y 2
print("Bienvenido al mundo de la programación")
nombre = input("ingresa tu nombre \n")
print(f"Bienvenido {nombre}")

#ejercicio 3
print("ingresa el valor de x para resolver la siguiente ecuacion \n")
#ecuacion = int(input("(x**2+3x+1)/4")) 
#correccion, estoy entregando la formula, sin antes entregar el valor "x"
x = float(input("(x**2+3x+1)/4 \n"))
ecuacion = ((x**2+3*x+1)/4) # ** = para elevar * = para multiplicar 3x 

print(f"el valor de la ecuacion con x = {x} es igual a {ecuacion}")

#ejercicio 4
print("ingresa los datos para poder registrarte \n")
nomCompleto = input("ingresa tu nombre completo \n")
rut = input("ingresa tu rut con puntos y guion \n")
correo = input("ingrese su correo \n")
tel = input("ingrese su numero telefonico \n")

#imprimo los datos personales
dat = ("datos personales")

print("NOMBRE: \t", nomCompleto.upper())
print("RUT: \t\t", rut)
print("CORREO: \t", correo.upper())
print("TELEFONO: \t", tel)
