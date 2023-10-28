# Proyecto_Arte

# Creación de un Museo de Imágenes de Arte con Ursina

Este proyecto tiene como objetivo mostrar cómo crear un museo virtual de imágenes de arte utilizando el motor de juegos Ursina en Python. Un museo de arte virtual es una forma interesante de presentar una colección de obras maestras artísticas de una manera interactiva y atractiva. Con Ursina, puedes construir una experiencia visual envolvente para los visitantes de tu museo.


### ***PRE-REQUISITOS*** 📋

***¿Qué cosas necesitas para ejecutar el proyecto de manera óptima? ¿como instalarlas?***
1. Utilizaremos el motor gráfico de la librería Ursina Engine.
   
   - Se instala a través de `pip` con el comando: `pip install ursina`
2. Una vez instalada la librería, podrás empezar a crear tu proyecto, que tendrá el siguiente formato:
   ```python
   from ursina import *

   app = Ursina()

   # Código

   app.run()
   
   ```
   
3. Recuerda revisar la siguiente página: [ursina cheat sheet](https://www.ursinaengine.org/cheat_sheet.html#models)
   - Encontrarás `models` `textures` `color` etc
4. Para dibujar una entidad
   ```python
   Entity(model='circle', position=(0,0,0), color=color.blue, texture='white33', rotation=(45,45,0))
   ```
5. Para observar los objetos en distintos ángulos
   ```python
   camera.orthographic = True
   EditorCamera()

## EXPRESIONES DE GRATITUD 🎁

* 😁 Comenta a otros sobre este proyecto 📢😀
* Invita un café ☕ a alguien del equipo. 
* 😉 Da las gracias públicamente 🤗.
* 👽👻🤖


## Configuración

1. Clona o descarga este repositorio en tu máquina local.

2. Asegúrate de tener todos los recursos (imágenes de arte) que deseas mostrar en el museo en una carpeta accesible.

3. Editar el archivo `main.py` para configurar la ubicación de tus imágenes y cualquier otra personalización necesaria.

## Ejecución

Ejecuta el programa `main.py`:


