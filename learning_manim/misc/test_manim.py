from manim import *
import numpy as np

# class SmokeTest(Scene):
#     def construct(self):
#         circle = Circle(radius=1, color=BLUE)
#         self.play(Create(circle))
#         self.wait(1)


def circle(t, r=1.0):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x,y

t_vals = np.linspace(0, 2 * np.pi, 100)
x_vals, y_vals = circle(t_vals)
print(x_vals, y_vals)