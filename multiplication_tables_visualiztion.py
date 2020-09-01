from manimlib.imports import *
import numpy as np


class Cardioid(Scene):
    def construct(self):
        self.intro_problem()
        self.generate_cardioid()
        self.logo()

    def intro_problem(self):
        intro = TextMobject('Visualizing Multiplication Table')
        self.play(Write(intro))
        self.play(FadeOut(intro, run_time=2))

    def generate_cardioid(self):
        label = VGroup(TextMobject("2's Table"), TextMobject("3's Table"), TextMobject("4's Table"),
                       TextMobject("5's Table"), TextMobject("6's Table"), TextMobject("7's Table"),
                       TextMobject("8's Table"), TextMobject("9's Table"), TextMobject("10's Table"))
        RADIUS = 3
        circle = Circle(radius=RADIUS, color=WHITE)
        POINTS = 150
        PERIMETER = 2 * RADIUS * PI / POINTS
        alpha= 2*np.arcsin(PERIMETER/(2*RADIUS))
        dot = VGroup()
        for i in range(POINTS):
            dot.add(Dot(np.array((RADIUS * np.cos(i*alpha), RADIUS * np.sin(i*alpha), 0)), radius=0.04, color=GOLD))
        self.play(Write(circle))
        self.play(Write(dot))
        tables = []
        seed = 2
        step = 1
        for i in range(2,11):
            tables.append([(i*seed)%POINTS for i in range(150)])
            seed += step
        line = VGroup()
        for i, table in enumerate(tables):
            for x,y in enumerate(table):
                line.add(Line(dot[x],dot[y])).set_stroke(width=0.5)
            self.play(Write(label[i].set_color(WHITE)))
            self.wait()
            self.play(label[i].to_edge, UP)
            self.play(Write(line))
            self.play(FadeOut(VGroup(line,label[i]), run_time=3))
            line = VGroup()
        self.play(FadeOut(VGroup(circle, dot), run_time=3))

    def logo(self):
        text = TextMobject("Thoughtful Coding").scale(1.5).move_to(DOWN*2.7)
        forall = TexMobject('\\forall').set_color(GOLD)
        forall.set_height(4)
        circle = Circle(radius=2.34).set_stroke(BLUE, 20)
        circle.move_to(np.array((0., 0.25, 0.)))
        forall.add(circle)
        self.play(
            Write(forall, run_time=3),
            Write(text, run_time=2.3)
        )
