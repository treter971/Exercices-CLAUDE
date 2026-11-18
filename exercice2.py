prix_article = float(input("Prix de l'article : "))
pourcentage_reduction = int(input("Pourcentage de réduction : "))

reduction = prix_article * pourcentage_reduction / 100
prix_final = prix_article - reduction

print(f"Réduction : {reduction} €")
print(f"Prix final : {prix_final} €")