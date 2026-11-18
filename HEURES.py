heures_a_faire = 7
heure_arrive = float(input("Saisir l'heure d'arrivée : "))

pause = 40 / 60

heure_depart = heure_arrive + heures_a_faire + pause

heures = int(heure_depart)
minutes = int((heure_depart - heures) * 60)

print(f"partir à {heures}h{minutes:02d}")
print("appuyer sur entrer")