
from PracticeProject.first_practice.homework.police import Police
from PracticeProject.first_practice.homework.timo import Timo
class HeroFactory:
    def create_hero(self,name):
        if name == 'Police':
            return Police()
        elif name == 'Timo':
            return Timo()
        else:
            print("此英雄不在英雄工厂中")

hero_factory = HeroFactory()
Police = hero_factory.create_hero("Police")
Timo = hero_factory.create_hero("Timo")