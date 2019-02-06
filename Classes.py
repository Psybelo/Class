class Personne:

  def __init__(self, nom, prenom, age):
    self.nom = nom
    self.prenom = prenom
    self.age = age
    self.enfants = []

  def marcher(self, vitesse):
    print('Moi, {} {}, je marche à {} km/h'.format(self.prenom, self.nom, vitesse))

  def vieillir(self):
    self.age += 1
    print("Moi, {} {}, j'ai maintenant {} ans".format(self.prenom, self.nom, self.age))

  def naissance_enfant(self, enfant):
    # enfant est un objet de la classe Personne
    self.enfants.append(enfant)

    print("Moi, {} {}, j'ai maintenant {} enfants".format(self.prenom, self.nom, len(self.enfants) ))

    i = 0
    for enfant in self.enfants:
      i += 1
      print("Mon enfant numéro {} s'appelle {} {} et a {} ans".format(i, enfant.prenom, enfant.nom, enfant.age))
