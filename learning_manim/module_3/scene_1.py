from manim import *
import numpy as np

class Rotation(Scene):
    """
    Animates a square being rotated
    """

    def construct(self):
# 1. - create the square
        square = Square(side_length = 2, color = BLUE, fill_opacity = 0.3)
        square.move_to(ORIGIN)

# 2. - label the corners
        labels = VGroup(*[
            Dot(point, color = WHITE, radius = 0.06)
            for point in square.get_vertices()
        ])

# 3. - matrix display
        angle_tracker = ValueTracker(0)

        matrix_display = always_redraw(
            lambda: MathTex(
                rf"R(\theta) = \begin{{bmatrix}}"
                rf"{np.cos(angle_tracker.get_value()):.2f} & "
                rf"{-np.sin(angle_tracker.get_value()):.2f}\\"
                rf"{np.sin(angle_tracker.get_value()):.2f} & "
                rf"{np.cos(angle_tracker.get_value()):.2f}"
                rf"\end{{bmatrix}}"
            ).to_corner(UL).scale(0.7)
        )

# 4. - angle label
        angle_label = always_redraw(
            lambda: MathTex(
                rf"\theta = {np.degrees(angle_tracker.get_value()):.1f}^\circ"
            ).to_corner(UR).scale(0.8)
        )

        self.add(square, labels, matrix_display, angle_label)

# 5. - rotate the square (with updating matrix display)
        self.play(
            Rotate(square, angle = 2*np.pi, about_point = ORIGIN),
            Rotate(labels, angle = 2*np.pi, about_point = ORIGIN),
            angle_tracker.animate.set_value(2*np.pi),
            run_time = 6,
            rate_func = linear
        )
        self.wait(1)

# it's fascinating how the matrix lines up so that the square remains a square throughout, never getting mishapen or anything. Also this one took a while to render!