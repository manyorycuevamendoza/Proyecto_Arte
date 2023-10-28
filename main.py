from ursina import*
from ursina.shaders import transition_shader
import numpy as np
import sys
import time as time
from random import randint
camera.orthographic=True
camera.fov=4


app = Ursina()
#de fondo una imagen
window.background = load_texture('space')
#window.color = color.blue
# formato hexadecimal
#window.color = color.hex('#000000')


# funcion para crear un cubo
def crear_piso():
    for i in range(-20,20):
        for j in range(-20,20):
            Entity(model='cube',position=(i,-20,j), texture='space')
def crear_techo():
    for i in range(-20,20):
        for j in range(-20,20):
            Entity(model='cube',position=(i,20,j), texture='space')
def crear_pared4():
    for i in range(-20,20):
        for j in range(-20,20):
            Entity(model='cube',position=(i,j,20), texture='space')

crear_piso()
crear_techo()
crear_pared4()


#el titulo se llama museo 
window.title = 'Museo'

#creando la letra M
def crear_M_l():
    for i in range(-40,-39):
        for j in range(46,51):
            Entity(model='cube',color=color.white, position=(i,j,-20), texture='start')

def crear_M_l2():
    for i in range(-36,-35):
        for j in range(46,51):
            Entity(model='cube',color=color.white, position=(i,j,-20), texture='start')

Entity(model='cube', position=(-39,50,-20), texture='start')
Entity(model='cube',position=(-38,49,-20), texture='start')
Entity(model='cube', position=(-37,50,-20), texture='start')

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

EditorCamera()
app.run()



