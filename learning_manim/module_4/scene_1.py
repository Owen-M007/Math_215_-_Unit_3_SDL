from manim import *
import numpy as np
from math import gcd

class Hypotrochoid(Scene):
    """
    draws a spirograph animation
    """

    R = 5 # outer circle radius
    r = 3 # rolling circle radius
    d = 2.5 # pen distance from rolling center

    def construct(self):
        scale = 0.6 # scale factor from math units to manim screen units

# 1. - fixed outer circle
        outer = Circle(radius = self.R * scale, color = GRAY, stroke_opacity = 0.6)

# 2. - theta tracker
        theta = ValueTracker(0)

# 3. - inner center position
        def inner_center():
            t = theta.get_value()
            cx = (self.R - self.r) * np.cos(t) * scale
            cy = (self.R - self.r) * np.sin(t) * scale
            return np.array([cx, cy, 0])
        
# 4. - pen position
        def pen_pos():
            t = theta.get_value()
            px = ((self.R - self.r) * np.cos(t) 
                  + self.d * np.cos((self.R - self.r) / self.r * t)) * scale
            py = ((self.R - self.r) * np.sin(t) 
                  - self.d * np.sin((self.R - self.r) / self.r * t)) * scale
            return np.array([px, py, 0])
        
# 5. - rolling inner circle
        inner_circle = always_redraw(
            lambda: Circle(
                radius = self.r * scale,
                color = BLUE,
                stroke_opacity = 0.8
            ).move_to(inner_center())
        )

# 6. - pen dot
        pen = always_redraw(
            lambda: Dot(
                pen_pos(),
                color = YELLOW,
                radius = 0.1
            )
        )

# 7. - arm from inner center to pen
        arm = always_redraw(
            lambda: Line(
                inner_center(),
                pen_pos(),
                color = RED,
                stroke_width = 2
            )
        )

# 8. - center dot of inner circle
        inner_dot = always_redraw(
            lambda: Dot(
                inner_center(),
                color = BLUE_D,
                radius = 0.06
            )
        )

# 9. - pen's traced path
        traced = TracedPath(
            pen.get_center,
            stroke_color = YELLOW,
            stroke_width = 2
        )
        
        self.add(outer, inner_dot, inner_circle, arm, pen, traced)

# 10. - compute theta needed for a closed curve
        R_int = int(round(self.R))
        r_int = int(round(self.r))
        g = gcd(R_int, r_int)

        num_rotations = R_int // g
        end_theta = 2 * np.pi * num_rotations

        self.play(
            theta.animate.set_value(end_theta),
            run_time = 10,
            rate_func = linear
        )
        self.wait(2)