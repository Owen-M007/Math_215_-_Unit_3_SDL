from manim import *
import numpy as np

class Transform(Scene):
    """
    Shows difference between scale
    then rotate and rotate then
    scale for non-uniform scaling
    """

    def construct(self):
        # starts with two rectangles
        rect_left = Rectangle(
            width = 1.75,
            height = 0.75,
            color = BLUE,
            fill_opacity = 0.4
            ).shift(LEFT * 2)
        
        rect_right = Rectangle(
            width = 1.75,
            height = 0.75,
            color = RED,
            fill_opacity = 0.4
            ).shift(RIGHT * 2)
        
        label_left = Text("first SCALE, then ROTATE", font_size = 16).next_to(rect_left, DOWN * 3)
        label_right = Text("first ROTATE, then SCALE", font_size = 16).next_to(rect_right, DOWN * 3)
        self.add(rect_left, rect_right, label_left, label_right)
        self.wait(1)

        # non-uniform scale matrix (stretch x by 2)
        scale_matrix = np.array([[2, 0], [0, 1]])

        # transform left rectangle
        self.play(
            ApplyMatrix(scale_matrix, rect_left),
            run_time = 1.5
        )
        self.play(
            Rotate(rect_left, PI/4, about_point = rect_left.get_center()),
            run_time = 1.5
        )

        # transform right rectangle
        self.play(
            Rotate(rect_right, PI/4, about_point = rect_right.get_center()),
            run_time = 1.5
        )
        self.play(
            ApplyMatrix(scale_matrix, rect_right),
            run_time = 1.5
        )
        self.wait(3)