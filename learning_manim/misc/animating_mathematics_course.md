# Animating Mathematics: Polar Coordinates and Coordinate Transformations Through Spirographs

**A Complete 5-Hour Self-Paced Course for Undergraduate Students**

---

## Course Overview

| | |
|---|---|
| **Audience** | Undergraduates with Calculus I & II and basic Python |
| **Duration** | 5 hours (5 × 60-minute modules) |
| **Software** | Python 3.10+, Manim CE, FFmpeg, LaTeX |
| **Goal** | Build original spirograph animations from mathematical first principles |

### Time Allocation per Module

```
Module 1 ██████████████████████████████  60 min
  ├─ Mathematical Foundations    ████████████ 15 min
  ├─ Guided Coding Walkthrough   ████████████████████ 25 min
  ├─ Active Practice             ████████████ 15 min
  └─ Reflection & Assessment     ████ 5 min

Module 2–5 follow the same 15 / 25 / 15 / 5 breakdown.
```

**Overall time pie (all 5 modules combined):**

| Segment | Minutes | % of Course |
|---|---|---|
| Mathematical Foundations | 75 | 25% |
| Guided Coding Walkthroughs | 125 | 42% |
| Active Practice | 75 | 25% |
| Reflection & Assessment | 25 | 8% |

### Course Learning Outcomes

By the end of this course you will be able to:

1. Convert fluently between polar and Cartesian coordinate systems
2. Express curves parametrically and explain why parametrization enables animation
3. Derive the equations for hypotrochoids and epitrochoids
4. Build, render, and modify mathematical animations in Manim CE
5. Articulate how coordinate transformations underlie computer graphics

### How to Use This Course

Work through each module sequentially. Whenever you see a **⏸ Pause and Predict** box, stop and write down (or mentally commit to) your prediction *before* running the code. This single habit is the highest-leverage learning technique in the course. Each module stands alone as a 60-minute session; take breaks between modules.

---

# Setup Guide

## Installing Manim CE, FFmpeg, and LaTeX

### Windows

```powershell
# 1. Install Python 3.10+ from python.org (check "Add to PATH")
# 2. Install FFmpeg via winget
winget install ffmpeg

# 3. Install MiKTeX (LaTeX) from miktex.org — use the installer, not winget
# 4. Install Manim CE
pip install manim

# 5. Verify
manim --version
```

**Common Windows issues:**
- `ffmpeg not found`: Add `C:\ffmpeg\bin` to your PATH environment variable manually.
- `LaTeX error`: Open MiKTeX Console and click **Update** to ensure all packages install on first use.
- `pip` not found: Run `python -m pip install manim` instead.

### macOS

```bash
# 1. Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install dependencies
brew install python ffmpeg
brew install --cask mactex-no-gui   # ~4 GB; use BasicTeX for a lighter install

# 3. Refresh PATH so latex is found
eval "$(/usr/libexec/path_helper)"

# 4. Install Manim CE
pip3 install manim

# 5. Verify
manim --version
```

**Common macOS issues:**
- M1/M2 Macs: use `arch -x86_64 pip3 install manim` only if the native install fails.
- `pango` errors: `brew install pango` then reinstall Manim.

### Linux (Ubuntu/Debian)

```bash
# 1. System packages
sudo apt update
sudo apt install -y python3 python3-pip ffmpeg texlive texlive-latex-extra \
     texlive-fonts-extra texlive-xetex libcairo2-dev libpango1.0-dev

# 2. Install Manim CE
pip3 install manim

# 3. Verify
manim --version
```

**Common Linux issues:**
- `cairo` not found: ensure `libcairo2-dev` is installed before `pip install`.
- Old Python (< 3.8): use `pyenv` to install a newer version.

### Quick Smoke Test

Save as `test_manim.py` and run:

```python
from manim import *

class SmokeTest(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.wait(1)
```

```bash
manim -pql test_manim.py SmokeTest
```

If a window opens showing a blue circle being drawn, your setup is complete. The flags mean:
- `-p` → preview (open the video after rendering)
- `-q` → quality: `l` = low (fast), `m` = medium, `h` = high
- Use `-ql` while learning; switch to `-qh` for final renders.

---

# Prerequisite Refresher (Appendix A)

Read this before starting Module 1 if you are rusty on any of these topics.

## Trigonometry Identities You Will Use Constantly

$$\sin^2\theta + \cos^2\theta = 1 \tag{Pythagorean identity}$$

$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$

$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1$$

$$\sin(2\theta) = 2\sin\theta\cos\theta$$

## Parametric Equations — Quick Review

A **parametric curve** uses a third variable $t$ (the *parameter*) to express $x$ and $y$ as functions:

$$x = f(t), \quad y = g(t), \quad t \in [t_0, t_f]$$

**Why parametric?** It separates *position* from *time*, making animation natural: each value of $t$ gives one frame. A circle of radius $r$ parametrically:

$$x(t) = r\cos t, \quad y(t) = r\sin t, \quad t \in [0, 2\pi]$$

Eliminating $t$ recovers $x^2 + y^2 = r^2$.

## Polar Coordinates — Quick Review

Every point $(x, y)$ in the plane has polar coordinates $(r, \theta)$ where:

$$x = r\cos\theta, \quad y = r\sin\theta$$
$$r = \sqrt{x^2+y^2}, \quad \theta = \arctan\!\left(\frac{y}{x}\right)$$

A **polar curve** $r = f(\theta)$ traces a path as $\theta$ sweeps from $0$ to some endpoint.

## Python Review: Functions and NumPy

```python
import numpy as np

# Define a parametric circle
def circle(t, r=1.0):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# Evaluate at several t values
t_values = np.linspace(0, 2*np.pi, 100)
x_vals, y_vals = circle(t_values)
```

`np.linspace(a, b, n)` returns `n` evenly-spaced values from `a` to `b` — your go-to tool for sweeping a parameter.

---

# Module 1: Parametric Circles and the Polar–Cartesian Bridge

**Estimated time:** 60 minutes | **Difficulty:** ★☆☆☆☆

---

## A. Module Title and Learning Objectives

**Title:** Parametric Circles and the Polar–Cartesian Bridge

By the end of this module, you will be able to:

1. **Convert** any point between Cartesian and polar coordinates using the standard formulas
2. **Express** a circle parametrically and identify what changing each parameter does to the animation
3. **Construct** a Manim scene that animates a point tracing a circular path
4. **Predict** how altering $r$ and the angular speed changes the resulting animation

---

## B. Mathematical Foundations (15 min)

### The Unit Circle as a Map

The most important function in this course is $(\cos t, \sin t)$. As $t$ increases from $0$ to $2\pi$, the point $(\cos t, \sin t)$ traces the unit circle exactly once, counterclockwise.

**Key insight:** $\cos t$ and $\sin t$ are *projections*. If you think of a point at angle $t$ on a wheel of radius 1, then:
- $\cos t$ is how far right the point is (horizontal projection)
- $\sin t$ is how far up the point is (vertical projection)

### Derivation: Cartesian Circle from Polar Definition

**Claim:** The polar curve $r = a$ (constant) is a circle of radius $a$ centered at the origin.

**Proof:** Starting from the polar-to-Cartesian conversion:

$$x = r\cos\theta = a\cos\theta$$
$$y = r\sin\theta = a\sin\theta$$

Square and add:

$$x^2 + y^2 = a^2\cos^2\theta + a^2\sin^2\theta = a^2(\cos^2\theta + \sin^2\theta) = a^2$$

Therefore $x^2 + y^2 = a^2$, the equation of a circle of radius $a$. $\square$

This derivation shows that Cartesian and parametric forms are equivalent descriptions of the *same* geometric object. The parametric form is better for animation because it *includes time*.

### General Parametric Circle

A circle of radius $r$, centered at $(h, k)$, traversed at angular speed $\omega$:

$$x(t) = h + r\cos(\omega t + \phi)$$
$$y(t) = k + r\sin(\omega t + \phi)$$

where $\phi$ is the **phase** (starting angle). Setting $h=k=0$, $\omega=1$, $\phi=0$ gives the unit circle.

**Visual intuition:** Imagine a clock hand of length $r$, anchored at $(h,k)$. At time $t$, the tip has traveled $\omega t$ radians from its starting angle $\phi$. The functions $\cos$ and $\sin$ decode this angle into horizontal and vertical position. Every animation in this course is, at its heart, multiple clock hands attached to each other.

---

## C. Guided Coding Walkthrough (25 min)

### Scene 1: A Point Tracing a Circle

```python
from manim import *          # import everything from Manim's public API
import numpy as np           # numerical tools (linspace, cos, sin, pi)

class TracingCircle(Scene):
    """
    Animate a dot traveling around a circle,
    leaving a traced path behind it.
    """

    def construct(self):
        # ── 1. AXES ──────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-2, 2, 0.5],   # [min, max, tick_step]
            y_range=[-2, 2, 0.5],
            x_length=6,             # screen width (Manim units)
            y_length=6,
            axis_config={"include_numbers": True},
        )
        self.add(axes)              # add to scene immediately (no animation)

        # ── 2. STATIC CIRCLE (guide) ─────────────────────────────────────────
        r = 1.5                     # radius in Manim units
        guide_circle = Circle(
            radius=r * axes.x_length / (axes.x_range[1] - axes.x_range[0]),
            # ↑ convert math radius to screen radius
            color=GRAY,
            stroke_opacity=0.4,
        )
        # Manim's Circle is centered at origin by default
        self.add(guide_circle)

        # ── 3. MOVING DOT ────────────────────────────────────────────────────
        # ValueTracker stores a single number that Manim can animate smoothly
        angle_tracker = ValueTracker(0)  # starts at angle 0

        # A dot that always sits at the current (x, y) on the circle
        dot = always_redraw(lambda: Dot(
            axes.c2p(                        # c2p = "coords to point"
                r * np.cos(angle_tracker.get_value()),
                r * np.sin(angle_tracker.get_value()),
            ),
            color=YELLOW,
            radius=0.1,
        ))

        # ── 4. RADIUS LINE ────────────────────────────────────────────────────
        radius_line = always_redraw(lambda: Line(
            start=axes.c2p(0, 0),
            end=axes.c2p(
                r * np.cos(angle_tracker.get_value()),
                r * np.sin(angle_tracker.get_value()),
            ),
            color=BLUE,
            stroke_width=2,
        ))

        # ── 5. TRACED PATH ────────────────────────────────────────────────────
        # ParametricFunction draws the curve defined by a lambda
        traced_path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=2)

        self.add(dot, radius_line, traced_path)

        # ── 6. ANIMATION ──────────────────────────────────────────────────────
        # Animate the tracker from 0 to 2π over 4 seconds
        self.play(
            angle_tracker.animate.set_value(2 * np.pi),
            run_time=4,
            rate_func=linear,   # constant angular speed (no easing)
        )
        self.wait(1)            # pause 1 second at the end
```

**Run it:**

```bash
manim -pql module1_scene1.py TracingCircle
```

**Expected output:** A grey guide circle appears on axes. A yellow dot and blue radius line appear at the 3 o'clock position (angle 0). Over 4 seconds the dot travels counterclockwise once around the circle, leaving a red traced path. After completing the circle, the scene pauses one second.

### Key Manim Concepts Introduced

| Concept | Purpose |
|---|---|
| `ValueTracker` | Stores a number Manim can smoothly animate |
| `always_redraw` | Redraws a Mobject every frame based on current tracker value |
| `TracedPath` | Records and draws the history of a point's position |
| `axes.c2p(x, y)` | Converts math coordinates to Manim screen coordinates |
| `rate_func=linear` | Constant speed (vs. default smooth easing) |

### Common Errors and Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `NameError: name 'np' is not defined` | Forgot `import numpy as np` | Add the import |
| Dot appears off-screen | Forgot `axes.c2p()` conversion | Wrap coordinates in `c2p()` |
| Circle looks squished | `x_length ≠ y_length` on axes | Set both to the same value |
| No traced path visible | Added objects in wrong order | Add `traced_path` *after* `dot` |
| `TypeError` in `always_redraw` | Lambda returns wrong type | Lambda must return a Mobject |

---

### ⏸ Pause and Predict #1

**Before modifying the code:** If you change `run_time=4` to `run_time=8` and also change `angle_tracker.animate.set_value(2 * np.pi)` to `set_value(4 * np.pi)`, what will the animation look like?

*Write your prediction, then try it.*

---

### Scene 2: Two Circles, Two Speeds

```python
class TwoCircles(Scene):
    """
    Two dots moving at different angular speeds.
    Previews Module 4's gear-on-gear idea.
    """

    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1],
                    x_length=6, y_length=6)
        self.add(axes)

        r1, r2 = 2.0, 1.0          # radii
        omega1, omega2 = 1, 3      # angular speeds (omega2 = 3x faster)

        t = ValueTracker(0)

        # Outer dot
        dot1 = always_redraw(lambda: Dot(
            axes.c2p(r1*np.cos(omega1*t.get_value()),
                     r1*np.sin(omega1*t.get_value())),
            color=YELLOW))

        # Inner dot (moves 3x faster)
        dot2 = always_redraw(lambda: Dot(
            axes.c2p(r2*np.cos(omega2*t.get_value()),
                     r2*np.sin(omega2*t.get_value())),
            color=PINK))

        path1 = TracedPath(dot1.get_center, stroke_color=YELLOW, stroke_opacity=0.5)
        path2 = TracedPath(dot2.get_center, stroke_color=PINK,   stroke_opacity=0.5)

        self.add(dot1, dot2, path1, path2)
        self.play(t.animate.set_value(2*np.pi), run_time=6, rate_func=linear)
        self.wait()
```

---

### ⏸ Pause and Predict #2

In `TwoCircles`, if you set `omega2 = 1` (same speed as `omega1`), what shape will each dot trace? What if `omega2 = -1` (same speed, opposite direction)?

---

## D. Active Practice (15 min)

### Exercise 1.1 — Ellipse (Beginner)

Modify `TracingCircle` to trace an ellipse instead of a circle. Recall that an ellipse centered at the origin with semi-axes $a$ and $b$ is parametrized by:

$$x(t) = a\cos t, \quad y(t) = b\sin t$$

Set $a = 2$, $b = 1$ and confirm visually that the result is wider than it is tall.

### Exercise 1.2 — Off-Center Circle (Intermediate)

Move the center of the circle to $(1, 0.5)$ by modifying the dot's position formula. The general formula is:

$$x(t) = h + r\cos t, \quad y(t) = k + r\sin t$$

Also draw a static `Dot` at $(1, 0.5)$ to mark the center.

### Exercise 1.3 — Angular Speed Sweep (Intermediate)

Create a scene with three dots on circles of the same radius but with angular speeds $\omega = 1, 2, 3$. Use three different colors. Animate all three simultaneously for $2\pi$ seconds and observe when each dot "laps" the slowest one.

### 🌟 Stretch Challenge (previews Module 2)

The **cardioid** is defined in polar coordinates by $r(\theta) = 1 + \cos\theta$. Convert this to parametric form:

$$x(\theta) = r(\theta)\cos\theta = (1+\cos\theta)\cos\theta$$
$$y(\theta) = r(\theta)\sin\theta = (1+\cos\theta)\sin\theta$$

Try tracing this curve with a dot and `TracedPath`. What shape do you get?

---

## E. Reflection & Assessment (5 min)

### Conceptual Check Questions

1. The formula $x = r\cos\theta$, $y = r\sin\theta$ converts polar to Cartesian. Going the other direction, what is $\theta$ in terms of $x$ and $y$? What ambiguity arises, and how does `atan2(y, x)` resolve it?

2. In `TracingCircle`, what role does `ValueTracker` play that a plain Python variable cannot? Why can't you just write `angle = 0` and increment it manually inside `construct`?

3. Why does the animation look smoother when `rate_func=linear` compared to the default `rate_func=smooth`? Which would you choose to simulate a wheel rolling at constant speed, and why?

### Written Reflection Prompt

> In the animation, the radius line sweeps through the circle like a clock hand. How does this mechanical image connect to the mathematical idea of *angle as an accumulated rotation*? Where else in mathematics have you seen "angle as a running total"?

### Self-Assessment Rubric

| Criterion | Novice | Developing | Proficient |
|---|---|---|---|
| Polar ↔ Cartesian conversion | Cannot apply formulas | Applies with reference | Applies fluently from memory |
| Parametric circle | Cannot write parametrization | Writes with help | Writes and modifies independently |
| Manim scene structure | Scene does not run | Runs with errors corrected by instructor | Runs and produces expected output |
| `always_redraw` concept | Cannot explain | Explains partially | Explains why it is needed vs. static objects |

---

---

# Module 2: Polar Curves in Motion — Rose Curves, Cardioids, Limaçons

**Estimated time:** 60 minutes | **Difficulty:** ★★☆☆☆

---

## A. Module Title and Learning Objectives

**Title:** Polar Curves in Motion — Rose Curves, Cardioids, Limaçons

By the end of this module, you will be able to:

1. **Derive** the Cartesian parametrization of any curve given in polar form $r = f(\theta)$
2. **Explain** why the number of petals in $r = \cos(n\theta)$ depends on the parity of $n$
3. **Animate** the *drawing* of a polar curve by sweeping $\theta$ from $0$ to $2\pi$
4. **Compare** three families of polar curves (roses, cardioids, limaçons) and identify their defining features

---

## B. Mathematical Foundations (15 min)

### From Polar Equation to Parametric Curve

Any polar curve $r = f(\theta)$ can be treated parametrically: let the parameter $t = \theta$ and write:

$$x(t) = f(t)\cos t, \quad y(t) = f(t)\sin t$$

The curve is now a parametric path we can trace by letting $t$ sweep.

### Rose Curves: $r = \cos(n\theta)$

**Claim:** $r = \cos(n\theta)$ produces a rose with:
- $n$ petals if $n$ is odd
- $2n$ petals if $n$ is even

**Partial derivation (for $n = 2$, the 4-petal rose):**

$r = \cos(2\theta)$. A "petal" occurs when $r > 0$ and reaches a local maximum. $\cos(2\theta) = 1$ at $\theta = 0, \pi$. The curve passes through the origin ($r=0$) at $\theta = \pi/4, 3\pi/4, 5\pi/4, 7\pi/4$, dividing the plane into four lobes. Each lobe is traced once as $\theta$ moves between consecutive zeros, giving 4 petals total. $\square$

**Visual intuition:** Each petal is generated when $r$ is positive (the point is on the same side as the angle). When $r$ is negative, the point flips to the opposite side — this is how odd-$n$ roses "fill in" the missing petals from a naïve count.

### The Cardioid: $r = 1 + \cos\theta$

A cardioid (heart-shaped curve) arises when the amplitude of the polar perturbation equals the constant term. In parametric form:

$$x(\theta) = (1+\cos\theta)\cos\theta = \cos\theta + \cos^2\theta$$
$$y(\theta) = (1+\cos\theta)\sin\theta = \sin\theta + \sin\theta\cos\theta$$

Using $\cos^2\theta = \frac{1+\cos 2\theta}{2}$ and $\sin\theta\cos\theta = \frac{\sin 2\theta}{2}$:

$$x(\theta) = \cos\theta + \tfrac{1}{2} + \tfrac{1}{2}\cos 2\theta$$
$$y(\theta) = \sin\theta + \tfrac{1}{2}\sin 2\theta$$

This shows that a cardioid is *literally* the sum of a circle and a second harmonic — a preview of Module 4's gear-on-gear construction.

### Limaçons: $r = a + b\cos\theta$

The **limaçon** family generalizes the cardioid. The ratio $k = b/a$ determines the shape:

| $k$ | Shape |
|---|---|
| $k < 1$ | Convex limaçon (no inner loop) |
| $k = 1$ | Cardioid |
| $k > 1$ | Inner-loop limaçon |
| $k \to \infty$ | Approaches a circle |

---

## C. Guided Coding Walkthrough (25 min)

### Scene 3: Animating a Rose Curve

```python
from manim import *
import numpy as np

class RoseCurve(Scene):
    """
    Draw a rose curve r = cos(n*theta), animating the sweep of theta.
    Change N to see different petal counts.
    """

    N = 3   # ← try 2, 3, 4, 5 and observe petal counts

    def construct(self):
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6, y_length=6,
            axis_config={"include_numbers": False},
        )
        self.add(axes)

        # Title (updates with N so you know which run you're watching)
        title = MathTex(rf"r = \cos({self.N}\theta)").to_corner(UL)
        self.add(title)

        # ── Parametric curve ────────────────────────────────────────────────
        # We animate by sweeping theta_end from 0 to 2pi
        theta_tracker = ValueTracker(0.001)  # start just above 0

        # The rose curve as a ParametricFunction
        # t_range determines how much of the curve is shown
        rose = always_redraw(lambda: ParametricFunction(
            lambda t: axes.c2p(
                np.cos(self.N * t) * np.cos(t),   # x(t) = r(t)*cos(t)
                np.cos(self.N * t) * np.sin(t),   # y(t) = r(t)*sin(t)
            ),
            t_range=[0, theta_tracker.get_value(), 0.02],
            # ↑ [start, end, step] — step controls smoothness
            color=TEAL,
            stroke_width=2,
        ))

        # A dot at the current endpoint
        tip_dot = always_redraw(lambda: Dot(
            axes.c2p(
                np.cos(self.N * theta_tracker.get_value())
                  * np.cos(theta_tracker.get_value()),
                np.cos(self.N * theta_tracker.get_value())
                  * np.sin(theta_tracker.get_value()),
            ),
            color=YELLOW,
            radius=0.08,
        ))

        self.add(rose, tip_dot)

        # Sweep theta from ~0 to 2*pi (full rose for odd N; use 4*pi for even N)
        end_angle = 2 * np.pi if self.N % 2 == 1 else 4 * np.pi
        # ↑ Even-n roses need a full 4π sweep to trace all petals

        self.play(
            theta_tracker.animate.set_value(end_angle),
            run_time=8,
            rate_func=linear,
        )
        self.wait(1)
```

**Expected output (N=3):** A three-petaled rose drawn in teal, with a yellow dot at the leading edge. The sweep takes 8 seconds. Petals grow one at a time as $\theta$ increases.

### ⏸ Pause and Predict #3

Before running with `N=4`: how many petals will appear? Will $\theta$ running to $2\pi$ be enough to complete the rose, or will some petals be missing? *Check your prediction against the comment in the code above.*

### Scene 4: Limaçon Gallery

```python
class LimaconGallery(Scene):
    """
    Show three limaçons side-by-side to illustrate how the ratio k = b/a
    changes the shape from convex → cardioid → inner-loop.
    """

    def construct(self):
        configs = [
            {"a": 1.5, "b": 0.5, "label": r"k<1\ \text{(convex)}", "color": BLUE},
            {"a": 1.0, "b": 1.0, "label": r"k=1\ \text{(cardioid)}", "color": GREEN},
            {"a": 0.8, "b": 1.2, "label": r"k>1\ \text{(inner loop)}", "color": RED},
        ]

        # Three mini-axes laid out horizontally
        offsets = [-4.5, 0, 4.5]

        for cfg, x_offset in zip(configs, offsets):
            a, b = cfg["a"], cfg["b"]
            scale = 1.5  # pixels per unit

            # Draw the limaçon as a ParametricFunction
            curve = ParametricFunction(
                lambda t, a=a, b=b: np.array([
                    scale * (a + b*np.cos(t)) * np.cos(t),   # x
                    scale * (a + b*np.cos(t)) * np.sin(t),   # y
                    0,
                ]),
                t_range=[0, 2*np.pi, 0.02],
                color=cfg["color"],
                stroke_width=2,
            ).shift(RIGHT * x_offset)

            label = MathTex(cfg["label"]).next_to(curve, DOWN)

            self.add(curve, label)

        self.play(
            *[FadeIn(mob) for mob in self.mobjects]
        )
        self.wait(3)
```

> **Note on `lambda` default arguments:** The pattern `lambda t, a=a, b=b: ...` "captures" the current values of `a` and `b`. Without the defaults, Python's late binding would make all three lambdas use the *last* iteration's values — a classic Python gotcha.

---

### ⏸ Pause and Predict #4

If you replace `np.cos(t)` with `np.sin(t)` in the limaçon formula (i.e., $r = a + b\sin\theta$ instead of $a + b\cos\theta$), how will the orientation of the curve change? Think about what $\theta = 0$ means for each formula.

---

## D. Active Practice (15 min)

### Exercise 2.1 — Rose Petal Counter (Beginner)

Run `RoseCurve` for $N = 1, 2, 3, 4, 5, 6$. Fill in this table from your observations:

| N | Petals | Sweep needed |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

Does the pattern match the mathematical rule stated in the foundations section?

### Exercise 2.2 — Colored Petals (Intermediate)

Modify `RoseCurve` so each petal is a different color. *Hint:* Trace the curve in $N$ separate `ParametricFunction` calls, each covering one petal's $\theta$ range.

### Exercise 2.3 — Animated Limaçon (Intermediate)

Take one of the limaçons from `LimaconGallery` and animate its drawing (like the rose curve). Use a `ValueTracker` and `always_redraw`.

### 🌟 Stretch Challenge (previews Module 3)

A **lemniscate** is given by $r^2 = \cos(2\theta)$, so $r = \sqrt{\cos(2\theta)}$ (taking the positive root). This is only defined where $\cos(2\theta) \geq 0$.

- Where is $\cos(2\theta) \geq 0$ on $[0, 2\pi]$?
- Plot only those arcs.
- How would you use `np.where` or `np.clip` to handle the domain restriction in code?

---

## E. Reflection & Assessment (5 min)

### Conceptual Check Questions

1. Explain in one sentence why $r = \cos(n\theta)$ with $n$ even requires sweeping $\theta$ from $0$ to $4\pi$ to complete all petals, while $n$ odd only needs $0$ to $2\pi$.

2. The cardioid $r = 1 + \cos\theta$ can be thought of as the locus of a point on a circle rolling around another circle of the same radius. How does the structure of the formula $r = 1 + \cos\theta$ hint at this "two circles" interpretation?

3. In the code, `always_redraw` re-creates the entire `ParametricFunction` object every animation frame. Is this computationally efficient? What alternative approach could you use for very complex curves?

### Written Reflection Prompt

> The rose curve changes dramatically with the single integer $N$. What does this tell you about the relationship between a formula's *algebraic structure* and its *geometric shape*? Can you think of another area of mathematics where a single parameter causes qualitative (not just quantitative) change?

### Self-Assessment Rubric

| Criterion | Novice | Developing | Proficient |
|---|---|---|---|
| Polar → parametric conversion | Cannot perform | Performs with formula sheet | Performs fluently |
| Rose petal count rule | Cannot state | States but cannot explain | States and explains via r-zero crossings |
| `ParametricFunction` in Manim | Cannot write | Writes with examples | Writes and debugs independently |
| Domain restriction handling | Unaware | Knows issue, unsure how to fix | Uses `np.where` or splitting t_range |

---

---

# Module 3: Coordinate Transformations — Translation, Rotation, Scaling

**Estimated time:** 60 minutes | **Difficulty:** ★★★☆☆

---

## A. Module Title and Learning Objectives

**Title:** Coordinate Transformations — Translation, Rotation, Scaling

By the end of this module, you will be able to:

1. **Apply** the matrix form of 2D rotation, scaling, and translation to a set of points
2. **Compose** two transformations and explain why order matters (non-commutativity)
3. **Implement** animated transformations in Manim using `.animate` and `ApplyMatrix`
4. **Relate** coordinate transformations to how computer graphics engines reposition objects

---

## B. Mathematical Foundations (15 min)

### Translation

Moving every point $(x, y)$ by a displacement $(d_x, d_y)$:

$$T(x, y) = (x + d_x,\ y + d_y)$$

Translation **cannot** be expressed as a $2\times 2$ matrix multiplication. This is why graphics systems use **homogeneous coordinates** — representing a 2D point as the 3-vector $[x\ y\ 1]^T$:

$$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}1 & 0 & d_x\\ 0 & 1 & d_y\\ 0 & 0 & 1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}$$

### Scaling

Scaling by factors $s_x$ (horizontal) and $s_y$ (vertical) about the origin:

$$S = \begin{bmatrix}s_x & 0\\ 0 & s_y\end{bmatrix}, \quad S\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}s_x x\\ s_y y\end{bmatrix}$$

**Uniform scaling** ($s_x = s_y = s$) preserves shape (similarity); **non-uniform scaling** distorts it.

### Rotation

**Derivation:** Rotate the point $(r\cos\phi, r\sin\phi)$ by angle $\theta$. The new angle is $\phi + \theta$:

$$x' = r\cos(\phi+\theta) = r\cos\phi\cos\theta - r\sin\phi\sin\theta = x\cos\theta - y\sin\theta$$
$$y' = r\sin(\phi+\theta) = r\cos\phi\sin\theta + r\sin\phi\cos\theta = x\sin\theta + y\cos\theta$$

In matrix form:

$$R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$$

**Verification:** $\det(R) = \cos^2\theta + \sin^2\theta = 1$. Rotation preserves area (determinant = 1) and is invertible ($R^{-1} = R(-\theta) = R^T$).

### Composition and Non-Commutativity

**Claim:** In general, $R(\theta) \cdot S \neq S \cdot R(\theta)$.

**Counterexample:** Let $S = \begin{bmatrix}2 & 0\\ 0 & 1\end{bmatrix}$ (double width) and $R = R(90°) = \begin{bmatrix}0&-1\\1&0\end{bmatrix}$.

$$R \cdot S = \begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}2&0\\0&1\end{bmatrix} = \begin{bmatrix}0&-1\\2&0\end{bmatrix}$$

$$S \cdot R = \begin{bmatrix}2&0\\0&1\end{bmatrix}\begin{bmatrix}0&-1\\1&0\end{bmatrix} = \begin{bmatrix}0&-2\\1&0\end{bmatrix}$$

These matrices are different, confirming non-commutativity. **In graphics:** "scale then rotate" produces a different result than "rotate then scale" when the scaling is non-uniform. $\square$

**Visual intuition:** Imagine scaling a rectangle to be wider, then rotating it 45° versus rotating it first, then stretching — the second produces a diamond stretched diagonally, while the first produces a rectangle tilted at 45°.

---

## C. Guided Coding Walkthrough (25 min)

### Scene 5: Animated Rotation Matrix

```python
from manim import *
import numpy as np

class RotationDemo(Scene):
    """
    Show a square being rotated by the 2x2 rotation matrix R(theta).
    Display the matrix entries updating in real time.
    """

    def construct(self):
        # ── 1. Create a square ─────────────────────────────────────────────
        square = Square(side_length=2, color=BLUE, fill_opacity=0.3)
        square.move_to(ORIGIN)

        # ── 2. Label the corners ───────────────────────────────────────────
        labels = VGroup(*[
            Dot(point, color=WHITE, radius=0.06)
            for point in square.get_vertices()
        ])

        # ── 3. Matrix display (updates live) ───────────────────────────────
        angle_tracker = ValueTracker(0)

        matrix_display = always_redraw(lambda: MathTex(
            rf"R(\theta) = \begin{{bmatrix}}"
            rf"{np.cos(angle_tracker.get_value()):.2f} & "
            rf"{-np.sin(angle_tracker.get_value()):.2f}\\"
            rf"{np.sin(angle_tracker.get_value()):.2f} & "
            rf"{np.cos(angle_tracker.get_value()):.2f}"
            rf"\end{{bmatrix}}"
        ).to_corner(UL).scale(0.7))

        # ── 4. Angle label ────────────────────────────────────────────────
        angle_label = always_redraw(lambda: MathTex(
            rf"\theta = {np.degrees(angle_tracker.get_value()):.1f}^\circ"
        ).to_corner(UR).scale(0.8))

        self.add(square, labels, matrix_display, angle_label)

        # ── 5. Rotate the square 360° while the matrix display updates ────
        self.play(
            # Manim's built-in Rotate animation
            Rotate(square, angle=2*np.pi, about_point=ORIGIN),
            Rotate(labels, angle=2*np.pi, about_point=ORIGIN),
            angle_tracker.animate.set_value(2*np.pi),
            run_time=6,
            rate_func=linear,
        )
        self.wait()
```

### Scene 6: Composition of Transformations

```python
class TransformComposition(Scene):
    """
    Demonstrate that Scale → Rotate ≠ Rotate → Scale
    for non-uniform scaling.
    """

    def construct(self):
        # Two identical rectangles start on opposite sides
        rect_left  = Rectangle(width=2, height=1, color=BLUE,
                                fill_opacity=0.4).shift(LEFT * 3)
        rect_right = Rectangle(width=2, height=1, color=RED,
                                fill_opacity=0.4).shift(RIGHT * 3)

        label_l = Text("Scale → Rotate", font_size=24).next_to(rect_left, DOWN)
        label_r = Text("Rotate → Scale", font_size=24).next_to(rect_right, DOWN)
        self.add(rect_left, rect_right, label_l, label_r)
        self.wait(1)

        # Non-uniform scale matrix: stretch x by 2
        scale_matrix = np.array([[2, 0], [0, 1]])

        # ── LEFT: Scale first, then rotate ────────────────────────────────
        self.play(
            ApplyMatrix(scale_matrix, rect_left),
            run_time=1.5,
        )
        self.play(
            Rotate(rect_left, PI/4, about_point=rect_left.get_center()),
            run_time=1.5,
        )

        # ── RIGHT: Rotate first, then scale ───────────────────────────────
        self.play(
            Rotate(rect_right, PI/4, about_point=rect_right.get_center()),
            run_time=1.5,
        )
        self.play(
            ApplyMatrix(scale_matrix, rect_right),
            run_time=1.5,
        )

        self.wait(2)
```

**Expected output:** Two rectangles. The blue one (left) becomes wide, then tilts 45° — a wide diamond. The red one (right) tilts first, then is stretched *horizontally in screen space*, producing a parallelogram-like shape. The two results are visually different.

---

### ⏸ Pause and Predict #5

For `TransformComposition`: what would happen if `scale_matrix` were *uniform* — say, `[[2, 0], [0, 2]]`? Would the left and right results still differ? Reason through it with the commutativity of scalar multiplication.

---

### Scene 7: Rotating a Polar Curve

```python
class RotatingPolarCurve(Scene):
    """
    Apply a time-varying rotation matrix to a rose curve.
    This is the core operation used by spirograph mechanisms.
    """

    def construct(self):
        N = 3   # rose petals
        theta_rot = ValueTracker(0)  # global rotation angle

        axes = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5],
                    x_length=6, y_length=6)
        self.add(axes)

        def rose_point(t, rot):
            """Compute a rose curve point, then rotate it by 'rot' radians."""
            r = np.cos(N * t)
            x = r * np.cos(t)
            y = r * np.sin(t)
            # Apply 2D rotation matrix
            x_rot = x * np.cos(rot) - y * np.sin(rot)
            y_rot = x * np.sin(rot) + y * np.cos(rot)
            return axes.c2p(x_rot, y_rot)

        rose = always_redraw(lambda: ParametricFunction(
            lambda t: rose_point(t, theta_rot.get_value()),
            t_range=[0, 2*np.pi, 0.02],
            color=TEAL,
            stroke_width=2,
        ))

        self.add(rose)

        # Spin the rose 360°
        self.play(
            theta_rot.animate.set_value(2 * np.pi),
            run_time=6,
            rate_func=linear,
        )
        self.wait()
```

**Common errors:**

| Error | Fix |
|---|---|
| `ApplyMatrix` flattens 3D object | Manim objects live in 3D; use `np.array([[s,0,0],[0,s,0],[0,0,1]])` for 3D matrix |
| `Rotate` and manual matrix give different results | `Rotate` is applied in *screen coordinates*; manual rotation is in *data coordinates* — use `axes.c2p()` carefully |

---

## D. Active Practice (15 min)

### Exercise 3.1 — Shear Transformation (Beginner)

A **shear** matrix is $\begin{bmatrix}1 & k\\ 0 & 1\end{bmatrix}$. Apply it to a square using `ApplyMatrix` with $k = 0.5$. Describe what happens to the shape.

### Exercise 3.2 — Orbit Animation (Intermediate)

Using what you know about translation and rotation, animate a small circle orbiting a large circle:
- Large circle radius: $R = 2$
- Small circle radius: $r = 0.3$
- The small circle's center moves along the large circle
- $\theta$ increases from $0$ to $4\pi$ (two full orbits)

### Exercise 3.3 — Matrix Chaining (Intermediate)

Compute by hand the matrix $M = R(45°) \cdot S(2, 1)$ (rotate then scale). Apply $M$ to a unit square using `ApplyMatrix`. Verify your hand-computed result matches the animation.

### 🌟 Stretch Challenge (previews Module 4)

The spirograph's inner gear rotates about its own center *and* its center orbits the outer gear's center. Write the position of a point on the rim of a rolling inner gear as a composition of:
1. A rotation about the inner gear's center
2. A translation to move the inner gear center onto the orbit
3. A rotation of the orbit

Use vectors, not matrices. This is exactly Module 4's derivation.

---

## E. Reflection & Assessment (5 min)

### Conceptual Check Questions

1. Why is translation *not* a linear transformation (in the sense of linear algebra)? What property of linear transformations does it fail?

2. The rotation matrix $R(\theta)$ has $\det = 1$ for all $\theta$. What does this tell you about how rotation transforms area? Contrast with a scaling matrix $S = \begin{bmatrix}2&0\\0&3\end{bmatrix}$.

3. In computer graphics, the "model matrix" transforms a 3D object from its own local coordinate system to the world coordinate system. Based on this module, what mathematical operations does the model matrix encode, and why does the order of those operations matter?

### Written Reflection Prompt

> When you apply "scale then rotate" versus "rotate then scale," you get different objects. Yet both sequences are valid mathematical operations. What does this tell you about the difference between *mathematical operations in the abstract* and *physical operations in space*? Can you think of a real-world physical analogy where order of operations matters in the same way?

### Self-Assessment Rubric

| Criterion | Novice | Developing | Proficient |
|---|---|---|---|
| 2D rotation matrix | Cannot recall | Recalls with reference | Derives from scratch using angle addition |
| Composition/non-commutativity | Cannot demonstrate | Demonstrates numerically | Explains geometrically and numerically |
| `ApplyMatrix` in Manim | Cannot use | Uses with template | Uses and troubleshoots 3D extension |
| Homogeneous coordinates | Unaware | Knows the concept | Explains why they unify translation and linear maps |

---

---

# Module 4: The Spirograph Mathematics — Hypotrochoids and Epitrochoids

**Estimated time:** 60 minutes | **Difficulty:** ★★★★☆

---

## A. Module Title and Learning Objectives

**Title:** The Spirograph Mathematics — Hypotrochoids and Epitrochoids

By the end of this module, you will be able to:

1. **Derive** the parametric equations for hypotrochoids and epitrochoids from geometric first principles
2. **Identify** the role of each parameter ($R$, $r$, $d$) in determining the shape of the curve
3. **Predict** the number of loops/petals from the ratio $R/r$
4. **Implement** a general hypotrochoid/epitrochoid function and animate it in Manim

---

## B. Mathematical Foundations (15 min)

### What Is a Spirograph?

A physical Spirograph consists of a fixed outer ring (the **annulus**) and a smaller gear that rolls around the inside or outside. A pen is placed at a fixed point on the rolling gear. The pen traces a curve as the gear rolls.

### Deriving the Hypotrochoid (inner rolling gear)

Let:
- $R$ = radius of the fixed outer circle
- $r$ = radius of the rolling inner circle
- $d$ = distance from the pen to the center of the rolling circle

**Step 1: Locate the rolling circle's center.**

The inner circle rolls *inside* the outer circle. The center of the inner circle lies on a circle of radius $R - r$:

$$\text{Center}_{\text{roll}} = \bigl((R-r)\cos\theta,\ (R-r)\sin\theta\bigr)$$

**Step 2: Find the rotation angle of the rolling circle.**

The arc length along the outer circle swept by angle $\theta$ is $R\theta$. For the inner circle to roll without slipping, it must rotate through angle $\phi$ where:

$$r\phi = R\theta \implies \phi = \frac{R\theta}{r}$$

Because the inner circle rolls *clockwise* when the orbit moves counterclockwise, the inner circle has rotated clockwise by $\phi$ relative to a fixed frame — but we subtract the orbital angle to get the rotation in the fixed frame:

$$\text{Roll angle (fixed frame)} = \frac{R-r}{r}\theta \quad \text{(clockwise)}$$

**Step 3: Locate the pen point.**

The pen is at distance $d$ from the inner circle's center, initially pointing to the right (angle 0). After the orbital angle is $\theta$:

$$\boxed{x(\theta) = (R-r)\cos\theta + d\cos\!\left(\frac{R-r}{r}\theta\right)}$$
$$\boxed{y(\theta) = (R-r)\sin\theta - d\sin\!\left(\frac{R-r}{r}\theta\right)}$$

**Closing condition:** The curve closes (returns to its starting point) when $\theta = 2\pi k$ for some integer $k$. The number of loops equals the numerator of $R/r$ in lowest terms.

### Epitrochoid (outer rolling gear)

When the small circle rolls *outside* the fixed circle, the derivation is nearly identical. The center of the rolling circle now lies at radius $R + r$:

$$\boxed{x(\theta) = (R+r)\cos\theta - d\cos\!\left(\frac{R+r}{r}\theta\right)}$$
$$\boxed{y(\theta) = (R+r)\sin\theta - d\sin\!\left(\frac{R+r}{r}\theta\right)}$$

**Special cases:**
- $d = r$: hypotrochoid → **hypocycloid** (pen on rim); epitrochoid → **epicycloid**
- $R/r = 2$, $d = r$: hypocycloid → **diameter of the outer circle** (straight line!)
- $R/r = 3$, $d = r$: **deltoid** (three-cusped hypocycloid)
- $R/r = 4$, $d = r$: **astroid** (four-cusped hypocycloid)

**Visual intuition:** The hypotrochoid formula is literally the sum of two circular motions:
1. $(R-r)\cos\theta$: the orbit of the inner gear's center, radius $R-r$
2. $d\cos\!\left(\frac{R-r}{r}\theta\right)$: the spinning of the pen around that center, radius $d$

Recall from Module 2 that the cardioid had exactly this structure. *Every spirograph is a pair of circles added together.*

---

## C. Guided Coding Walkthrough (25 min)

### Scene 8: Animated Hypotrochoid with Gear Visualization

```python
from manim import *
import numpy as np

class Hypotrochoid(Scene):
    """
    Full spirograph animation:
    - Outer fixed circle (gray)
    - Rolling inner circle (blue)
    - Radius line from inner center to pen (red)
    - Traced path (yellow)
    
    Parameters: R=5, r=3, d=2.5 → 5-petal rose-like curve
    Try: R=7, r=2, d=1  or  R=5, r=2, d=3
    """

    R = 5      # outer circle radius (math units)
    r = 3      # rolling circle radius
    d = 2.5    # pen distance from rolling center

    def construct(self):
        # ── Scale factor: math units → Manim screen units ────────────────
        scale = 0.6   # shrink everything to fit the screen

        # ── Fixed outer circle ────────────────────────────────────────────
        outer = Circle(radius=self.R * scale, color=GRAY, stroke_opacity=0.6)
        self.add(outer)

        # ── Theta tracker ─────────────────────────────────────────────────
        theta = ValueTracker(0)

        # ── Helper: current inner circle center position ───────────────────
        def inner_center():
            t = theta.get_value()
            cx = (self.R - self.r) * np.cos(t) * scale
            cy = (self.R - self.r) * np.sin(t) * scale
            return np.array([cx, cy, 0])

        # ── Helper: current pen position ──────────────────────────────────
        def pen_pos():
            t = theta.get_value()
            px = ((self.R - self.r) * np.cos(t)
                  + self.d * np.cos((self.R - self.r) / self.r * t)) * scale
            py = ((self.R - self.r) * np.sin(t)
                  - self.d * np.sin((self.R - self.r) / self.r * t)) * scale
            return np.array([px, py, 0])

        # ── Rolling inner circle ──────────────────────────────────────────
        inner_circle = always_redraw(lambda: Circle(
            radius=self.r * scale,
            color=BLUE,
            stroke_opacity=0.8,
        ).move_to(inner_center()))

        # ── Pen dot ───────────────────────────────────────────────────────
        pen = always_redraw(lambda: Dot(pen_pos(), color=YELLOW, radius=0.1))

        # ── Line from inner center to pen ─────────────────────────────────
        arm = always_redraw(lambda: Line(
            inner_center(), pen_pos(), color=RED, stroke_width=2
        ))

        # ── Center dot of inner circle ────────────────────────────────────
        inner_dot = always_redraw(lambda: Dot(
            inner_center(), color=BLUE_D, radius=0.06
        ))

        # ── Traced path of the pen ─────────────────────────────────────────
        traced = TracedPath(pen.get_center, stroke_color=YELLOW, stroke_width=2)

        self.add(inner_circle, arm, inner_dot, pen, traced)

        # ── Compute how much theta we need for a closed curve ────────────
        from math import gcd
        R_int = int(round(self.R))
        r_int = int(round(self.r))
        g = gcd(R_int, r_int)
        # Need to sweep R/gcd full rotations of the rolling circle
        # which corresponds to (R/gcd) * 2π in theta
        num_rotations = R_int // g
        end_theta = 2 * np.pi * num_rotations

        self.play(
            theta.animate.set_value(end_theta),
            run_time=12,
            rate_func=linear,
        )
        self.wait(2)
```

**Expected output (R=5, r=3, d=2.5):** A gray outer circle. A blue rolling circle moves counterclockwise inside it. A red arm extends from the rolling circle's center to a yellow dot (the pen). The pen traces a complex 5-petal yellow curve over 12 seconds.

### Scene 9: Epitrochoid

```python
class Epitrochoid(Scene):
    """
    Rolling gear OUTSIDE the fixed circle.
    R=3, r=2, d=1 → classic epitrochoid
    """

    R = 3
    r = 2
    d = 1.5

    def construct(self):
        scale = 0.5
        theta = ValueTracker(0)

        fixed = Circle(radius=self.R * scale, color=GRAY, stroke_opacity=0.5)
        self.add(fixed)

        def roll_center():
            t = theta.get_value()
            return np.array([
                (self.R + self.r) * np.cos(t) * scale,
                (self.R + self.r) * np.sin(t) * scale,
                0
            ])

        def pen_pos():
            t = theta.get_value()
            return np.array([
                ((self.R + self.r)*np.cos(t)
                 - self.d*np.cos((self.R + self.r)/self.r * t)) * scale,
                ((self.R + self.r)*np.sin(t)
                 - self.d*np.sin((self.R + self.r)/self.r * t)) * scale,
                0
            ])

        rolling = always_redraw(lambda: Circle(
            radius=self.r * scale, color=BLUE
        ).move_to(roll_center()))

        pen  = always_redraw(lambda: Dot(pen_pos(), color=ORANGE, radius=0.1))
        arm  = always_redraw(lambda: Line(roll_center(), pen_pos(),
                                          color=RED, stroke_width=2))
        path = TracedPath(pen.get_center, stroke_color=ORANGE, stroke_width=2)

        self.add(rolling, arm, pen, path)

        from math import gcd
        g = gcd(int(self.R), int(self.r))
        self.play(
            theta.animate.set_value(2*np.pi * int(self.R) // g),
            run_time=10, rate_func=linear
        )
        self.wait(2)
```

---

### ⏸ Pause and Predict #6

For `Hypotrochoid` with `R=4`, `r=1`, `d=0.5`:
- What is $\gcd(4, 1)$?
- How many full orbits are needed to close the curve?
- How many "petals" or loops do you expect?
*Write your predictions, then change the class variables and run it.*

---

### ⏸ Pause and Predict #7

If you set `d = r` in `Hypotrochoid` (pen on the rim of the rolling circle), the hypotrochoid becomes a **hypocycloid**. For `R=4`, `r=1`, `d=1`, the hypocycloid should be an **astroid**. What does an astroid look like? *Sketch it on paper before running.*

---

## D. Active Practice (15 min)

### Exercise 4.1 — Parameter Exploration (Beginner)

Run `Hypotrochoid` with the following parameter sets and describe the resulting curve in one sentence each:

| R | r | d | Description |
|---|---|---|---|
| 5 | 3 | 5 |  |
| 7 | 2 | 3 |  |
| 5 | 5 | 2 |  |
| 3 | 1 | 1 |  |

The last entry ($R/r = 3$, $d = r$) should be a **deltoid**. Verify this.

### Exercise 4.2 — Spirograph Ratio Analysis (Intermediate)

For each of the following $R/r$ ratios (in lowest terms), predict the number of loops and confirm by running the animation:

$$\frac{R}{r} \in \left\{\frac{5}{2},\ \frac{7}{3},\ \frac{8}{3},\ \frac{6}{4}=\frac{3}{2}\right\}$$

### Exercise 4.3 — Arm Length Effect (Intermediate)

Fix `R=5`, `r=3` and animate the effect of changing `d` from `0` to `3` continuously. What happens when `d = 0`? What about `d = R - r`?

### 🌟 Stretch Challenge (previews Module 5)

A **Lissajous figure** is given by:

$$x(t) = A\sin(at + \delta), \quad y(t) = B\sin(bt)$$

These are not spirograph curves, but they share the "sum of circular motions" structure. Animate a Lissajous figure and explore how the ratio $a/b$ and the phase $\delta$ affect the shape. Compare to what you know about spirograph parameters.

---

## E. Reflection & Assessment (5 min)

### Conceptual Check Questions

1. In the hypotrochoid derivation, we subtracted the spin angle to account for the rolling direction. Specifically, the roll angle in the fixed frame is $\frac{R-r}{r}\theta$ with a *negative* $y$-component. What physical property of rolling without slipping creates this sign difference?

2. The closing condition (when the curve returns to its starting point) depends on $\gcd(R, r)$. Why does the greatest common divisor appear here? What does it represent geometrically?

3. If $d > r$ in a hypotrochoid, the pen point extends beyond the rolling circle's rim. Is this physically realizable with a real Spirograph toy? What does the curve look like differently from $d < r$?

### Written Reflection Prompt

> The hypotrochoid formula shows that every spirograph curve is literally the *sum* of two circular motions. Fourier analysis says that *any* periodic function can be written as a sum of circular motions (sinusoids). Connect these ideas: in what sense is your spirograph a two-term Fourier series? What would a three-term Fourier series look like geometrically?

### Self-Assessment Rubric

| Criterion | Novice | Developing | Proficient |
|---|---|---|---|
| Hypotrochoid derivation | Cannot reproduce | Follows with prompting | Derives independently from first principles |
| Parameter roles ($R$, $r$, $d$) | Cannot distinguish | Describes each vaguely | Predicts curve shape from values |
| Loop count from $R/r$ | Cannot compute | Computes with reminders | Computes and explains via gcd |
| Manim gear animation | Scene crashes | Scene runs with rough visuals | Smooth animation with correct geometry |

---

---

# Module 5: Capstone — Build, Customize, and Present an Original Spirograph

**Estimated time:** 60 minutes | **Difficulty:** ★★★★★

---

## A. Module Title and Learning Objectives

**Title:** Capstone — Build, Customize, and Present an Original Spirograph

By the end of this module, you will be able to:

1. **Design** an original spirograph animation by selecting parameters that produce an aesthetically interesting curve
2. **Enhance** a Manim scene with color gradients, LaTeX annotations, and camera control
3. **Export** a publication-quality animation at multiple resolutions
4. **Articulate** the mathematical story of your spirograph in a 3-minute verbal explanation

---

## B. Mathematical Foundations (15 min)

### Multi-Gear Spirographs

A real Spirograph uses two gears, but nothing stops us from composing three or more circular motions:

$$x(t) = r_1\cos(\omega_1 t) + r_2\cos(\omega_2 t) + r_3\cos(\omega_3 t)$$
$$y(t) = r_1\sin(\omega_1 t) + r_2\sin(\omega_2 t) + r_3\sin(\omega_3 t)$$

This is exactly a **truncated Fourier series** in disguise. The Fourier representation theorem guarantees that any smooth closed curve can be approximated to arbitrary precision by adding more terms.

**Epicycle decomposition (historical note):** Ptolemy's geocentric model of the solar system used exactly this construction — epicycles upon epicycles — to approximate planetary orbits. The mathematical structure was correct even though the physical interpretation was wrong. Fourier later gave it the rigorous foundation.

### Coloring by Curvature or Speed

The **speed** of a parametric curve is $\|\mathbf{r}'(t)\| = \sqrt{(dx/dt)^2 + (dy/dt)^2}$. For our hypotrochoid:

$$\frac{dx}{dt} = -(R-r)\sin\theta - d\cdot\frac{R-r}{r}\sin\!\left(\frac{R-r}{r}\theta\right)$$

$$\frac{dy}{dt} = (R-r)\cos\theta - d\cdot\frac{R-r}{r}\cos\!\left(\frac{R-r}{r}\theta\right)$$

Coloring each segment by speed gives a visual "heat map" of where the pen moves fast (usually near the tips of petals, where the two circular motions reinforce) versus slowly (near cusps, where they partially cancel).

### The "Torus Knot" Connection

If you wrap a spirograph curve around a torus (donut) instead of a flat plane, you get a **torus knot**. The linking numbers are exactly $R/r$ in lowest terms. This shows that spirograph mathematics connects to topology — the study of shapes that can be continuously deformed.

---

## C. Guided Coding Walkthrough (25 min)

### Scene 10: Production-Quality Spirograph

```python
from manim import *
import numpy as np
from math import gcd

class ProductionSpirograph(Scene):
    """
    A fully-featured spirograph animation with:
    - Color gradient along the path
    - Synchronized gear animation
    - LaTeX parameter annotations
    - Smooth fade-in of the curve
    
    Capstone template: customize R, r, d, and COLORS.
    """

    # ── Your parameters ────────────────────────────────────────────────────
    R = 7          # outer circle radius
    r = 3          # rolling circle radius
    d = 4          # pen distance (try d > r for outer loops)
    COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]  # gradient palette

    def construct(self):
        scale = 0.45

        # ── Compute how far theta must sweep to close the curve ───────────
        g = gcd(self.R, self.r)
        n_loops = self.R // g          # number of full outer rotations
        end_theta = 2 * np.pi * n_loops

        # ── Background and title ─────────────────────────────────────────
        title = MathTex(
            rf"R={self.R},\; r={self.r},\; d={self.d}"
        ).to_edge(UP).set_color(WHITE)
        subtitle = MathTex(
            rf"\text{{Loops: }} {n_loops},\quad"
            rf"\frac{{R}}{{r}} = \frac{{{self.R}}}{{{self.r}}} = "
            rf"\frac{{{self.R // g}}}{{{self.r // g}}}"
        ).next_to(title, DOWN).scale(0.7)

        self.add(title, subtitle)

        # ── Static guide circles ──────────────────────────────────────────
        outer_ring = Circle(radius=self.R * scale, color=GRAY,
                            stroke_opacity=0.3, stroke_width=1)
        orbit_ring = Circle(radius=(self.R - self.r) * scale, color=DARK_GRAY,
                            stroke_opacity=0.2, stroke_width=1,
                            fill_opacity=0)
        self.add(outer_ring, orbit_ring)

        # ── ValueTracker ──────────────────────────────────────────────────
        theta = ValueTracker(0)

        # ── Position helpers ──────────────────────────────────────────────
        def roll_center():
            t = theta.get_value()
            return np.array([
                (self.R - self.r) * np.cos(t) * scale,
                (self.R - self.r) * np.sin(t) * scale, 0
            ])

        def pen_point():
            t = theta.get_value()
            return np.array([
                ((self.R - self.r)*np.cos(t)
                 + self.d*np.cos((self.R - self.r)/self.r * t)) * scale,
                ((self.R - self.r)*np.sin(t)
                 - self.d*np.sin((self.R - self.r)/self.r * t)) * scale,
                0
            ])

        # ── Gears ─────────────────────────────────────────────────────────
        rolling_gear = always_redraw(lambda: Circle(
            radius=self.r * scale, color=BLUE_D, stroke_width=1.5,
            stroke_opacity=0.6, fill_opacity=0.05
        ).move_to(roll_center()))

        gear_center_dot = always_redraw(lambda: Dot(
            roll_center(), radius=0.04, color=BLUE_C
        ))

        arm = always_redraw(lambda: Line(
            roll_center(), pen_point(),
            color=BLUE_A, stroke_width=1.5, stroke_opacity=0.8
        ))

        pen_dot = always_redraw(lambda: Dot(
            pen_point(), radius=0.1, color=YELLOW
        ))

        # ── COLOR GRADIENT traced path ────────────────────────────────────
        # We build the full curve in segments, each colored differently.
        # This gives a rainbow gradient effect.
        NUM_SEGMENTS = len(self.COLORS)
        theta_step = end_theta / NUM_SEGMENTS

        def colored_curve_up_to(current_theta):
            """
            Draw the traced path from 0 to current_theta,
            splitting it into colored segments.
            """
            curves = VGroup()
            for i, color in enumerate(self.COLORS):
                seg_start = i * theta_step
                seg_end   = min((i+1) * theta_step, current_theta)
                if seg_end <= seg_start:
                    break
                curve = ParametricFunction(
                    lambda t, scale=scale: np.array([
                        ((self.R - self.r)*np.cos(t)
                         + self.d*np.cos((self.R - self.r)/self.r * t)) * scale,
                        ((self.R - self.r)*np.sin(t)
                         - self.d*np.sin((self.R - self.r)/self.r * t)) * scale,
                        0
                    ]),
                    t_range=[seg_start, seg_end, 0.015],
                    color=color,
                    stroke_width=2,
                )
                curves.add(curve)
            return curves

        # Use always_redraw to update the gradient path every frame
        gradient_path = always_redraw(
            lambda: colored_curve_up_to(theta.get_value())
        )

        self.add(rolling_gear, gear_center_dot, arm, gradient_path, pen_dot)

        # ── Main animation ────────────────────────────────────────────────
        self.play(
            theta.animate.set_value(end_theta),
            run_time=14,
            rate_func=linear,
        )

        # ── Finale: fade out gears, keep the curve ─────────────────────────
        self.play(
            FadeOut(rolling_gear),
            FadeOut(gear_center_dot),
            FadeOut(arm),
            FadeOut(pen_dot),
            run_time=1.5,
        )

        # Flash the completed curve
        self.play(
            gradient_path.animate.set_stroke(width=3),
            run_time=0.5,
        )
        self.wait(3)
```

**Run at high quality for your final render:**

```bash
manim -pqh module5_capstone.py ProductionSpirograph
```

### Scene 11: Three-Gear Spirograph (Bonus)

```python
class ThreeGearSpirograph(Scene):
    """
    Three nested circular motions:
    x(t) = r1*cos(w1*t) + r2*cos(w2*t) + r3*cos(w3*t)
    
    Demonstrates Fourier/epicycle decomposition.
    """

    # Angular frequencies and radii
    PARAMS = [
        {"r": 2.5, "w": 1},    # first arm (orbit)
        {"r": 1.0, "w": 3},    # second arm (faster)
        {"r": 0.5, "w": 7},    # third arm (fastest)
    ]
    COLORS_ARMS = [BLUE, GREEN, RED]

    def construct(self):
        scale = 0.9
        theta = ValueTracker(0)

        def arm_endpoints(t):
            """Return the tip position of each cumulative arm."""
            positions = [np.array([0, 0, 0])]
            for p in self.PARAMS:
                prev = positions[-1]
                tip = prev + np.array([
                    p["r"] * np.cos(p["w"] * t) * scale,
                    p["r"] * np.sin(p["w"] * t) * scale,
                    0
                ])
                positions.append(tip)
            return positions

        # Arms
        arms = always_redraw(lambda: VGroup(*[
            Line(arm_endpoints(theta.get_value())[i],
                 arm_endpoints(theta.get_value())[i+1],
                 color=self.COLORS_ARMS[i], stroke_width=2)
            for i in range(len(self.PARAMS))
        ]))

        pen = always_redraw(lambda: Dot(
            arm_endpoints(theta.get_value())[-1],
            color=YELLOW, radius=0.1
        ))

        path = TracedPath(pen.get_center, stroke_color=YELLOW, stroke_width=1.5)

        self.add(arms, pen, path)

        # Run for enough time to get a good-looking curve
        self.play(
            theta.animate.set_value(6 * np.pi),
            run_time=12, rate_func=linear
        )
        self.wait(2)
```

---

### ⏸ Pause and Predict #8

In `ThreeGearSpirograph`, what happens if all three frequencies are the same (`w: 1` for all)? The result is mathematically equivalent to what simpler single-gear spirograph? Calculate the combined radius and verify.

---

### ⏸ Pause and Predict #9

If you reverse the direction of the second arm (change `"w": 3` to `"w": -3`), how do you expect the symmetry of the traced curve to change? Will it still be a closed curve?

---

## D. Active Practice (15 min)

### Exercise 5.1 — Your Signature Spirograph (Required Capstone)

Design a spirograph using `ProductionSpirograph` that you find visually beautiful. Requirements:
- The curve must close (choose $R$, $r$ such that $\gcd(R,r) \geq 1$)
- Use a custom color palette (change `COLORS`)
- Add your name as a `Text` object somewhere in the scene
- Export at `-qm` or `-qh` quality

Document your parameter choices and why you made them.

### Exercise 5.2 — Mathematical Annotation (Intermediate)

Add `always_redraw` labels to `ProductionSpirograph` that display:
- The current angle $\theta$ in degrees
- The current pen position $(x, y)$
- The fraction of the curve completed (as a percentage)

### Exercise 5.3 — Speed Coloring (Advanced)

Instead of coloring segments by a fixed gradient, color each tiny segment by the **speed** of the pen at that point:

$$\text{speed}(t) = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$$

Differentiate the hypotrochoid equations symbolically, compute speed at each $t$, and use Manim's `color_using_function_position` or manually build a `VMobject` with varying stroke color.

### 🌟 Stretch Challenge — Fourier Art

Using `ThreeGearSpirograph` as a template, try to approximate a recognizable shape (circle, star, heart) by choosing the parameters $r_i$ and $\omega_i$ to match a simple Fourier series. This is the basis of "Fourier drawing" animations popularized online.

---

## E. Reflection & Assessment (5 min)

### Conceptual Check Questions

1. Your spirograph is mathematically equivalent to a two-term (or three-term) Fourier series. The Fourier theorem says *any* periodic function can be so represented. What does "any periodic function" mean geometrically — what kinds of curves does this include?

2. You used `gcd(R, r)` to determine when the curve closes. What changes if $R/r$ is irrational? Is the curve still well-defined? Does it ever close?

3. Computer graphics engines (like OpenGL) represent every transformation as a matrix and compose them into a single "model-view-projection" matrix before rendering. Based on all five modules, what mathematical operations have you composed to produce a spirograph, and how would you express this as a single matrix product?

### Written Reflection Prompt

> At the start of this course, a "spirograph" was probably just a childhood toy. Now you can derive its equations from scratch, write code that animates it, and connect it to Fourier analysis, gear kinematics, and computer graphics. Write a 150-word response to this question: *What does it mean to "understand" a mathematical object?* Has your understanding of the spirograph deepened, or has the math replaced the intuition? Can both coexist?

### Final Self-Assessment Rubric

| Criterion | Novice | Developing | Proficient |
|---|---|---|---|
| Hypotrochoid derivation | Cannot reproduce | Reproduces with notes | Derives from scratch in < 10 min |
| Parameter prediction | Cannot predict shape | Predicts roughly | Predicts loops, symmetry, closure |
| Manim scene quality | Crashes or no output | Runs, rough visuals | Smooth, annotated, exportable |
| Color/aesthetic design | Default colors only | Modified colors | Custom gradient with intentional design |
| Mathematical storytelling | Cannot explain | Explains mechanically | Connects to Fourier, transformations, topology |
| Code documentation | No comments | Sparse comments | Every section explained for a reader |

---

---

# Appendix A: Prerequisite Refresher

*(See the beginning of this document — the refresher appears after the Setup Guide.)*

---

# Appendix B: Complete Quick-Reference Card

## Manim CE Cheat Sheet

```python
# Scene skeleton
class MyScene(Scene):
    def construct(self):
        ...  # all your code here

# Shapes
Circle(radius=1, color=BLUE, fill_opacity=0.3)
Square(side_length=2)
Line(start=LEFT, end=RIGHT, color=WHITE)
Dot(point=ORIGIN, radius=0.1, color=YELLOW)
Rectangle(width=4, height=2)

# Math
MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1")
Text("Hello", font_size=36)

# Axes and coordinates
axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
axes.c2p(x, y)                     # math → screen
axes.p2c(point)                    # screen → math

# Parametric curve
ParametricFunction(lambda t: [x(t), y(t), 0], t_range=[0, 2*np.pi, 0.02])

# Animation
ValueTracker(initial_value)        # animated number
always_redraw(lambda: Mobject)     # redraws every frame
TracedPath(dot.get_center)         # records path

# Plays
self.play(Create(obj))             # draw in
self.play(FadeIn(obj))             # fade in
self.play(Rotate(obj, PI/2))       # rotate
self.play(ApplyMatrix(matrix, obj))# matrix transform
self.play(tracker.animate.set_value(new_val), run_time=5, rate_func=linear)
self.add(obj)                      # instant (no animation)
self.wait(2)                       # pause 2 seconds

# Grouping
VGroup(obj1, obj2, obj3)           # treat as one object
```

## Key Formulas

| Curve | Formula |
|---|---|
| Parametric circle | $x = r\cos t,\ y = r\sin t$ |
| Polar to Cartesian | $x = r\cos\theta,\ y = r\sin\theta$ |
| Rose curve | $r = \cos(n\theta)$; petals: $n$ (odd) or $2n$ (even) |
| Cardioid | $r = 1 + \cos\theta$ |
| Limaçon | $r = a + b\cos\theta$ |
| Rotation matrix | $R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$ |
| Hypotrochoid | $x = (R-r)\cos\theta + d\cos\!\left(\frac{R-r}{r}\theta\right)$ |
| Epitrochoid | $x = (R+r)\cos\theta - d\cos\!\left(\frac{R+r}{r}\theta\right)$ |
| Close condition | Sweep $\theta$ through $2\pi \cdot \frac{R}{\gcd(R,r)}$ |

---

# Appendix C: Troubleshooting Guide

| Symptom | Likely Cause | Fix |
|---|---|---|
| `No module named 'manim'` | Manim not installed in current Python | `pip install manim` in the right environment |
| Black screen, no shapes | Added shapes after `self.wait()` | Call `self.add()` or `self.play()` before `self.wait()` |
| Curve looks pixelated | Low quality flag `-ql` | Use `-qm` or `-qh` |
| `LaTeX Error` mid-render | Missing LaTeX package | Run MiKTeX/TeX Live updater |
| `always_redraw` not updating | Lambda captures wrong variable | Use default arguments in lambda to force capture |
| Traced path disappears | Dot was FadedOut | Use a separate invisible dot for TracedPath anchor |
| Very slow rendering | Too many `always_redraw` redraws | Pre-compute curve; only redraw what changes |
| Curve doesn't close | Wrong sweep angle | Compute $2\pi \cdot R / \gcd(R,r)$ |
| `ValueError: t_range` | `t_step` too large | Make step $\leq 0.02$; for fast curves use $0.005$ |

---

# Appendix D: Further Reading and Resources

## Mathematics
- **Needham, T.** — *Visual Complex Analysis* (Oxford). Chapter 1 gives the best visual treatment of complex exponentials as circular motion.
- **Pressley, A.** — *Elementary Differential Geometry*. Chapter 1 covers parametric curves rigorously.
- **Maor, E.** — *Trigonometric Delights* (Princeton). Wonderful historical and conceptual treatment.

## Manim CE
- Official docs: `https://docs.manim.community`
- Theorem of Beethoven (YouTube): best Manim tutorial series for beginners
- `manim.community/plugins` for extra renderers and effects

## Spirographs and Fourier Art
- **3Blue1Brown** — "But what is a Fourier series?" (YouTube): the epicycle animation that inspired a generation
- **Harmonograph** (Wikipedia): physical pendulum analog of spirographs
- `spirographicart.com` — interactive browser-based spirograph explorer

## Computer Graphics Connection
- **Shirley, P. & Marschner, S.** — *Fundamentals of Computer Graphics*. Chapters 6–7 cover the transformation pipeline.
- **Pharr, M. et al.** — *Physically Based Rendering* (free online). Chapter 2 covers geometric transformations in full generality.

---

*End of course document. Total approximate reading + coding time: 5 hours.*

*Version 1.0 — Generated for undergraduate self-paced use.*
