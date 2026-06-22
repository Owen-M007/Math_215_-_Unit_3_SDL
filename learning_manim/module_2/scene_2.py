from manim import *
import numpy as np

class Limacons(Scene):
    """
    draws three limacons to show convex,
    cardioid, and inner loop variations
    k = b/a
    """

    def construct(self):
        configs = [
            {"a": 1.5, "b": 0.5, "label": r"k<1\\convex", "color": BLUE},
            {"a": 1.0, "b": 1.0, "label": r"k=1\\cardioid", "color": GREEN},
            {"a": 0.8, "b": 1.2, "label": r"k>1\\inner loop", "color": RED}
        ]

        offsets = [-3, 0, 3]

        for cfg, x_offset in zip(configs, offsets):
            a, b = cfg["a"], cfg["b"]
            scale = 1

            curve = ParametricFunction(
                lambda t, a=a, b=b: np.array([
                    scale*(a + b*np.cos(t))*np.cos(t), # x
                    scale*(a + b*np.cos(t))*np.sin(t), # y
                    0
                ]),
                t_range = [0, 2*np.pi, 0.02],
                color = cfg["color"],
                stroke_width = 2
            ).shift(RIGHT * x_offset)

            label = MathTex(cfg["label"]).next_to(curve, DOWN)

            self.add(curve, label)
        
        self.play(
            *[FadeIn(mob) for mob in self.mobjects]
        )
        self.wait(5)