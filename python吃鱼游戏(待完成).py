# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:19:46 2017

@author: Tidus
"""
import random

class Fish:
    def __init__(self):
        self.posx = random.randint(1,10)
        self.posy = random.randint(1,10)    
        self.pos = [self.posx,self.posy]
        print('某条鱼儿出生位置是:',[self.posx,self.posy])
        
    def pos(self):
        return [self.posx,self.posy]

    
    def move(self):
        new_x = self.posx + random.choice([1,-1])
        new_y = self.posy + random.choice([1,-1])
        if new_x < 1:
            self.posx = 1 - (new_x - 1)
        elif new_x > 10:
            self.posx = 1- (new_x - 10)
        if new_y < 1:
            self.posy = 1 - (new_y - 1)
        elif self.posy > 10:
            self.posy = 1- (new_y - 10)
        else:
            return [self.posx,self.posy]

        
class Turtle:
    def __init__(self):
        self.posx = random.randint(1,10)
        self.posy = random.randint(1,10)    
        self.pos = [self.posx,self.posy]
        self.hl = 100
        print('乌龟的出生位置是:',self.pos)
        
    def move(self):

        distance = input('请输入行进方法(一步或者两步)：')
        direction = input('请输入行进方向：')
        if direction == '上' and distance == '2':
            self.pos[0] -= 2
            self.hl -= 2
        elif direction == '下' and distance == '2':
            self.pos[0] += 2
            self.hl -= 2
        elif direction == '左' and distance == '2':
            self.pos[1] -= 2
            self.hl -= 2
        elif direction == '右' and distance == '2':
            self.pos[1] += 2
            self.hl -= 2
        elif direction == '下' and distance == '1':
            self.pos[0] += 1
            self.hl -= 1
        elif direction == '左' and distance == '1':
            self.pos[1] -= 1
            self.hl -= 1
        elif direction == '右' and distance == '1':
            self.pos[1] += 1
            self.hl -= 1
        elif direction == '右' and distance == '1':
            self.pos[1] += 1
            self.hl -= 1
            
    def pos(self):
        if self.pos[0] < 1:
            self.pos[0] = 1 - (self.pos[0] - 1)
        elif self.pos[0] > 10:
            self.pos[0] = 1- (self.pos[0] - 10)
        if self.pos[1] < 1:
            self.pos[1] = 1 - (self.pos[1] - 1)
        elif self.pos[1] > 10:
            self.pos[1] = 1- (self.pos[1] - 10)
        else:
            return self.pos
    
    def eat(self):
        self.hl +=20
        if self.hl >100:
            self.hl = 100

fish = []
turtle = Turtle()

for i in range(10):
    f = Fish()
    new_fish = f.pos
    fish.append(new_fish)
 
while True:
    print('乌龟当前位置在：',turtle.pos)
    print('乌龟当前的体力是：',turtle.hl)
    print('某一条鱼儿当前位置在：',fish[random.randint(0,len(fish)-1)])
    if not len(fish):
        print('鱼儿死光了，游戏结束！')
        break
    if not turtle.hl:
        print('乌龟累死了，游戏结束！')
        break
    turtle.move()
    pos = turtle.pos
    for each_fish in fish[:]:
        if each_fish == pos:
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼儿被吃掉了...')
            print('鱼儿被吃掉的地点:',pos)
            print('还存活的鱼儿的位置:',fish)
        
