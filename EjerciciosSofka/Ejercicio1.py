# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:41:17 2020

@author: LuisaFernandaRestrepo


Este programa determina  el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de
días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el
número de días de estancia es superior a 7, la línea aérea le hace un descuento del 30%.
(el precio por km. es de $35.00)
"""
def main():
    precio_km = 35   #Precio por kilómetro
    limite_km_descuento = 1000 #límite de kilómetros para aplicar el descuento
    limite_dias_descuento = 7 #límite de días para aplicar el descuento
    porcentaje_descuento = 0.3 #Porcentaje del descuento
    
    
    print('Para determinar el valor de su pasaje de avión es necesario que ingrese la distancia de su destino en kilómetros y la duración de su viaje en número de días')
    distancia = float(input('Ingrese la distancia en kilómetros: ')) #distancia ingresada por el usuario
    if(distancia<0): #Si la distancia es menor que 0 se muestra un aviso y se cierra el programa
        print('ingrese una distancia positiva')
        return        
    dias = float(input('ingrese la duración de su viaje en días: ')) #días ingresados por el usuario
    if(dias<0): #Si el número de días es negativo se muestra un aviso y se cierra el programa
        print('ingrese un número de días positivo')
        return 
    precio_boleto = precio_km*distancia #Cálculo de precio del pasaje sin descuentos
    
    if(distancia>limite_km_descuento and dias>limite_dias_descuento): #Si los km y los días superan los límites establecidos, se hace el descuento
        descuento = precio_boleto*porcentaje_descuento #Cálculo del descuento
        print('Como la distancia a recorrer supera los', limite_km_descuento, 'km y su estancia supera los', limite_dias_descuento, 'días, usted recibe un descuento del', 100*porcentaje_descuento,  '% en el valor de su pasaje')
        print('Valor del pasaje: $',precio_boleto )#valor sin descuento
        print('Valor del descuento: $', descuento) #Descuento
        print('Total a pagar: $', precio_boleto - descuento) #Valor con descuento
    else: 
        print('El valor de su pasaje es: $', precio_boleto) #precio del pasaje sin descuento
        
if __name__== "__main__":
    main()
    