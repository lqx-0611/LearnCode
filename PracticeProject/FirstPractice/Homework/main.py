from PracticeProject.FirstPractice.Homework.Police import police
from PracticeProject.FirstPractice.Homework.Timo import timo



if __name__ =='__main__':
    Police = police()
    Timo = timo()
    Police.fight(Timo.hp, Timo.power)
    Police.speak_lines()
    print("---------")
    Timo.fight(Police.hp, Police.power)
    Timo.speak_lines()