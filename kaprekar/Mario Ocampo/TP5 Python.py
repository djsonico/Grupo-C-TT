#El entorno usado es python 3.8 , el ide elegido es Pycharm 2020.1.1

entradas=int(input("Indique la cantidad de numeros que desee comprobar(entradas)"))
x=0 #Se declara un contador
const=int(6174) #Se declara la constante para luego ser comparada
while x!=entradas: #Se compara la cantidad de entradas elegidas por el usuario, con la variable contador
    numero= input("Elige un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido)")
    list(numero)
    while len(numero)!=4: #Se revisa si el numero ingresado, contiene 4 digitos.
        print("---------------Error---------------")
        print("El numero ingresado debe tener 4 digitos")
        print("")
        numero = (input("Elige un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido)"))
        list(numero)
    numero = int(numero)#Se convierte el la variable numero, a formato int. Para tener menos inconvenientes al momento de usarla.
    if numero == const or numero == 0000: #Se valida si el numero ingresado es igual a la constante de krapekar, o si el numero es 0000.
        print("El numero de iteraciones es: 0")
    elif numero == 1111 or numero == 2222 or numero == 3333 or numero == 4444 or numero == 5555 or numero == 6666 or numero == 7777 or numero == 8888 or numero == 9999: #Se revisa que los numeros ingresados no se repitan en los 4 digitos.
        print("El numero de iteraciones es: 8")
    else: #Si el numero ingresado no entra en las validaciones anteriores, se procede a realizar el calculo de la constante de Kaprekar.
        print("el numero que ingreso es:",numero)
        print("Realizando la constante de Kaprekar")
        print("-----------------------------------")
        numero=int(numero)
        for z in range(99):
            numero1="{:04d}".format(numero)  #Se le da formato a la variable numero, presentado el numero en 4 digitos (Si, es una revalidacion de lo ya validado).
            numeroGrande="".join(sorted(numero1,reverse=True))#Si el numero elegido fuera 1432, se ordena en 4321.
            numeroChico="".join(sorted(numero1))#Si el numero elegido fuera 1432, se ordena en 1234.
            numResta=int(numeroGrande)-int(numeroChico)#Se produce la resta del numero mas grande, con el numero mas chico.
            if numResta == const: #Una vez que se llega al valor de la constante de kaprekar, se ingresa al if, se muestra la cantidad de iteraciones y se termina el programa.
                print("numero de iteracion: "+"{:02}".format(z+1))
                break
            numero=numResta#Se asigna el resultado de la operacion resta, a la variable numero, para volver a comenzar el ciclo nuevamente. Pero con el numero obtenido.
    x=x+1 # Se le suma un valor a la variable contador.


