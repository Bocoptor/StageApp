nom_a = input("Entrez le nom de l'article :")
prix_ht = int(input("Entrez son prix HT :"))
nomb_ex = int(input("Entrez le nombre d'exemplaires :"))
taux_tva = int(input("Entrez le taux de TVA :"))

tva = taux_tva / 100
prix_t_htva = prix_ht * nomb_ex
prix_ttc = (prix_t_htva * tva) + prix_t_htva

print(f"Nom de l'article : {nom_a}")
print(f"Prix Hors TVA : {prix_ht}")
print(f"Nombre exemplaires : {nomb_ex}")
print(f"Taux TVA : {taux_tva}")
print(f"Prix total Hors TVA : {prix_t_htva}")
print(f"Prix total TTC : {prix_ttc}")