from manim import *
from manim.mobject import graph

class Graphings(Scene):
    def construct(self):

        # Define the graph function
        graph_func = lambda x, y: ((1 ** 2) * (y ** 2) - ((x ** 2) * ((1 * 4) - x ** 2)))

        # Create the graph object
        graph = ImplicitFunction(
            graph_func,
            color=YELLOW
        )

        

        question_text = Text("Trace the Curve :a^2*y^2 = x^2*(a^2-x^2)",color=YELLOW).scale(0.6)
        self.play(Write(question_text))
        self.play(question_text.animate.shift(UP*3+LEFT*3))
        self.wait(1)

        plane = Axes(
            x_length=16,
            y_length=8
        )  



         # Create dashed lines
        dashed_line = DashedLine(start=[1.5, 3, 0], end=[-1.5, -3, 0])#for the 1st quadrant to the 3rd
        dashed_line1 = DashedLine(start=[-1.5, 3, 0], end=[1.5, -3, 0])#for the 2 quadrant to the 4th
        dashed_line3 = DashedLine(start=[1.99, 4, 0], end=[1.99, -4, 0])#for the line x=2
        dashed_line4 = DashedLine(start=[-1.99, 4, 0], end=[-1.99, -4, 0])#for the linex=-2


          # Group all objects together
        group = VGroup(plane, graph, dashed_line, dashed_line1, dashed_line3, dashed_line4)
        group.shift(RIGHT * 4).scale(0.45) # Change the value to adjust the amount of shift
        self.play(Create(plane))

        symmetry_text = Text("Symmetry :- ",color=PURPLE).scale(0.5).to_edge(LEFT * 2)
        text = Text("1) Symmetric about x axis").scale(0.5).next_to(symmetry_text, DOWN)
        text2 = Text("2) Symmetric about y axis").scale(0.5).next_to(text, DOWN)
        self.play(Write(symmetry_text))
        self.wait(0.3)
        self.play(Write(text))
        self.wait(0.3)
        self.play(Write(text2))
        self.wait(1)
        self.play(Unwrite(symmetry_text))
        self.play(Unwrite(text))
        self.play(Unwrite(text2))

        poi_text = Text("Point of Intersection as follows:",color=PURPLE).scale(0.5).to_edge(LEFT * 2)
        intercept = Text("x = 0 implies y=0 ").scale(0.5).next_to(poi_text, DOWN)
        intercept1 = Text("and y = 0 implies x = +a,-a").scale(0.5).next_to(intercept, DOWN)
        origin = Text("Therefore, Passing through origin").scale(0.5).next_to(intercept1, DOWN)
        self.play(Write(poi_text))
        self.wait(0.3)
        self.play(Write(intercept))
        self.wait(0.3)
        self.play(Write(intercept1))
        self.wait(0.3)        
        self.play(Write(origin))
        self.wait(1)

        self.play(Unwrite(poi_text))
        self.wait(0.3)
        self.play(Unwrite(intercept))
        self.wait(0.3)
        self.play(Unwrite(intercept1))
        self.wait(0.3)        
        self.play(Unwrite(origin))
        self.wait(1)

        tangent = Text("Tangent : ",color=PURPLE).scale(0.5).to_edge(LEFT * 3)
        lowest = Text("After solving Tangents:x=y").scale(0.5).next_to(tangent, DR)
        equ = Text("x=-y").scale(0.5).next_to(lowest, DOWN)
        equ2 = Text("x=a and x=-a").scale(0.5).next_to(equ, DOWN)
        equ3 = Text("Two real and coincident tangents").scale(0.5).next_to(equ2, DOWN)
        final_equ = Text("(0,0) is a cusp").scale(0.5).next_to(equ3, DOWN)
        self.play(Write(tangent))
        self.wait(0.2)
        self.play(Write(lowest))
        self.wait(0.2)
        self.play(Write(equ))
        self.wait(0.2)
        self.play(Write(equ2))
        self.wait(0.2)
        self.play(Write(equ3))
        self.wait(0.2)
        self.play(Write(final_equ))
        self.wait(1)
        self.play(Create(dashed_line, run_time=4))
        self.play(Create(dashed_line1, run_time=4))
        self.play(Create(dashed_line3, run_time=4))
        self.play(Create(dashed_line4, run_time=4))
        self.play(Unwrite(tangent))
        self.wait(0.2)
        self.play(Unwrite(lowest))
        self.wait(0.2)
        self.play(Unwrite(equ))
        self.wait(0.2)
        self.play(Unwrite(equ2))
        self.wait(0.2)
        self.play(Unwrite(equ3))
        self.wait(0.2)
        self.play(Unwrite(final_equ))
        self.wait(1)
        


        asymptote = Text("Asymptote :",color=PURPLE).scale(0.5).to_edge(LEFT * 3)
        asym_xaxis = Text("After solving : No Asymptote present").scale(0.5).next_to(asymptote, DOWN)
       
        self.play(Write(asymptote))
        self.wait(0.1)
        self.play(Write(asym_xaxis))
        self.wait(0.1)

        self.play(Unwrite(asymptote))
        self.play(Unwrite(asym_xaxis))
        


        region = Text("Region of Absence : ",color=PURPLE).scale(0.5).to_edge(LEFT * 3)
        curve_exists = Text("When x>a and x<-a curve does not exists").scale(0.5).next_to(region, DOWN)
        presence = Text("The curve exists in region -a<x<a").scale(0.5).next_to(curve_exists, DOWN)
        
        self.play(Write(region))
        self.play(Write(curve_exists))
        self.play(Write(presence))

        self.play(Unwrite(region))
        self.play(Unwrite(curve_exists))
        self.play(Unwrite(presence))
       
        
       
        curve_draw=Text("We can draw the curve now",color=PURPLE).scale(0.5).shift(LEFT*3)
        self.play(Write(curve_draw))
        self.play(Create(graph, run_time=4))       
      
        #it would be diffiicult to shift the one one line
        # Shift the group to the right

        # Play the animations
        #self.play(DrawBorderThenFill(question_text,run_time=2))
        
        #
        #
        #
        self.wait(4)
