import time

# deux classes indépendantes
# on constate déjà des similitudes entre les deux classes

class Predator:
    speed = 2  # vitesse de marche "normale"

    def __init__(self, pos):
        self.position = pos
        self.prey = None

    def set_prey(self, prey):
        self.prey = prey

    def go(self):
        # le lion bouge vers le buffle
        if self.position >= self.prey.position:
            # lion à droite du buffle => aller vers la gauche
            self.position -= self.speed
        else:
            # lion à gauche du buffle => aller vers la droite
            self.position += self.speed
        # envoyer le statut à Unity
        print(f"Lion:{self.position}|Biche:{self.prey.position}")

    def prey_caught(self):
        # retourne true si la proie et le prédateur sont très proches
        return abs(self.position - self.prey.position) <= 1


class Prey:
    speed = 1  # vitesse de marche "normale"
    proximity_distance = 20  # distance en dessous de laquelle la proie sent le prédateur

    def __init__(self, pos):
        self.position = pos
        self.predator = None

    def set_predator(self, predator):
        self.predator = predator

    def go(self):
        if abs(self.position - self.predator.position) <= self.proximity_distance:
            # si distance predator-prey trop courte alors prey tente de s'échapper
            if self.position > self.predator.position:
                # buffle à droite du lion => filer vers la droite
                self.position += self.speed
            else:
                # buffle à gauche du lion => filer vers la gauche
                self.position -= self.speed
        # envoyer l'état actuel à Unity
        print(f"Lion:{self.predator.position}|Biche:{self.position}")

    def prey_caught(self):
        return False


# MAIN
lion = Predator(50)  # position 0
buffle = Prey(100)  # position 100
lion.set_prey(buffle)
buffle.set_predator(lion)

animal_list = [lion, buffle]
while True:
    # chaque animal bouge
    for animal in animal_list:
        animal.go()

    # on vérifie si un animal est attrapé
    if any(animal.prey_caught() for animal in animal_list):
        print("Bon appétit !")
        break

    time.sleep(0.2)
