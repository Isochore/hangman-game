import random # Importe le module aléatoire
import re # Importe le module de regex
reg = re.compile('[a-zA-Z]') # Déclaration d'une regex qui prend tout l'alphabet en minuscule et majuscule

# Dessin du pendu
hangpics = ['''
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Liste des mots avec split pour former une liste
words = 'agneau aigle albatros alligator alpaga anaconda ane antilope araignee autruche babouin baleine belette beluga biche bison blaireau boa boeuf bonobo brebis buffle cachalot campagnol canard capucin capybara caribou carpe castor cerf chacal chameau chamois chat chaus cheval chevre chevreuil chien chimpanze chinchilla chouette cigogne cobaye coccinelle cochon coq coyote crabe crocodile cygne daim dauphin dinde dindon dingo drill dromadaire ecureuil elan elephant emeu epaulard escargot espadon eyra faisan faon faucon fennec fouine fourmilier furet gaufre gaur gazelle gelada genette gerbille gerboise gibbon girafe glouton gnou gorille grenouille grizzly grue guanaco guepard guigna hamster herisson hermine heron hibou hippocampe hippopotame hirondelle hyene ibis iguane impala isard isatis jaguar kangourou kiwi koala kodiak koudou lamantin lama lapin lemming lemurien leopard lerot lezard lievre lion loir lophophore lori loup loutre lycaon lynx manchot mandrill mangouste manul mara marmotte marsouin martre mesange morse mouette moufette mouflon mouton mulet mulot musaraigne muscardin naja nandou narval nasique nason noctule notou numbat ocelot octodon oie okapi once opossum oran ornithorynque orque orycterope oryx otarie ouistiti ours panda pangolin panthere paon paresseux pecaris pekan pelican perroquet phacochere phoque pie pika pingouin pipistrelle pogona poisson polatouche poney poule poulpe poussin puma putois python quetzal quiscale quokka ragondin rat ratufa renard requin rhesus rhinoceros roussette salamandre sanglier serpent serval singe souris suricate tamandua tamanoir tamarin tamia tapir tarsier tatou taupe taureau tigre tortue toucan trigonocephale unau urubu vache varan vautour veau vipere vison wallabi wapiti watussi wombat xerus yack zebre zebrule zebu zibeline zorille'.split()
guessList = []
i = 0
missing = []

rnd = random.randint(0, len(words)-1) # Déclare un nombre aléatoire

currWord = words[rnd] # Sélectionne le mot aléatoire

for letter in currWord: # Remplit la liste des lettres manquantes
      missing.append("_")

print("\nDevinez le mot, il s'agit d'un animal.")

while True: # Boucle du jeu

      print(hangpics[i] + "\n") # Affiche le dessin du pendu
      if i == len(hangpics) - 1: # Si dernier dessin
            print("Vous avez perdu, le mot était : " + currWord)
            break
 
      print(" ".join(missing) + "\n") # Affiche les lettres manquantes avec une jointure pour plus de clarté

      print ("Lettres déjà utilisées : " + ", ".join(guessList) + "\n") # Affiche les lettres déjà proposées

      while True: # Boucle tant qu'une lettre n'a pas été correctement saisie

            print("Saisissez une lettre")
            guess = input() # Saisie
            if reg.match(guess) and guess not in guessList: # Si la lettre correspond à la regex
                  guess = guess.lower() # Met en minuscule
                  break
            elif guess in guessList: # Si lettre déjà proposée
                  print("Cette lettre a déjà été proposée")
            else:
                  print("Veuillez saisir un caractère valide")

      guessList.append(guess) # Ajoute la lettre à la liste de lettres proposées

      if guess in currWord: # Si la lettre se trouve dans le mot
            allIdx = [index for index, value in enumerate(currWord) if value == guess] # Cherche tous les index de la lettre dans le mot
            if len(allIdx) > 1: # Si la lettre s'y trouve plus d'une fois
                  for currIndex in allIdx: # Remplace les lettres manquantes par la lettre
                        missing[currIndex] = guess
            else: # Sinon elle apparaît qu'une fois
                  idx = currWord.index(guess)
                  missing[idx] = guess # On l'ajoute
      else: # La lettre ne se trouve pas dans le mot
            i += 1 # On incrémente de 1 l'index des dessins

      if missing.count("_") == 0: # S'il n'y a plus de lettres manquantes
            print("Bravo vous avez gagné, le mot était : " + currWord) # Le joueur a gagné
            break



