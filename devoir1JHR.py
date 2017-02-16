#coding: utf-8

for i in range(1930,2018) :

       for j in range(0,1000) :
       
        print (str(i)[2:] + format(j, "03d"));
       
# Solution très élégante! Bravo!

# Ton script fonctionne, mais comme la syntaxe est pointilleuse en python, il pourrait être amélioré pour en assurer la lisibilité et la robustesse sur les points suivants:
# 1 - Il est préféfable de ne pas mettre d'espace avant les deux-points dans les boucles «for»
# 2 - L'indentation doit être régulière (toujours 3, 4 ou 5 caractères, ou un «tab»)
# 3 - Il est préférable de ne pas mettre d'espace entre «print» et la parenthèse, comme on n'en met pas entre «range» et la parenthèse. C'est une question de consistance.
# 4 - Il n'est pas nécessaire de terminer les lignes par un point-virgule.

for i in range(1930,2018):
	for j in range(0,1000):
		print(str(i)[2:] + format(j, "03d"))