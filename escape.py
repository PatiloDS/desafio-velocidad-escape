# Patricio Carrasco Zura
# Ve: corresponde a la Velocidad de Escape en [m/s].
# g: corresponde a la constante gravitacional en [m/s2].
# r: Corresponde al radio del planeta en [m]
import math

print(" se realizara el calculo de la velocidad de escape")
gravedad = float(input("ingrese el radio [en metros]: "))
radio = float(input("ingrese el radio [en kilometros]: "))
rmt= radio*1000
ve1=2*rmt*gravedad
ve= math.sqrt(ve1)
print(f"la velocidad de escape es: {ve}")
