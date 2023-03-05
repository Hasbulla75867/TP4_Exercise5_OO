"""
Programme fait par Raul Mic Nicolas
TP4 : Introduction à la programmation OO
Écrire une dataclass pour prendre en charge les caractéristiques d'un personnage de D&D.
    a) force, dextérité, constitution, intelligence, sagesse et charisme.
    b) Chaque attribut devra être initialisé à une valeur aléatoire entre 1 et 20.

"""

from dataclasses import dataclass
import random


@dataclass
class Avatar:
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class AvatarStats:
    def __init__(self):
        self.avatar = Avatar()


stats_jeu = AvatarStats()

# afficher les caractéristiques du personnage D&D
print(f"La force du avatar D&D est de {stats_jeu.avatar.force} points")
print(f"La dextérité du avatar D&D est de {stats_jeu.avatar.dexterite} points")
print(f"La constitution du avatar D&D est de {stats_jeu.avatar.constitution} points")
print(f"L'intelligence du avatar D&D est de {stats_jeu.avatar.intelligence} points")
print(f"La sagesse du avatar D&D est de {stats_jeu.avatar.sagesse} points")
print(f"Le charisme du avatar D&D est de {stats_jeu.avatar.charisme} points")
