from practice_project.first_practice.homework.police import Police
from practice_project.first_practice.homework.timo import Timo



if __name__ =='__main__':
    Police = Police()
    Timo = Timo()
    Police.fight(Timo.hp, Timo.power)
    Police.speak_lines()
    print("---------")
    Timo.fight(Police.hp, Police.power)
    Timo.speak_lines()