from ursina import*
from ursina.shaders import transition_shader
import numpy as np
import sys
import time as time
from random import randint
camera.orthographic=True
camera.fov=4


app = Ursina()
Entity(model='plane', scale=(200,200,200), texture=load_texture('1.jpg'),rotation_x=-90, z=90)
#Entity(model=load_model('mi_modelo.obj'))
#de fondo una imagen
window.background = load_texture('galaxy.jpg')
#window.color = color.black10
# formato hexadecimal
#window.color = color.hex('#000000')


# funcion para crear un cubo
def crear_piso():
    for i in range(-15,15):
        for j in range(-15,15):
            Entity(model='cube',position=(i,-15,j), texture='space')
def crear_techo():
    for i in range(-15,15):
        for j in range(-15,15):
            Entity(model='cube',position=(i,15,j), texture='space')
def crear_pared4():
    for i in range(-15,15):
        for j in range(-15,15):
            Entity(model='cube',position=(i,j,15), texture='space')
def crear_pared1():
    for i in range(-15,15):
        for j in range(-15,15):
            Entity(model='cube',position=(15,i,j), texture='space')
def crear_pared2():
    for i in range(-15,15):
        for j in range(-15,15):
            Entity(model='cube',position=(-15,i,j), texture='space')

crear_piso()
crear_techo()
crear_pared4()
crear_pared1()
crear_pared2()


#el titulo se llama museo 
window.title = 'Museo'

#creando la letra M
def crear_M_l():
    for i in range(-38,-37):
        for j in range(46,51):
            Entity(model='cube',color=color.white, position=(i,j,-20), texture='start')

def crear_M_l2():
    for i in range(-34,-33):
        for j in range(46,51):
            Entity(model='cube',color=color.white, position=(i,j,-20), texture='start')

Entity(model='cube', position=(-37,50,-20), texture='start')
Entity(model='cube',position=(-36,49,-20), texture='start')
Entity(model='cube', position=(-35,50,-20), texture='start')

#creando la letra U
def crear_U_1():
    for i in range(-32,-31):
        for j in range(46,51):
            Entity(model='cube',position=(i,j,-20), texture='start')
#creando la letra U
def crear_U_2():
    for i in range(-29,-28):
        for j in range(46,51):
            Entity(model='cube',position=(i,j,-20), texture='start')

Entity(model='cube', position=(-32,46,-20), texture='start')
Entity(model='cube', position=(-31,46,-20), texture='start')
Entity(model='cube', position=(-30,46,-20), texture='start')

#creando la letra S
Entity(model='cube', position=(-26,50,-20), texture='start')
Entity(model='cube', position=(-25,50,-20), texture='start')
Entity(model='cube', position=(-24,50,-20), texture='start')

Entity(model='cube', position=(-26,48,-20), texture='start')
Entity(model='cube',position=(-25,48,-20), texture='start')
Entity(model='cube', position=(-24,48,-20), texture='start')

Entity(model='cube', position=(-26,46,-20), texture='start')
Entity(model='cube', position=(-25,46,-20), texture='start')
Entity(model='cube', position=(-24,46,-20), texture='start')

Entity(model='cube', position=(-24,47,-20), texture='start')
Entity(model='cube', position=(-26,49,-20), texture='start')

#creando la letra E
Entity(model='cube', position=(-21,50,-20), texture='start')
Entity(model='cube', position=(-20,50,-20), texture='start')
Entity(model='cube', position=(-19,50,-20), texture='start')

Entity(model='cube',position=(-21,48,-20), texture='start')
Entity(model='cube', position=(-20,48,-20), texture='start')

Entity(model='cube',position=(-21,46,-20), texture='start')
Entity(model='cube',position=(-20,46,-20), texture='start')
Entity(model='cube',position=(-19,46,-20), texture='start')

Entity(model='cube', position=(-21,47,-20), texture='start')
Entity(model='cube', position=(-21,49,-20), texture='start')

#creando O
#creando la letra  O
def crear_o_1():
    for i in range(-16,-15):
        for j in range(46,51):
            Entity(model='cube', position=(i,j,-20), texture='start')
#creando la letra U
def crear_o_2():
    for i in range(-14,-13):
        for j in range(46,51):
            Entity(model='cube',position=(i,j,-20), texture='start')
Entity(model='cube',position=(-15,50,-20), texture='start')
Entity(model='cube',position=(-15,46,-20), texture='start')

#M
crear_M_l()
crear_M_l2()
#U
crear_U_1()
crear_U_2()
#S
crear_o_1()
crear_o_2()

#creando cubos que se mueban,para ello necesito crear una clase
class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            model='cube',
            texture='gato',
            color=color.white,
            position=position,
            scale=(3,3,3),
            )
    def update(self):
        self.rotation_y += 1
        if held_keys['left arrow']:
            self.x -= 1 * time.dt
        if held_keys['right arrow']:
            self.x += 1 * time.dt
        if held_keys['up arrow']:
            self.z -= 1 * time.dt
        if held_keys['down arrow']:
            self.z += 1 * time.dt
        if held_keys['a']:
            self.y -= 1 * time.dt
        if held_keys['s']:
            self.y += 1 * time.dt

#creo el cubo
#nivel 1
cubo10 = Cubo(position=(5,-5,10))
cubo10 = Cubo(position=(-5,-5,10))

cubo10 = Cubo(position=(10,-5,2))
cubo10 = Cubo(position=(10,-5,-5))

cubo10 = Cubo(position=(-10,-5,2))
cubo10 = Cubo(position=(-10,-5,-5))

cubo10 = Cubo(position=(5,-5,-15))
cubo10 = Cubo(position=(-5,-5,-15))

#nivel 2
cubo10 = Cubo(position=(5,10,10))
cubo10 = Cubo(position=(-5,10,10))

cubo10 = Cubo(position=(10,10,2))
cubo10 = Cubo(position=(10,10,-5))

cubo10 = Cubo(position=(-10,10,2))
cubo10 = Cubo(position=(-10,10,-5))

cubo10 = Cubo(position=(5,10,-15))
cubo10 = Cubo(position=(-5,10,-15))
#------------------------------------------------------------------------------------------------------------------------------------------------------
#cubos se mueven en forma circular
class Cubo_mobible(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            model='cube',
            texture='gato',
            color=color.white,
            position=position,
            scale=(3,3,3),
            )
    def update(self):
        self.rotation_y += 1
        self.x = np.sin(time.time())*35
        self.z = np.cos(time.time())*35
        self.y = np.cos(time.time())*35

#creo el cubo
#cubo14 = Cubo2(position=(-15,-15,0))
cubo15 = Cubo_mobible(position=(70,10,5))

#cubo que se mueba en forma circular pero que tenga una rotacion en eje x
class Cubo_mobible_2(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            model='cube',
            texture='gato',
            color=color.white,
            position=position,
            scale=(3,3,3),
            )
    def update(self):
        self.rotation_y += 1
        self.x = np.sin(time.time())*25
        self.z = np.cos(time.time())*25
        self.y = np.cos(time.time())*25
        self.rotation_x += 1

#creo el cubo
cubo16 = Cubo_mobible_2(position=(-5,-5,10))

#escribire la palabra espacial con cubos
#E
#creando la letra E
Entity(model='cube', position=(-7,50,-20), texture='start')
Entity(model='cube', position=(-6,50,-20), texture='start')
Entity(model='cube', position=(-5,50,-20), texture='start')

Entity(model='cube',position=(-7,48,-20), texture='start')
Entity(model='cube', position=(-6,48,-20), texture='start')

Entity(model='cube',position=(-7,46,-20), texture='start')
Entity(model='cube',position=(-6,46,-20), texture='start')
Entity(model='cube',position=(-5,46,-20), texture='start')

Entity(model='cube', position=(-7,47,-20), texture='start')
Entity(model='cube', position=(-7,49,-20), texture='start')

#S
Entity(model='cube', position=(-3,50,-20), texture='start')
Entity(model='cube', position=(-2,50,-20), texture='start')
Entity(model='cube', position=(-1,50,-20), texture='start')

Entity(model='cube', position=(-3,49,-20), texture='start')

Entity(model='cube', position=(-3,48,-20), texture='start')
Entity(model='cube',position=(-2,48,-20), texture='start')
Entity(model='cube', position=(-1,48,-20), texture='start')

Entity(model='cube', position=(-3,46,-20), texture='start')
Entity(model='cube', position=(-2,46,-20), texture='start')
Entity(model='cube', position=(-1,46,-20), texture='start')

Entity(model='cube', position=(-1,47,-20), texture='start')

#P
Entity(model='cube', position=(2,50,-20), texture='start')
Entity(model='cube', position=(3,50,-20), texture='start')
Entity(model='cube', position=(4,50,-20), texture='start')

Entity(model='cube', position=(2,49,-20), texture='start')
Entity(model='cube', position=(2,48,-20), texture='start')
Entity(model='cube', position=(2,47,-20), texture='start')
Entity(model='cube', position=(2,46,-20), texture='start')

Entity(model='cube', position=(3,48,-20), texture='start')
Entity(model='cube', position=(4,48,-20), texture='start')
Entity(model='cube', position=(4,49,-20), texture='start')
#A

Entity(model='cube', position=(6,49,-20), texture='start')
Entity(model='cube', position=(6,48,-20), texture='start')
Entity(model='cube', position=(6,47,-20), texture='start')
Entity(model='cube', position=(6,46,-20), texture='start')

Entity(model='cube', position=(7,50,-20), texture='start')

Entity(model='cube', position=(8,50,-20), texture='start')
Entity(model='cube', position=(8,48,-20), texture='start')

Entity(model='cube', position=(7,48,-20), texture='start')

Entity(model='cube', position=(9,49,-20), texture='start')
Entity(model='cube', position=(9,48,-20), texture='start')

Entity(model='cube', position=(9,47,-20), texture='start')
Entity(model='cube', position=(9,46,-20), texture='start')

#C
Entity(model='cube', position=(11,50,-20), texture='start')

Entity(model='cube', position=(12,50,-20), texture='start')
Entity(model='cube', position=(13,50,-20), texture='start')

Entity(model='cube', position=(12,46,-20), texture='start')
Entity(model='cube', position=(13,46,-20), texture='start')

Entity(model='cube', position=(11,49,-20), texture='start')
Entity(model='cube', position=(11,48,-20), texture='start')
Entity(model='cube', position=(11,47,-20), texture='start')
Entity(model='cube', position=(11,46,-20), texture='start')

#I
Entity(model='cube', position=(15,50,-20), texture='start')
Entity(model='cube', position=(15,49,-20), texture='start')
Entity(model='cube', position=(15,48,-20), texture='start')
Entity(model='cube', position=(15,47,-20), texture='start')
Entity(model='cube', position=(15,46,-20), texture='start')

#A
Entity(model='cube', position=(17,49,-20), texture='start')
Entity(model='cube', position=(17,48,-20), texture='start')
Entity(model='cube', position=(17,47,-20), texture='start')
Entity(model='cube', position=(17,46,-20), texture='start')

Entity(model='cube', position=(18,50,-20), texture='start')

Entity(model='cube', position=(19,50,-20), texture='start')
Entity(model='cube', position=(19,48,-20), texture='start')

Entity(model='cube', position=(18,48,-20), texture='start')

Entity(model='cube', position=(20,49,-20), texture='start')
Entity(model='cube', position=(20,48,-20), texture='start')

Entity(model='cube', position=(20,47,-20), texture='start')
Entity(model='cube', position=(20,46,-20), texture='start')

#L
Entity(model='cube', position=(22,50,-20), texture='start')
Entity(model='cube', position=(22,49,-20), texture='start')
Entity(model='cube', position=(22,48,-20), texture='start')
Entity(model='cube', position=(22,47,-20), texture='start')
Entity(model='cube', position=(22,46,-20), texture='start')

Entity(model='cube', position=(23,46,-20), texture='start')
Entity(model='cube', position=(24,46,-20), texture='start')


#escribire la palabra "Barranco deconstruido" con cubos

#B
Entity(model='cube', position=(-40,-46,-20), texture='start')
Entity(model='cube', position=(-40,-47,-20), texture='start')
Entity(model='cube', position=(-40,-48,-20), texture='start')
Entity(model='cube', position=(-40,-49,-20), texture='start')
Entity(model='cube', position=(-40,-50,-20), texture='start')

Entity(model='cube', position=(-39,-50,-20), texture='start')
Entity(model='cube', position=(-38,-50,-20), texture='start')
Entity(model='cube', position=(-37,-50,-20), texture='start')

Entity(model='cube', position=(-39,-46,-20), texture='start')
Entity(model='cube', position=(-38,-46,-20), texture='start')
Entity(model='cube', position=(-37,-46,-20), texture='start')

Entity(model='cube', position=(-39,-48,-20), texture='start')


Entity(model='cube', position=(-38,-48,-20), texture='start')
Entity(model='cube', position=(-37,-49,-20), texture='start')
Entity(model='cube', position=(-37,-47,-20), texture='start')

#A
Entity(model='cube', position=(-35,-47,-20), texture='start')
Entity(model='cube', position=(-35,-48,-20), texture='start')
Entity(model='cube', position=(-35,-49,-20), texture='start')
Entity(model='cube', position=(-35,-50,-20), texture='start')

Entity(model='cube', position=(-34,-46,-20), texture='start')

Entity(model='cube', position=(-33,-46,-20), texture='start')
Entity(model='cube', position=(-33,-48,-20), texture='start')

Entity(model='cube', position=(-34,-48,-20), texture='start')

Entity(model='cube', position=(-32,-47,-20), texture='start')
Entity(model='cube', position=(-32,-48,-20), texture='start')

Entity(model='cube', position=(-32,-49,-20), texture='start')
Entity(model='cube', position=(-32,-50,-20), texture='start')

#R
Entity(model='cube', position=(-30,-46,-20), texture='start')
Entity(model='cube', position=(-30,-47,-20), texture='start')
Entity(model='cube', position=(-30,-48,-20), texture='start')
Entity(model='cube', position=(-30,-49,-20), texture='start')
Entity(model='cube', position=(-30,-50,-20), texture='start')

Entity(model='cube', position=(-29,-48,-20), texture='start')
Entity(model='cube', position=(-28,-48,-20), texture='start')   
Entity(model='cube', position=(-27,-48,-20), texture='start')

Entity(model='cube', position=(-29,-46,-20), texture='start')
Entity(model='cube', position=(-28,-46,-20), texture='start')
Entity(model='cube', position=(-27,-46,-20), texture='start')

Entity(model='cube', position=(-27,-47,-20), texture='start')


Entity(model='cube', position=(-28,-49,-20), texture='start')
Entity(model='cube', position=(-27,-50,-20), texture='start')

#R
Entity(model='cube', position=(-25,-46,-20), texture='start')
Entity(model='cube', position=(-25,-47,-20), texture='start')
Entity(model='cube', position=(-25,-48,-20), texture='start')
Entity(model='cube', position=(-25,-49,-20), texture='start')
Entity(model='cube', position=(-25,-50,-20), texture='start')

Entity(model='cube', position=(-24,-48,-20), texture='start')
Entity(model='cube', position=(-23,-48,-20), texture='start')
Entity(model='cube', position=(-22,-48,-20), texture='start')

Entity(model='cube', position=(-24,-46,-20), texture='start')
Entity(model='cube', position=(-23,-46,-20), texture='start')
Entity(model='cube', position=(-22,-46,-20), texture='start')

Entity(model='cube', position=(-22,-47,-20), texture='start')


Entity(model='cube', position=(-23,-49,-20), texture='start')
Entity(model='cube', position=(-22,-50,-20), texture='start')

#A

Entity(model='cube', position=(-20,-47,-20), texture='start')
Entity(model='cube', position=(-20,-48,-20), texture='start')
Entity(model='cube', position=(-20,-49,-20), texture='start')
Entity(model='cube', position=(-20,-50,-20), texture='start')

Entity(model='cube', position=(-19,-46,-20), texture='start')

Entity(model='cube', position=(-18,-46,-20), texture='start')
Entity(model='cube', position=(-18,-48,-20), texture='start')

Entity(model='cube', position=(-19,-48,-20), texture='start')

Entity(model='cube', position=(-17,-47,-20), texture='start')
Entity(model='cube', position=(-17,-48,-20), texture='start')

Entity(model='cube', position=(-17,-49,-20), texture='start')
Entity(model='cube', position=(-17,-50,-20), texture='start')

#N

Entity(model='cube', position=(-15,-46,-20), texture='start')
Entity(model='cube', position=(-15,-47,-20), texture='start')
Entity(model='cube', position=(-15,-48,-20), texture='start')
Entity(model='cube', position=(-15,-49,-20), texture='start')
Entity(model='cube', position=(-15,-50,-20), texture='start')

Entity(model='cube', position=(-14,-49,-20), texture='start')
Entity(model='cube', position=(-13,-48,-20), texture='start')
Entity(model='cube', position=(-12,-47,-20), texture='start')
Entity(model='cube', position=(-11,-46,-20), texture='start')

Entity(model='cube', position=(-11,-46,-20), texture='start')
Entity(model='cube', position=(-11,-47,-20), texture='start')
Entity(model='cube', position=(-11,-48,-20), texture='start')
Entity(model='cube', position=(-11,-49,-20), texture='start')
Entity(model='cube', position=(-11,-50,-20), texture='start')

#C
Entity(model='cube', position=(-9,-50,-20), texture='start')

Entity(model='cube', position=(-8,-50,-20), texture='start')
Entity(model='cube', position=(-7,-50,-20), texture='start')

Entity(model='cube', position=(-8,-46,-20), texture='start')
Entity(model='cube', position=(-7,-46,-20), texture='start')

Entity(model='cube', position=(-9,-49,-20), texture='start')
Entity(model='cube', position=(-9,-48,-20), texture='start')
Entity(model='cube', position=(-9,-47,-20), texture='start')
Entity(model='cube', position=(-9,-46,-20), texture='start')

#O

Entity(model='cube', position=(-5,-46,-20), texture='start')
Entity(model='cube', position=(-5,-47,-20), texture='start')
Entity(model='cube', position=(-5,-48,-20), texture='start')
Entity(model='cube', position=(-5,-49,-20), texture='start')
Entity(model='cube', position=(-5,-50,-20), texture='start')

Entity(model='cube', position=(-4,-46,-20), texture='start')
Entity(model='cube', position=(-4,-50,-20), texture='start')

Entity(model='cube', position=(-3,-46,-20), texture='start')
Entity(model='cube', position=(-3,-50,-20), texture='start')

Entity(model='cube', position=(-2,-46,-20), texture='start')
Entity(model='cube', position=(-2,-47,-20), texture='start')
Entity(model='cube', position=(-2,-48,-20), texture='start')
Entity(model='cube', position=(-2,-49,-20), texture='start')
Entity(model='cube', position=(-2,-50,-20), texture='start')

#formamos la palabra "deconstruido"

#D
Entity(model='cube', position=(2,-46,-20), texture='start')
Entity(model='cube', position=(2,-47,-20), texture='start')
Entity(model='cube', position=(2,-48,-20), texture='start')
Entity(model='cube', position=(2,-49,-20), texture='start')
Entity(model='cube', position=(2,-50,-20), texture='start')

Entity(model='cube', position=(3,-46,-20), texture='start')
Entity(model='cube', position=(4,-47,-20), texture='start')
Entity(model='cube', position=(5,-48,-20), texture='start')
Entity(model='cube', position=(4,-49,-20), texture='start')
Entity(model='cube', position=(3,-50,-20), texture='start')

#E
Entity(model='cube', position=(7,-46,-20), texture='start')
Entity(model='cube', position=(7,-47,-20), texture='start')
Entity(model='cube', position=(7,-48,-20), texture='start')
Entity(model='cube', position=(7,-49,-20), texture='start')
Entity(model='cube', position=(7,-50,-20), texture='start')

Entity(model='cube', position=(8,-46,-20), texture='start')
Entity(model='cube', position=(9,-46,-20), texture='start')
Entity(model='cube', position=(10,-46,-20), texture='start')

Entity(model='cube', position=(8,-48,-20), texture='start')
Entity(model='cube', position=(9,-48,-20), texture='start')

Entity(model='cube', position=(8,-50,-20), texture='start')
Entity(model='cube', position=(9,-50,-20), texture='start')
Entity(model='cube', position=(10,-50,-20), texture='start')

#C--------------------------------------------------
Entity(model='cube', position=(12,-46,-20), texture='start')
Entity(model='cube', position=(13,-46,-20), texture='start')

Entity(model='cube', position=(12,-46,-20), texture='start')
Entity(model='cube', position=(14,-46,-20), texture='start')

Entity(model='cube', position=(13,-50,-20), texture='start')
Entity(model='cube', position=(14,-50,-20), texture='start')

Entity(model='cube', position=(12,-47,-20), texture='start')
Entity(model='cube', position=(12,-48,-20), texture='start')
Entity(model='cube', position=(12,-49,-20), texture='start')
Entity(model='cube', position=(12,-50,-20), texture='start')

#O--------------------------------------
Entity(model='cube', position=(16,-46,-20), texture='start')
Entity(model='cube', position=(16,-47,-20), texture='start')
Entity(model='cube', position=(16,-48,-20), texture='start')
Entity(model='cube', position=(16,-49,-20), texture='start')
Entity(model='cube', position=(16,-50,-20), texture='start')

Entity(model='cube', position=(17,-46,-20), texture='start')
Entity(model='cube', position=(17,-50,-20), texture='start')

Entity(model='cube', position=(18,-46,-20), texture='start')
Entity(model='cube', position=(18,-50,-20), texture='start')

Entity(model='cube', position=(19,-46,-20), texture='start')
Entity(model='cube', position=(19,-47,-20), texture='start')
Entity(model='cube', position=(19,-48,-20), texture='start')
Entity(model='cube', position=(19,-49,-20), texture='start')
Entity(model='cube', position=(19,-50,-20), texture='start')

#N--------------------------------------------------

Entity(model='cube', position=(21,-46,-20), texture='start')
Entity(model='cube', position=(21,-47,-20), texture='start')
Entity(model='cube', position=(21,-48,-20), texture='start')
Entity(model='cube', position=(21,-49,-20), texture='start')
Entity(model='cube', position=(21,-50,-20), texture='start')

Entity(model='cube', position=(22,-49,-20), texture='start')
Entity(model='cube', position=(23,-48,-20), texture='start')
Entity(model='cube', position=(24,-47,-20), texture='start')
Entity(model='cube', position=(25,-46,-20), texture='start')

Entity(model='cube', position=(25,-46,-20), texture='start')
Entity(model='cube', position=(25,-47,-20), texture='start')
Entity(model='cube', position=(25,-48,-20), texture='start')
Entity(model='cube', position=(25,-49,-20), texture='start')
Entity(model='cube', position=(25,-50,-20), texture='start')

#S
Entity(model='cube', position=(27,-46,-20), texture='start')
Entity(model='cube', position=(28,-46,-20), texture='start')
Entity(model='cube', position=(29,-46,-20), texture='start')

Entity(model='cube', position=(27,-47,-20), texture='start')

Entity(model='cube', position=(27,-48,-20), texture='start')
Entity(model='cube',position=(28,-48,-20), texture='start')
Entity(model='cube', position=(29,-48,-20), texture='start')

Entity(model='cube', position=(27,-50,-20), texture='start')
Entity(model='cube', position=(28,-50,-20), texture='start')
Entity(model='cube', position=(29,-50,-20), texture='start')

Entity(model='cube', position=(29,-49,-20), texture='start')

#T
Entity(model='cube', position=(31,-46,-20), texture='start')
Entity(model='cube', position=(32,-46,-20), texture='start')
Entity(model='cube', position=(33,-46,-20), texture='start')
Entity(model='cube', position=(34,-46,-20), texture='start')
Entity(model='cube', position=(35,-46,-20), texture='start')

Entity(model='cube', position=(33,-47,-20), texture='start')    
Entity(model='cube', position=(33,-48,-20), texture='start')
Entity(model='cube', position=(33,-49,-20), texture='start')
Entity(model='cube', position=(33,-50,-20), texture='start')


#R--------------------------------------------------
Entity(model='cube', position=(37,-46,-20), texture='start')
Entity(model='cube', position=(37,-47,-20), texture='start')
Entity(model='cube', position=(37,-48,-20), texture='start')
Entity(model='cube', position=(37,-49,-20), texture='start')
Entity(model='cube', position=(37,-50,-20), texture='start')

Entity(model='cube', position=(38,-48,-20), texture='start')
Entity(model='cube', position=(39,-48,-20), texture='start')   
Entity(model='cube', position=(40,-48,-20), texture='start')

Entity(model='cube', position=(38,-46,-20), texture='start')
Entity(model='cube', position=(39,-46,-20), texture='start')
Entity(model='cube', position=(40,-46,-20), texture='start')

Entity(model='cube', position=(40,-47,-20), texture='start')


Entity(model='cube', position=(39,-49,-20), texture='start')
Entity(model='cube', position=(40,-50,-20), texture='start')

#U--------------------------------------------------
Entity(model='cube', position=(42,-46,-20), texture='start')
Entity(model='cube', position=(42,-47,-20), texture='start')
Entity(model='cube', position=(42,-48,-20), texture='start')
Entity(model='cube', position=(42,-49,-20), texture='start')
Entity(model='cube', position=(42,-50,-20), texture='start')

Entity(model='cube', position=(46,-50,-20), texture='start')
Entity(model='cube', position=(46,-49,-20), texture='start')
Entity(model='cube', position=(46,-48,-20), texture='start')
Entity(model='cube', position=(46,-47,-20), texture='start')
Entity(model='cube', position=(46,-46,-20), texture='start')

Entity(model='cube', position=(43,-50,-20), texture='start')
Entity(model='cube', position=(44,-50,-20), texture='start')
Entity(model='cube', position=(45,-50,-20), texture='start')

#I--------------------------------------------------
Entity(model='cube', position=(48,-46,-20), texture='start')
Entity(model='cube', position=(48,-47,-20), texture='start')
Entity(model='cube', position=(48,-48,-20), texture='start')
Entity(model='cube', position=(48,-49,-20), texture='start')
Entity(model='cube', position=(48,-50,-20), texture='start')

#D--------------------------------------------------
Entity(model='cube', position=(50,-46,-20), texture='start')
Entity(model='cube', position=(50,-47,-20), texture='start')
Entity(model='cube', position=(50,-48,-20), texture='start')
Entity(model='cube', position=(50,-49,-20), texture='start')
Entity(model='cube', position=(50,-50,-20), texture='start')

Entity(model='cube', position=(51,-46,-20), texture='start')
Entity(model='cube', position=(52,-47,-20), texture='start')
Entity(model='cube', position=(53,-48,-20), texture='start')
Entity(model='cube', position=(52,-49,-20), texture='start')
Entity(model='cube', position=(51,-50,-20), texture='start')

#O--------------------------------------------------
Entity(model='cube', position=(55,-46,-20), texture='start')
Entity(model='cube', position=(55,-47,-20), texture='start')
Entity(model='cube', position=(55,-48,-20), texture='start')
Entity(model='cube', position=(55,-49,-20), texture='start')
Entity(model='cube', position=(55,-50,-20), texture='start')

Entity(model='cube', position=(56,-46,-20), texture='start')
Entity(model='cube', position=(57,-46,-20), texture='start')

Entity(model='cube', position=(56,-50,-20), texture='start')
Entity(model='cube', position=(57,-50,-20), texture='start')

Entity(model='cube', position=(58,-46,-20), texture='start')
Entity(model='cube', position=(58,-47,-20), texture='start')
Entity(model='cube', position=(58,-48,-20), texture='start')
Entity(model='cube', position=(58,-49,-20), texture='start')
Entity(model='cube', position=(58,-50,-20), texture='start')

EditorCamera()
app.run()



