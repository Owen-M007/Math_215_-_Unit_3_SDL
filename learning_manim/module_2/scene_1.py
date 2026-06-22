from manim import *
import numpy as np

class RoseCurve(Scene):
    """
    Animates the drawing of a rose curve
    """

    n = 3  # change this to see a different number of petals

    def construct(self):
        axes = Axes(
            x_range=[-1.5,1.5,0.5],
            y_range=[-1.5,1.5,0.5],
            x_length=6,
            y_length=6 #,
            # axis_config={"include_numbers": False}
        )
        self.add(axes)

# title changes with n
        title = MathTex(rf"r = \cos({self.n}\theta)").to_corner(UL)
        self.add(title)

        theta_tracker = ValueTracker(0.001) # starts just above zero
        
        rose = always_redraw(lambda: ParametricFunction(
            lambda t: axes.c2p(
                np.cos(self.n * t) * np.cos(t), # x(t) = r(t)*cos(t)
                np.cos(self.n * t) * np.sin(t) # y(t) = r(t)*sin(t)
            ),
            t_range=[0, theta_tracker.get_value(),0.02], #[start, end, step]
            color=TEAL,
            stroke_width=2
        ))

        tip_dot = always_redraw(lambda: Dot(
            axes.c2p(
                np.cos(self.n * theta_tracker.get_value()) * np.cos(theta_tracker.get_value()),
                np.cos(self.n * theta_tracker.get_value()) * np.sin(theta_tracker.get_value())
            ),
            color=YELLOW,
            radius=0.08
        ))

        self.add(rose, tip_dot)

        end_angle = 2 * np.pi

        self.play(
            theta_tracker.animate.set_value(end_angle),
            run_time=8,
            rate_func=linear
        )
        self.wait(1)