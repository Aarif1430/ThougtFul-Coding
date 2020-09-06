from manimlib.imports import *
import numpy as np
from random import uniform


class PI_Approximation(Scene):
    def construct(self):
        self.intro_problem()
        self.add_counter()
        self.draw_circle_inside_rect()

    def intro_problem(self):
        intro = TextMobject('Approximate PI using monte-carlo simulation')
        self.play(Write(intro))
        self.play(FadeOut(intro, run_time=2))

    def add_counter(self):
        self.n_clacks = 0
        counter_label = TextMobject("\\# PI: ")
        counter_mob = DecimalNumber(self.n_clacks)
        counter_mob.next_to(
            counter_label[-1], RIGHT,
        )
        counter_mob.align_to(counter_label[-1][-1], DOWN)
        counter_group = VGroup(
            counter_label,
            counter_mob,
        )
        counter_group.to_corner(UR)
        counter_group.shift(LEFT)
        self.add(counter_group)
        self.counter_mob = counter_mob

    def draw_circle_inside_rect(self):
        RADIUS = 2
        circle = Circle(radius=RADIUS, color=BLUE)
        rect = Square(side_length=2*RADIUS, color = WHITE)
        points_inside_circle = 0
        total = 0
        self.play(Write(circle), Write(rect))
        for i in range(5000):
            x = uniform(-RADIUS, RADIUS)
            y = uniform(-RADIUS, RADIUS)
            dis = x * x + y * y
            total += 1
            if dis < RADIUS * RADIUS:
                self.play(Write(Dot(np.array((x, y, 0)), radius=0.02, color=GOLD), run_time=10e-10))
                points_inside_circle += 1
            else:
                self.play(Write(Dot(np.array((x, y, 0)), radius=0.02, color=RED), run_time=10e-10))
            self.counter_mob.set_value(4 * (points_inside_circle / total))