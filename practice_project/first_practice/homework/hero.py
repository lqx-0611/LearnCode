# coding=utf-8
'''
课程里面所有的演示代码，自己独立完成（基础不好的同学， 选做）
使用简单工厂方法， 实现timo 和 police 两个英雄
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力

每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹
'''

class Hero:
    hp = 0
    power = 0
    Hero_name ='xx'
    '''   
    每个英雄都有一个 fight 方法：
    my_hp = hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    两个 hp 进行对比，血量剩余多的人获胜
    '''
    def fight(self,enemy_hp,enemy_power):
        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp-self.power
        if my_final_hp > enemy_final_hp:
            print(f"{self.Hero_name}赢了")
        elif my_final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("我们打平了")
    '''
    每个英雄都一个speak_lines方法
    调用speak_lines方法，不同的角色会打印（讲出）不同的台词
    timo : 提莫队长正在待命
    police: 见识一下法律的子弹
    '''
    def speak_lines(self):
        if self.Hero_name == "Timo":
            print('Timo:提莫队长正在待命')
        elif self.Hero_name == "Police":
            print('Police:见识一下法律的子弹')

