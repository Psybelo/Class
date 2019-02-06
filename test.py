from Classes import Personne

oumar = Personne('Sylla', 'Oumar', 30)

print(oumar.nom, oumar.prenom)

mariana = Personne('Bello', 'Mariana', 35)

print(mariana.nom, mariana.prenom)

oumar.marcher(6)
mariana.marcher(7)

oumar.vieillir()
mariana.vieillir()

toto = Personne('Sylla', 'Toto', 0)
oumar.naissance_enfant(toto)

oumar.vieillir()
mariana.vieillir()
toto.vieillir()

tata = Personne('Sylla', 'Tata', 0)
oumar.naissance_enfant(tata)

