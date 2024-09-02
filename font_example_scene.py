from manim import *

class TextDemo(Scene):
    def construct(self):
        text = Text("Never gonna give you up")
        text.set_color(RED)
        text2 = Text("Never gonna let you down")
        text2.set_color(BLUE)

        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE, width=4)

        square = Square()
        square.set_fill(RED, opacity=0.5)
        square.set_stroke(RED, width=4)
        
        self.play(Write(text))
        self.play(Unwrite(text))
        self.remove(text)
        self.play(Write(text2))
        self.play(Transform(text2, circle))
        self.remove(text2)
        self.play(Uncreate(circle))
        self.play(Create(square)) 