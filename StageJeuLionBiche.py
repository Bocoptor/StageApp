import time
import sys


position_lion = 0
position_biche = 100


vitesse_lion = 3
vitesse_biche = 2

while position_lion < position_biche:

    position_lion += vitesse_lion
    position_biche += vitesse_biche


    print(f"Lion: {position_lion} | Biche: {position_biche}")

    sys.stdout.flush()  # Vide le buffer immédiatement


    time.sleep(1)


print("Le lion a attrapé la biche!")
sys.stdout.flush()  # Vide le buffer final
