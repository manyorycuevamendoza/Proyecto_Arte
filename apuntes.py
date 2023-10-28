# def crear_pared1():
#     for i in range(-35,35):
#         for j in range(-35,35):
#             Entity(model='cube',color=color.blue, position=(35,i,j), texture='blue')
# def crear_pared2():
#     for i in range(-35,35):
#         for j in range(-35,35):
#             Entity(model='cube', color=color.orange,position=(-35,i,j), texture='orange')

# def crear_pared4():
#     for i in range(-35,35):
#         for j in range(-35,35):
#             Entity(model='cube',color=color.yellow,  position=(i,j,35), texture='yellow')
   # crear_pared1()
# crear_pared2()
# crear_pared4()

#elimino el cubo que no quiero



# #para hacer la puerta, necesito que se mobible, por lo que creo una clase
# class Puerta(Entity):
#     def __init__(self, position=(0,0,0)):
#         super().__init__(
#             parent=scene,
#             model='cube',
#             texture='door',
#             color=color.pink,
#             position=position,
#             scale=(-5,5,1),
#             )
#     def update(self):
#         self.rotation_y += 1
#         if held_keys['left arrow']:
#             self.x -= 1 * time.dt
#         if held_keys['right arrow']:
#             self.x += 1 * time.dt
#         if held_keys['up arrow']:
#             self.z -= 1 * time.dt
#         if held_keys['down arrow']:
#             self.z += 1 * time.dt
#         if held_keys['a']:
#             self.y -= 1 * time.dt
#         if held_keys['s']:
#             self.y += 1 * time.dt
# #creo la puerta
# puerta = Puerta(position=(0,-22,-25))

#ursina game


#gris
Entity(model='cube',position=(-2,-3,16), texture='fuego')
#Entity(model='cube',color=color.red ,position=(-2,-4,16), texture='fuego')
Entity(model='cube',position=(-2,1,16), texture='fuego')

#Entity(model='cube',color=color.red ,position=(-1,1,16), texture='fuego')
#Entity(model='cube',color=color.red ,position=(-1,2,16), texture='fuego')

https://www.computerhope.com/cgi-bin/htmlcolor.pl?c=357EC7