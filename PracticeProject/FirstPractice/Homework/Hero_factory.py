
from PracticeProject.FirstPractice.Homework.Police import police
from PracticeProject.FirstPractice.Homework.Timo import timo
class Hero_factory:

    def create_hero(self,name):
        if name == 'Police':
            return police()
        elif name == 'Timo':
            return timo()
        else:
            print("此英雄不在英雄工厂中")

hero_factory = Hero_factory()
Police = hero_factory.create_hero("Police")
Timo = hero_factory.create_hero("Timo")