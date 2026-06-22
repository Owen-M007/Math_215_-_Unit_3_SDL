from manim import *
import numpy as np

class TracingEllipse(Scene):
    """
    Animation of a dot tracing out
    an elliptical path
    """

    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
        self.add(axes)

        a = 2
        b = 1
        omega = 1 # angular speeds

        t = ValueTracker(0)

        # dot
        dot = always_redraw(lambda: Dot(
            axes.c2p(a * np.cos(omega * t.get_value()),
                     b * np.sin(omega * t.get_value())),
            color=YELLOW
        ))

        path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_opacity=0.5)
        
        self.add(dot, path)
        self.play(
            t.animate.set_value(2 * np.pi), 
            run_time=4,
            rate_func=linear
        )
        self.wait(1)


class OffCenterCircle(Scene):
    """
    Animation of a dot tracing out
    a circular path not centered at the origin
    """

    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
        self.add(axes)

        r = 1
        h = 1
        k = 0.5
        omega = 1 # angular speeds

        t = ValueTracker(0)

        # dot
        dot = always_redraw(lambda: Dot(
            axes.c2p(h + r * np.cos(omega * t.get_value()),
                     k + r * np.sin(omega * t.get_value())),
            color=YELLOW
        ))

        center = Dot(axes.c2p(h, k),
            color=GRAY
        )
        self.add(center)

        path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_opacity=0.5)
        
        self.add(dot, path)
        self.play(
            t.animate.set_value(2 * np.pi), 
            run_time=4,
            rate_func=linear
        )
        self.wait(1)
        