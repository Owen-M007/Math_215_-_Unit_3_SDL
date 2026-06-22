from manim import *
import numpy as np

class TracingCircle(Scene):
    """
    Animation of a dot tracing out
    a circular path
    """

    def construct(self):

# 1.
        axes = Axes(
            x_range=[-2, 2, 0.5], # [min, max, tick step]
            y_range=[-2, 2, 0.5],
            x_length=6,
            y_length=6,

            axis_config={"include_numbers": True} #,
        )

        self.add(axes)

# 2.
        r = 1.5

        guide_circle = Circle(
            radius=r * axes.x_length / (axes.x_range[1] - axes.x_range[0]),
            color=GRAY,
            stroke_opacity=0.4 #,
        )

        self.add(guide_circle)

# 3.
        angle_tracker = ValueTracker(0)

        dot = always_redraw(lambda: Dot(
            axes.c2p(
                r * np.cos(angle_tracker.get_value()),
                r * np.sin(angle_tracker.get_value()) #,
            ),
            color=YELLOW,
            radius=0.1 #,
        ))

# 4.
        radius_line = always_redraw(lambda: Line(
            start=axes.c2p(0,0),
            end=axes.c2p(
                r * np.cos(angle_tracker.get_value()),
                r * np.sin(angle_tracker.get_value()) #,
            ),
            color=BLUE,
            stroke_width=2
        ))

# 5.
        traced_path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=2)
        self.add(dot, radius_line, traced_path)

# 6.
        self.play(
            # angle_tracker.animate.set_value(2 * np.pi),
            # run_time=4,
            angle_tracker.animate.set_value(4 * np.pi),
            run_time=8,
            rate_func=linear #,
        )
        self.wait(1)