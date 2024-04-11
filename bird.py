from ursina import *

app = Ursina()
Sky()
bird = Animation('assets/bird.png', 
                  collider='box',
                  scale=(2,2,2),
                  y=5)
camera.orthographic = True
camera.fov = 20

app.run()