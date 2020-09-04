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
    nombre_datos = 'basededatos.txt'
    precio_dolar = 3669.85
    fichero = open(nombre_datos, "r")
    capacidad = 18000
    limite_kg_bulto = 500
    limite_kg1 = 25
    limite_kg2 = 300
    limite_kg3 = 500
    precio_1_kg = 0
    precio_2_kg = 1500
    precio_3_kg = 2500
    ingresos = 0
    bulto_maximo = 0
    bulto_minimo = limite_kg_bulto
    num_bultos_aceptados = 0
    num_bultos_check =0 
    peso_total = 0
    for b in fichero:
        num_bultos_check +=1
        bulto = float(b)
        if bulto < 0 or bulto > limite_kg_bulto:    
            print('Advertencia: El bulto' ,num_bultos_check, 'con peso ', bulto, 'kg sobrepasa el peso permitido por bulto, rechazado')
        elif peso_total + bulto > capacidad:
            print('Advertencia: Al aceptar el bulto', num_bultos_check, 'con peso ',bulto, ' kg se excede la capacidad de carga del avión, rechazado')         
        else:
            num_bultos_aceptados +=1
            peso_total +=bulto 
            if(bulto<bulto_minimo):bulto_minimo=bulto
            if(bulto>bulto_maximo):bulto_maximo=bulto                
            if bulto<limite_kg1:
                ingresos += bulto*precio_1_kg
            elif limite_kg1<bulto and bulto < limite_kg2:
                ingresos += bulto*precio_2_kg               
            elif limite_kg2<bulto and bulto < limite_kg3:
                ingresos += bulto*precio_3_kg                
    fichero.close() 
    
    print('Número total de bultos ingresados: ', num_bultos_aceptados)
    print('Peso del bulto más pesado: ', bulto_maximo)
    print('Peso del bulto más liviano: ', bulto_minimo)
    print('Promedio del peso de los bultos: ', peso_total/num_bultos_aceptados)
    print('Ingresos por concepto de carga en pesos: $', ingresos)
    print('Ingresos por concepto de carga en dolares: $', ingresos/precio_dolar)
if __name__== "__main__":
    main()
    