#manim -ql scene.py TriangleArea
from array import array
from manim import *
def createScaleShift(self, object, direction, factor : int):
    self.play(Create(object))
    self.play(object.animate().scale(2))
    self.play(object.animate().shift(direction * factor))
#poly = Polygram([ORIGIN, RIGHT, UP])
class TriangleArea(Scene):
    def construct(self): 
        #create triangle
        triangle = Triangle()
        self.play(Create(triangle))
        self.play(triangle.animate.scale(2).shift(UP))
        triangle_vertices = triangle.get_vertices()
        #create text
        intro = Text("Area of a triangle", font_size=40)
        intro.move_to([0,-1,0])
        self.play(AddTextLetterByLetter(intro))
        #create base and height line
        lbase = Line(triangle_vertices[1],triangle_vertices[2]).set_color(YELLOW)
        lheight = Line(triangle_vertices[0],(triangle_vertices[1] + triangle_vertices[2]) / 2).set_color(RED)
        self.play(Create(lbase), Create(lheight))
        #transform into base, height
        formulaPlane  = DOWN * 2
        self.add(lbase.copy(), lheight.copy())
        ShrinkToCenter(lbase), ShrinkToCenter(lheight)
        self.play(Transform(lbase, Text("base", font_size=30).set_color(YELLOW).move_to(formulaPlane + [-1,0,0])),
        Transform(lheight, Text("height", font_size=30).set_color(RED).move_to(formulaPlane + [1,0,0])))
        #add (, ), *
        leftBracket = Text("(", font_size=30).next_to(lbase, LEFT)
        rightBracket = Text(")",font_size=30).next_to(lheight, RIGHT)
        self.play(Write(leftBracket),Write(Text("*",font_size=30).move_to(formulaPlane)),Write(rightBracket))
        #add divider and 2 symbol
        ldivider = Line(leftBracket.get_center(), rightBracket.get_center()).move_to(formulaPlane + [0,-0.5,0])
        self.play(Create(ldivider), Write(Text("2",font_size=30).move_to(ldivider.get_center() + [0,-.5,0])))
#Citation
# The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.16.0) [Computer software]. https://www.manim.community/
