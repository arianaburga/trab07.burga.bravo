import os
#input
nro_de_cuenta=int(os.sys.argv[1])
#validador de datos
nro_de_cuenta_invalido=(nro_de_cuenta!="33322415")

while(nro_de_cuenta_invalido):
    nro_de_cuenta=input("ingrese el numero de cuenta")
    nro_de_cuenta_invalido=(nro_de_cuenta!="3322415")

#processing
for numero in nro_de_cuenta:
    print(numero)
#fin_iterar
print("fin del bucle")

#ouput
print("numero de cuenta:",nro_de_cuenta)
