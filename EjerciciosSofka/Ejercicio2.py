# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:19:26 2020

@author: restr


Un BOING 747 tiene una capacidad de carga para equipaje de aproximadamente 18.000
kg. Confeccione un algoritmo que controle la recepción de equipajes para este avión,
sabiendo que:
• Un bulto no puede exceder la capacidad de carga del avión ni tampoco exceder los 500
Kg.
• El valor por kilo del bulto es:
- de 0 a 25 Kg. cero pesos
- de 26 a 300 Kg. 1500 pesos por kilo de equipaje.
- de 301 a 500 Kg. 2500 pesos por kilo de equipaje
Para un vuelo cualquiera se pide:
a) Número total de bultos ingresados para el vuelo
b) Peso del bulto más pesado y del más liviano
c) Peso promedio de los bultos
d) Ingreso en pesos y en dólares por concepto de carga. Construya una tabla de
seguimiento con no menos de 15 bultos para realizar la prueba del algoritmo.
"""

def main():
    nombre_datos = 'basededatos.txt' #Nombre de la base de datos que contiene los bultos a ingresar     
    precio_dolar = 3669.85 #Precio del dolar el jueves 9 septiembre
    fichero = open(nombre_datos, "r") #se abre la base de datos y se guarda en el fichero
    capacidad = 18000 #Capacidad de carga del avión
    limite_kg_bulto = 500 #límite de kilogramos por bulto
    limite_kg1 = 25 #límite superior del primer rango de kilos  
    limite_kg2 = 300 #límite superior del segundo rango de kilos
    limite_kg3 = 500 #límite superior del tercer rango de kilos
    precio_1_kg = 0 # precio en pesos del primer rango de kilos
    precio_2_kg = 1500 # precio en pesos del segundo rango de kilos
    precio_3_kg = 2500 # precio en pesos del tercer rango de kilos
    ingresos = 0 #Variable que guarda los ingresos en pesos
    bulto_maximo = 0 #variable que guarda el peso máximo de los bultos recibidos 
    bulto_minimo = limite_kg_bulto #variable que guarda el peso mínimo de los bultos recibidos
    num_bultos_aceptados = 0 #guarda el número de bultos aceptados
    num_bultos_check =0 #guarda el número de bultos analizados
    peso_total = 0 #peso total de los bultos recibidos
    for b in fichero: #se recorre el fichero en orden y se analiza cada bulto
        num_bultos_check +=1 #cuenta el bulto en cuestión
        bulto = float(b) # el bulto leído entra como str y se convierte a float
        if bulto < 0 or bulto > limite_kg_bulto: # pesos no permitidos   
            print('Advertencia: El bulto' ,num_bultos_check, 'con peso ', bulto, 'kg sobrepasa el peso permitido por bulto, rechazado') #warning por bulto con peso inapropiado
        elif peso_total + bulto > capacidad: #si si al aceptar un bulto se excede con la capacidad de carga, no se admite pero se sigue intentando llenar el avión con unos más livianos
            print('Advertencia: Al aceptar el bulto', num_bultos_check, 'con peso ',bulto, ' kg se excede la capacidad de carga del avión, rechazado')         
        else: #Si se acepta el bulto    
            num_bultos_aceptados +=1 #se aumenta el número de bultos aceptados  
            peso_total +=bulto  #se incrementa el peso total de la carga
            if(bulto<bulto_minimo):bulto_minimo=bulto #Se guarda el mínimo peso de bulto hasta el momento     
            if(bulto>bulto_maximo):bulto_maximo=bulto #Se guarda el máximo peso de bulto hasta el momento              
            if bulto<limite_kg1: #El buto que pese ente 0 y el límite del rango 1, tiene valor precio1_kg por kilogramo
                ingresos += bulto*precio_1_kg # 
            elif limite_kg1<bulto and bulto < limite_kg2: #El buto que pese ente limite de rango 1 y el límite del rango 2, tiene valor precio2_kg por kilogramo
                ingresos += bulto*precio_2_kg               
            elif limite_kg2<bulto and bulto < limite_kg3:#El buto que pese ente limite de rango 1 y el límite del rango 2, tiene valor precio2_kg por kilogramo
                ingresos += bulto*precio_3_kg                
    fichero.close() #se cierra el fichero con los datos de los bultos 
    #Resultados
    print('Número total de bultos ingresados: ', num_bultos_aceptados) #número de bultos aceptados
    print('Peso del bulto más pesado: ', bulto_maximo) #peso del bulto más pesado
    print('Peso del bulto más liviano: ', bulto_minimo) #peso del bulto más liviano
    print('Promedio del peso de los bultos: ', peso_total/num_bultos_aceptados) #media del peso
    print('Ingresos por concepto de carga en pesos: $', ingresos)#total del ingresos en pesos   
    print('Ingresos por concepto de carga en dolares: $', ingresos/precio_dolar)#total de ingresos en dólares
if __name__== "__main__":
    main()
    
