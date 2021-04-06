from Police import police
from Timo import timo

if __name__ =='__main__':
    Police = police()
    Timo = timo()
    Police.fight(Timo.hp, Timo.power)
    Police.speak_lines()
    print("---------")
    Timo.fight(Police.hp, Police.power)
    Timo.speak_lines()