print("ingrese la cantidad de respestas correctas del alumno:")
RP=int(input())
print("ingrese la cantidad de respestas incorrectas del alumno:")
RI=int(input())
print("ingrese la cantidad de respestas en blanco del alumno:")
RB=int(input())
R=int((RP*3)+(RI-RI-RI)+(RB*0))
print("el puntaje final del alumno es de:")
print(R)