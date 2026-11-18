note = float(input("Saisire note : "))

if note >= 16:
    print("Votre note est de :", note, "Votre mention est : Tres bien")
elif note >= 14:
    print("Votre note est de :", note, "Votre mention est : Bien")
elif note >= 12:
    print("Votre note est de :", note, "Votre mention est : assez bien")
elif note >= 10:
    print("Votre note est de :", note, "Votre mention est : passable")
else:
    print("Votre note est de :", note, "Votre mention est : non admis")

print("appuyez sur une touche pour quitter")
