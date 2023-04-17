from os import sep


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

h = str((((mins + dura)//60) + hour)%24) #
m = str((mins + dura)%60)

print ("Este evento finaliza a las: " +h +":" + m)
print("\nPresiona la tecla Enter para finalizar el programa.")
input()
print("FIN.")
