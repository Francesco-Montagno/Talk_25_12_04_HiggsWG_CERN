
# source ~/envs/manim/bin/activate

"""
Command to generate the slides with manim:
manim render generating_slides.py Slide_Class_Name -pqh -s --resolution 1920,1080 
"""


from turtle import left
from manim import *
from numpy import diag
my_template = TexTemplate()
my_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
my_template.add_to_preamble(r"\usepackage[normalem]{ulem}")
my_template.add_to_preamble(r"\usepackage{xcolor}")
my_template.add_to_preamble(r"\usepackage{mathtools}")
my_template.add_to_preamble(r"\definecolor{IFAE_Color}{RGB}{0,84,61}")  # esempio

IFAE_Color = ManimColor([0., 0.32941177, 0.23921569])

class BaseSlide(Scene):
    def setup_background(self):
        self.camera.background_color = WHITE
        
        top_bar = Rectangle(
            width=config.frame_width,
            height=0.8,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(config.frame_height / 2 - 0.2)

        bottom_bar = Rectangle(
            width=config.frame_width,
            height=1.0,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(-config.frame_height / 2)
        
        self.add(top_bar, bottom_bar)

        logo = ImageMobject("assets/IFAE_logo_SO.png").scale(0.15)
        logo.to_corner(UL, buff=0.7)
        self.add(logo)

class Slide_Title(BaseSlide):
    def construct(self):
        self.setup_background()

        # Titolo
        title = Tex(r"\textbf{EFT Theory Uncertainties at the LHC}", color=BLACK, font_size=48, tex_template=my_template,)
        
        # Presentatore e collaboratori
        presenter = Tex(r"{Presented by F. Montagno}", color=BLACK, font_size=32)
        collaborators = Tex(r"In collaboration with S. Chang, M. Luty, T. Ma and A. Wulzer.", color=BLACK, font_size=28)

        # Raggruppa centro
        central_block = VGroup(title, presenter, collaborators).arrange(DOWN, buff=0.7)
        central_block.move_to(ORIGIN)
        self.play(LaggedStartMap(Write, central_block, lag_ratio=0.2))
        self.wait(0.3)

        event = Tex(
            r"LHC Higgs WG Workshop, 04/12/2025",
            color=BLACK,
            font_size=24
        )
        event.to_corner(DR, buff=0.6)
        self.play(FadeIn(event))
        
        event = Tex(
            r"arXiv:2507.15954",
            color=BLACK,
            font_size=24
        )
        event.to_corner(DL, buff=0.6)
        self.play(FadeIn(event))
        
        self.wait(1)

class Slide_Why_EFT(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{EFTs and their validity}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        bullet = Tex(
            r"• EFT is a low-energy parametrization of UV models.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.5)

        self.add(bullet)
        
        bullet2 = Tex(
            r"Useful for model-independent searches.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(LEFT * .7)
        self.add(bullet2)

        # Single bullet
        bullet = Tex(
            r"• Precision measurements →",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=4)

        self.add(bullet)
        
        bullet2 = Tex(
            r"Constraints on Wilson coefficients.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(RIGHT * .7)
        self.add(bullet2)

        # Single bullet
        bullet = Tex(
            r"• Under which conditions is the EFT reliable?",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=5.5)

        self.add(bullet)

        # --- Right column image ---
        diagram = ImageMobject("assets/Higgs-Markus.png").scale(0.6).to_edge(RIGHT, buff=0.2).to_edge(DOWN, buff=1.5)
        caption = Tex(
            r"Abu-Ajamieh, Chang, Chen, Luty (2020)",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)
        # Add to scene

class Slide_EFT_Problem(BaseSlide):
    def construct(self):
        self.setup_background()
        # Title
        title = Tex(
            r"\textbf{The Problem: EFT Validity}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        bullet = Tex(
            r"• An EFT describes the effect of heavy particles",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(RIGHT, buff=1.5).to_edge(UP, buff=2.5)

        self.add(bullet)
        
        bullet2 = Tex(
            r" with mass $M$ in an expansion in $E/M$",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(RIGHT * (-0.4))
        self.add(bullet2)

        # Single bullet
        bullet = Tex(
            
            r"• At $E \gtrsim M$ the EFT breaks down",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(RIGHT, buff=3.27).to_edge(UP, buff=4)

        self.add(bullet)
        
        # bullet2 = Tex(
        #     r"For → EFT loses predictivity, may violate principles like unitarity",
        #     font_size=32,
        #     tex_template=my_template,
        #     color=BLACK
        # ).next_to(bullet, DOWN, buff=0.3).shift(RIGHT * .7)
        # self.add(bullet2)

        # Single bullet
        bullet = Tex(
            r"• Data in the high-energy regime ($E \gtrsim M$)",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(RIGHT, buff=2.08).to_edge(UP, buff=5)

        self.add(bullet)
        
        bullet2 = Tex(
            r" could give \textbf{too strong} constraints",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(RIGHT * -0.4)
        self.add(bullet2)
        # --- Right column image ---
        diagram = ImageMobject("assets/amplitude_1.png").scale(0.6).to_edge(LEFT, buff=0.8).to_edge(DOWN, buff=1.)
        self.add(diagram)

class Slide_The_Clipping_Proposal(BaseSlide):
    def construct(self):
        self.setup_background()
        # Title
        title = Tex(
            r"\textbf{The Clipping Proposal}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        bullet = Tex(
            r"• Don't use data above a cutoff $E_\text{cut} < M$",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(RIGHT, buff=2).to_edge(UP, buff=2.5)

        self.add(bullet)


        # # Single bullet
        # bullet = Tex(
        #     r"\textbf{Problems}",
        #     font_size=32,
        #     tex_template=my_template,
        #     color=ManimColor([0.5, 0.15, 0.15])
        # ).to_edge(RIGHT, buff=6.5).to_edge(UP, buff=3.8)

        # self.add(bullet)
        

        # # Single bullet
        # bullet = Tex(
        #     r"• Where to cut?",
        #     font_size=32,
        #     tex_template=my_template,
        #     color=BLACK
        # ).to_edge(RIGHT, buff=5.65).to_edge(UP, buff=4.5)

        # self.add(bullet)
        
        # bullet2 = Tex(
        #     r"• Can I reconstruct '$E$'?",
        #     font_size=32,
        #     tex_template=my_template,
        #     color=BLACK
        # ).next_to(bullet, DOWN, buff=0.5).shift(RIGHT * 0.58)
        # self.add(bullet2)
        # --- Right column image ---
        diagram = ImageMobject("assets/amplitude_1000.png").scale(0.6).to_edge(LEFT, buff=0.8).to_edge(DOWN, buff=1.)
        self.add(diagram)
        
class Slide_Our_Proposal(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Our Proposal}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)


        # Single bullet
        bullet = Tex(
            r"• Introduce parameterized uncertainties into",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.2)

        self.add(bullet)
        
        bullet2 = Tex(
            r" EFT predictions via \textbf{nuisance parameters}",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.2).shift(LEFT * -.1)
        self.add(bullet2)
        
        bullet3 = Tex(
            r" that reflect the higher order corrections.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet2, DOWN, buff=0.2).shift(LEFT * .2)
        self.add(bullet3)
        # Single bullet
        bullet = Tex(
            r"• The scale $M$ at which the EFT \textbf{breaks down}  ",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=4.1)

        self.add(bullet)
        
        bullet2 = Tex(
            r"is treated as an independent parameter.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(LEFT * .2)
        self.add(bullet2)

        # Single bullet
        bullet = Tex(
            r"• EFT uncertainty $\longleftrightarrow$ ignorance about UV",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=5.5)

        self.add(bullet)
        
        bullet2 = Tex(
            r"\textbf{Unavoidable prior assumptions}",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.3).shift(RIGHT * -.35)
        self.add(bullet2)
        
        bullet3 = Tex(
            r"about the size of allowed deviations.",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet2, DOWN, buff=0.3).shift(RIGHT * .15)
        self.add(bullet3)
        # --- Right column image ---
        diagram = ImageMobject("assets/uv_reach_with_clipping.png").scale(0.7).to_edge(RIGHT, buff=0.3).to_edge(DOWN, buff=1.)

        self.add(diagram)
        
        # Placeholder for diagram (right column)
        # diagram = ImageMobject("assets/diagram_placeholder.png").scale(0.7).to_edge(RIGHT, buff=1)
        # self.add(diagram)

class Slide_Outline(BaseSlide):
    def construct(self):
        self.setup_background()

        # Titolo principale
        title = Tex(
            r"\textbf{Outline}",
            color=BLACK,
            font_size=52,
            tex_template=my_template
        ).to_edge(UP, buff=1.2)
        self.add(title)

        # Colonna sinistra – già trattato
        color1 = BLACK # GRAY
        left = VGroup(
            Tex(r"\textbf{1.} EFTs and their validity", font_size=34, color=color1, tex_template=my_template),
            Tex(r"\textbf{2.} The Problem: EFT Validity", font_size=34, color=color1, tex_template=my_template),
            Tex(r"\textbf{3.}  The Clipping Proposal", font_size=34, color=color1, tex_template=my_template),
            Tex(r"\textbf{4.}  Our Proposal", font_size=34, color=color1, tex_template=my_template),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=3)

        color2 = BLACK
        # Colonna destra – da trattare
        right = VGroup(
            Tex(r"\textbf{5.} Low Energy Expansion", font_size=34, color=color2, tex_template=my_template),
            Tex(r"\textbf{6.} Parametrizing EFT Uncertainties", font_size=34, color=color2, tex_template=my_template),
            Tex(r"\textbf{7.} Toy Model Implementation", font_size=34, color=color2, tex_template=my_template),
            Tex(r"\textbf{8.} Comparison with UV Models", font_size=34, color=color2, tex_template=my_template),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=3)

        # Sottotitoli delle colonne
        left_title = Tex(
            r"\textbf{Motivation}",
            font_size=38,
            color=IFAE_Color,  # puoi cambiare colore a piacere
            tex_template=my_template
        ).next_to(left, UP, buff=0.5)

        right_title = Tex(
            r"\textbf{Approach}",
            font_size=38,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(right, UP, buff=0.5)
        
        left_title.shift(RIGHT * -3)
        left_title.shift(DOWN * 0.5)
        right_title.shift(LEFT * -0.1)
        right_title.shift(DOWN * 0.7)
        content = VGroup(left, right).arrange(RIGHT, buff=1.8).move_to(ORIGIN)
        content.shift(DOWN * 0.5)
        # right[0].set_opacity(0)  # 4. Parametrizing EFT Uncertainties
        # right[1].set_opacity(0)  # 5. Exclusion ...
        # right[2].set_opacity(0)  # 6. Summary and Outlook
        # right_title.set_opacity(0)
        self.add(left_title, right_title, content)

class Slide_Parametrizing_EFT_Uncertainties(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Low Energy Expansion}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagrammi
        diagram1 = ImageMobject(
            "assets/tree.png"
            ).scale(0.8).to_edge(LEFT, buff=1.5).shift(UP * 0.3)

        # Equation
        equation = MathTex(
            r"\mathcal{M}_\textrm{BSM} = g^2 \frac{1}{\hat s-M^2}",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram1, DOWN, buff=0.5)
        self.add(diagram1, equation)
        
        # Freccia tra i due diagrammi
        arrow = Arrow(
            start=diagram1.get_right() + RIGHT * 0.1,
            end=diagram1.get_right() + RIGHT * 2,
            buff=0,
            color=BLACK
        ).next_to(diagram1, RIGHT, buff=1.5).shift(DOWN *0.2)
        arrow_text = Tex(
            r"\textbf{Integrating out new physics}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(arrow, UP, buff=0.2)
        diagram2 = ImageMobject("assets/contact.png").scale(0.8).next_to(diagram1, RIGHT, buff=5)

        # Aggiungi tutto alla scena
        self.add(arrow, arrow_text, diagram2,)
        
        arrow_text_down = Tex(
            r"$\boldsymbol{\hat s \ll M^2}$",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(arrow, DOWN, buff=0.2)
        self.add(arrow_text_down,)
        # Equation
        equation2 = MathTex(
            r"\mathcal{M}_\textrm{EFT} = G\left[1 + \frac{\hat s}{M^2} +\frac{\hat s^2}{M^4} + \dots\right]",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram2, DOWN, buff=0.5)
        self.add(equation2)
        
        equation2 = MathTex(
            r"\underbrace{\phantom{\frac{\hat s}{M^2} + \frac{\hat s^2}{M^4}+ \dots} }",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram2, DOWN, buff=1.5,).shift(RIGHT*1.2)
        self.add(equation2)

        equation3 = Tex(
            r"\textbf{Mandelstam Descendants}",
            font_size=32,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.2,).shift(LEFT*0.4)
        self.add(equation3)

class Slide_Parametrizing_EFT_Uncertainties_2(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Low Energy Expansion}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagrammi
        diagram1 = ImageMobject(
            "assets/box.png"
            ).scale(0.8).to_edge(LEFT, buff=1.5).shift(UP * 0.3)


        self.add(diagram1, )
        
        # Freccia tra i due diagrammi
        arrow = Arrow(
            start=diagram1.get_right() + RIGHT * 0.1,
            end=diagram1.get_right() + RIGHT * 2,
            buff=0,
            color=BLACK
        ).next_to(diagram1, RIGHT, buff=1.5).shift(DOWN *0.2)
        arrow_text = Tex(
            r"\textbf{Integrating out new physics}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(arrow, UP, buff=0.2)
        diagram2 = ImageMobject("assets/box_eft.png").scale(0.8).next_to(diagram1, RIGHT, buff=5)

        
        # Aggiungi tutto alla scena
        self.add(arrow, arrow_text, diagram2,)
        arrow_text_down = Tex(
            r"$\boldsymbol{\hat s,\hat t \ll M^2}$",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(arrow, DOWN, buff=0.2)
        self.add(arrow_text_down,)
        # Equation
        equation2 = MathTex(
            r"\mathcal{M}_\textrm{EFT} = G\left[1 + c_1\frac{\hat s}{M^2} +c_2\frac{\hat t}{M^2} + c_3\frac{\hat s^2}{M^4} + c_4 \frac{\hat s\hat t}{M^4} + \dots\right]",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram1, DOWN, buff=0.5).shift(RIGHT*4)
        self.add(equation2)
        
        equation2 = MathTex(
            r"\underbrace{\phantom{c_1\frac{\hat s}{M^2} +c_2\frac{\hat t}{M^2} + c_3\frac{\hat s^2}{M^4} + c_4 \frac{\hat s\hat t}{M^4} + \dots} }",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram1, DOWN, buff=1.5,).shift(RIGHT*5)
        self.add(equation2)

        equation3 = Tex(
            r"\textbf{Mandelstam Descendants}",
            font_size=32,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.2,).shift(LEFT*0.4)
        self.add(equation3)

class Slide_Parametrizing_EFT_Uncertainties_3(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parameterizing \\EFT Uncertainties}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Text
        text = Tex(
            r"The general structure from integrating out heavy physics is",
            font_size=36,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=.6)
        self.add(text)
        # Equation
        equation = MathTex(
            r"\mathcal{M}_\textrm{BSM}(12\rightarrow 34) = \sum_{\mathcal{O}}G_\mathcal{O}\mathcal{M}_\mathcal{O}\left[1 + c_{\mathcal{O},1}\frac{\hat s}{M^2} +c_{\mathcal{O},2}\frac{\hat t}{M^2} + c_{\mathcal{O},3}\frac{\hat s^2}{M^4} + c_{\mathcal{O},4} \frac{\hat s\hat t}{M^4} + \dots\right]",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation)
        
        # Subtitle
        subtitle = Tex(
            r"\textbf{What else do we need?}",
            font_size=36,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.5)
        self.add(subtitle)

        # Bullet points
        bullet1 = Tex(
            r"• A prior assumption that enforces $\mathcal{O}(1)$ $c_{\mathcal{O},i}$",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(subtitle, DOWN, buff=0.5).shift(LEFT*1.7)
        self.add(bullet1)
        bullet2 = Tex(
            r"• A modeling for $E \gtrsim M$ data \textcolor{IFAE_Color}{\textit{(Avoid Clipping)}}",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(bullet1, DOWN, buff=0.5).shift(RIGHT*0.15)
        self.add(bullet2)

class Slide_Parametrizing_EFT_Uncertainties_4(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parameterizing \\EFT Uncertainties}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Text  
        text = Tex(
            r"Given a single EFT operator $\boldsymbol{\mathcal{O}}$, with Wilson coefficient $\boldsymbol{G}$, we probe",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.6)
        self.add(text)
        
        # Equation
        equation = MathTex(
            r"\mathcal{M} = \mathcal{M}_\textrm{SM} + G \mathcal{M}_\mathcal{O} + O(G^2)",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation)

        # Text
        text2 = Tex(
            r"The \textbf{EFT uncertainties} are parameterized by rescaling the Wilson coefficient",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.5)
        self.add(text2)
        
        # Equation 2
        equation2 = MathTex(
            r"G \rightarrow G\mathcal{R}_\nu(x_1,x_2,x_3)\,,\quad x_1 = \frac{\hat s_{12}}{M^2}\,,\quad x_2 = \frac{\hat s_{13}}{M^2}\,,\quad x_3 = \frac{\hat s_{14}}{M^2}\,",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation2)
        
        # Important point 
        important = Tex(
            r"\textbf{Important:} No event generation needed!",
            font_size=32,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.5)
        self.add(important)

class Slide_Parametrizing_EFT_Uncertainties_5(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parameterizing \\EFT Uncertainties}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Text 
        text = Tex(
            r"The rescaling factor should",
            font_size=36,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.5).shift(LEFT*4)
        self.add(text)

        # Bullet points
        bullet1 = Tex(
            r"• \textcolor{IFAE_Color}{\textbf{Reproduce the expansion}} for $\boldsymbol{E \ll M}$ \textcolor{IFAE_Color}{(No unphysical energy growth)}",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.add(bullet1)
        
        bullet2 = Tex(
            r"• Account for \textcolor{IFAE_Color}{\textbf{lack of predictivity}} for $\boldsymbol{E \gtrsim M}$ \textcolor{IFAE_Color}{(100\% theory uncertainty)}",
            font_size=32,
            color=BLACK,            
            tex_template=my_template
        ).next_to(bullet1, DOWN, buff=0.3).to_edge(LEFT, buff=1)
        self.add(bullet2)
        
        # Equation
        equation = MathTex(
            r"\mathcal{R}_\nu(x_1,x_2,x_3) = \left(\frac{F(x_\textrm{max})}{x_\textrm{max}}\right)^{p/2}\sum_{\alpha,\beta,\gamma\geq0}\nu_{\alpha\beta\gamma}F(x_1)^\alpha F(x_2)^\beta F(x_3)^\gamma",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(bullet2, DOWN, buff=0.5).shift(RIGHT*1)
        self.add(equation)

        # Equation
        equation2 = MathTex(
            r"""F(x)  = \begin{cases}
                    x & |x|\leq 1 \\
                    \textrm{sign}(x) & |x| > 1
                \end{cases}\,,\quad \nu_{000} = 1,\quad x_\textrm{max} = \textrm{max}(x_1,x_2,x_3)
            """,
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.5).shift(RIGHT*-0)
        self.add(equation2)

class Slide_Parametrizing_EFT_Uncertainties_6(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parameterizing \\EFT Uncertainties}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Text
        text = Tex(
            r"•~When~$\boldsymbol{|x_{1,2,3}|\ll 1}\longrightarrow$~$G\mathcal{R}_\nu(x_1,x_2,x_3)~\mathcal{M}_\mathcal{O}~=~G~\mathcal{M}_\mathcal{O}[1~+~\nu_{100}~x_1~+~\nu_{010}~x_2~+~\nu_{110}~x_1~x_2+~\dots]$",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.6).shift(RIGHT*0)
        self.add(text)

        # Equation
        equation = Tex(
            r"\textbf{This reproduces }",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.3).shift(RIGHT*0)
        self.add(equation)

        equation2 = MathTex(
            r"\mathcal{M}_\textrm{BSM}(12\rightarrow 34) = G\mathcal{M}_\mathcal{O}\left[1 + c_{\mathcal{O},1}\frac{\hat s}{M^2} +c_{\mathcal{O},2}\frac{\hat t}{M^2} + c_{\mathcal{O},3}\frac{\hat s^2}{M^4} + c_{\mathcal{O},4} \frac{\hat s\hat t}{M^4} + \dots\right]",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.2).shift(RIGHT*0)
        self.add(equation2)

        # Text
        text = Tex(
            r"• In the \textbf{high energy limit},\quad $\mathcal{R}_\nu(x_1,x_2,x_3)\sim E^{-p}[1 + \nu_{100} + \nu_{010} + \nu_{110} + \dots]$",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.6).shift(RIGHT*-0.1)
        self.add(text)

        # Text
        text2 = Tex(
            r"We choose $p$ so that the modified amplitude is \textbf{independent of energy} in the UV ",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0.6)
        self.add(text2)

class Slide_Toy_Model(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Toy Model Implementation}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)
        
        # Image
        image = ImageMobject("assets/reach_s_different_binning_logscale.png")
        image.scale(1)
        image.next_to(title, DOWN, buff=0.2).shift(LEFT*3.75)
        self.add(image)
        
        # Text 
        text = MathTex(
            r"\mathcal{L} = \mathcal{L}_\textrm{QED} + \mathcal{L}_\textrm{QCD} - G(\bar u_L\gamma_\mu u_L)(\bar e_R \gamma^\mu e_R)",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(image, RIGHT, buff=0.5).shift(UP*2)
        self.add(text)


        # Text
        text2 = Tex(
            r"Partonic process $\boldsymbol{u\bar u \rightarrow e^+ e^-}$, energy growth $\boldsymbol{\sim E^2}$",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0.2)
        self.add(text2)
        
        # Text
        text3 = Tex(
            r"\textbf{Properties}",
            font_size=32,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=1).shift(RIGHT*0)
        self.add(text3)
        
        # Bullet points
        bullets = VGroup(
            Tex(r"• $n_\nu \sim 2$ gives convergent results", color = BLACK ,font_size=34, tex_template=my_template),
            Tex(r"• Asymptotic behavior as Plain EFT", color = BLACK, font_size=34, tex_template=my_template),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(image, buff=1).shift(DOWN*1.2)    
        self.add(bullets)

class Slide_Dependence_on_the_Prior(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Dependence on the Prior}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)
        
        # Image
        image = ImageMobject("assets/reach_s_different_priors.png")
        image.scale(1.3)
        image.next_to(title, DOWN, buff=0.4).shift(RIGHT*-4)
        self.add(image)

        # Text 
        text = MathTex(
            r"\mathcal{L}_\textrm{prior}(\nu) = \prod_{\alpha,\beta,\gamma}\exp\left(-\frac{\nu_{\alpha\beta\gamma}^2}{2\sigma_\nu^2}\right)\,,\quad \textrm{baseline: }\sigma_\nu = 3",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(image, RIGHT, buff=0.5).shift(UP*2)
        self.add(text)
        
        equation2 = MathTex(
            r"\underbrace{\phantom{\textrm{baseline: }\sigma_\nu = 3} }",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.05,).shift(RIGHT*2.25)
        self.add(equation2)

        equation3 = MathTex(
            r"\boldsymbol{\textbf{\textrm{Prob}}(|\nu|<3) = 0.68}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.2,).shift(LEFT*0.1)
        self.add(equation3)

        # text 
        text2 = Tex(
            r"• \textbf{\textcolor{IFAE_Color}{Predictivity}} requires ",
            font_size=26,
            color=BLACK,
            tex_template=my_template,
        ).next_to(image, RIGHT, buff=1).shift(UP*0.1)

        self.add(text2)
        
        text2_b = Tex(
            r"bounding \textbf{higher-order} EFT terms ",
            font_size=26,
            color=BLACK,
            tex_template=my_template,
        ).next_to(text2, DOWN, buff=0.1).shift(RIGHT*0.5)

        self.add(text2_b)        
        # text
        text3 = Tex(
            r"• \textbf{\textcolor{IFAE_Color}{Different priors}} correspond to \\ \textbf{different physical assumptions}",
            font_size=26,
            color=BLACK,
            tex_template=my_template
        ).next_to(text2_b, DOWN, buff=0.3).shift(RIGHT*0)
        self.add(text3)

class Slide_UV(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Comparison with UV Models}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagram 
        diagram = ImageMobject("assets/tree-vector-s-channel.png")
        diagram.scale(0.8)
        diagram.next_to(title, DOWN, buff=0.5).shift(LEFT*3.5)
        self.add(diagram)
        
        # Lagrangian
        lagrangian = MathTex(
            r"\mathcal{L}_{Z^\prime} = gZ^\prime_{\mu}(\bar u_L\gamma^\mu u_L + \bar e_R \gamma^\mu e_R)",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(lagrangian)
        
        # Diagram 2
        diagram2 = ImageMobject("assets/tree-t-channel.png")
        diagram2.scale(0.8)
        diagram2.next_to(title, DOWN, buff=0.5).shift(RIGHT*3)
        self.add(diagram2)

        # Lagrangian 2
        lagrangian2 = MathTex(
            r"\mathcal{L}_{\phi} = y (\phi\bar u_L e_R + \textrm{h.c.})",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram2, DOWN, buff=0.2)
        self.add(lagrangian2)
        
        # Diagram 3
        diagram3 = ImageMobject("assets/contact.png")
        diagram3.scale(0.8)
        diagram3.next_to(diagram, DOWN, buff=1.).shift(RIGHT*3.3)
        # self.add(diagram3)  

        # Lagrangian 3
        lagrangian3 = MathTex(
            r"\mathcal{L}_\textrm{EFT} = - G(\bar u_L\gamma_\mu u_L)(\bar e_R \gamma^\mu e_R)",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram3, DOWN, buff=0.2)
        # self.add(lagrangian3)
        
        arrow1 = Arrow(
            start=lagrangian.get_bottom()+RIGHT*1.5 + DOWN*0.3,
            end=diagram3.get_top() + DOWN*0.6,
            buff=0,
            color=IFAE_Color
        ).shift(LEFT*1.5)

        # Freccia dal diagramma φ → contact
        arrow2 = Arrow(
            start=lagrangian2.get_bottom() + DOWN*0.3+LEFT*1.5,
            end=diagram3.get_top() + DOWN*0.6,
            buff=0,
            color=IFAE_Color
        ).shift(RIGHT*1.5)

        # self.add(arrow1, arrow2)

        # Testo per arrow1
        arrow1_label = MathTex(
            r"\boldsymbol{G=\frac{g^2}{M_Z^2}}", font_size=26, color=IFAE_Color
        ).next_to(arrow1, DOWN, buff=0.01).shift(LEFT*0.4) 
        arrow1_label.shift(UP*0.3)
        arrow1_label.rotate(arrow1.get_angle())  # ruota lo stesso angolo della freccia

        # Testo per arrow2
        arrow2_label = MathTex(
            r"\boldsymbol{G=\frac{y^2}{2M_\phi^2}}", font_size=26, color=IFAE_Color
        ).next_to(arrow2, DOWN, buff=0.1).shift(RIGHT*0.4) 
        arrow2_label.shift(UP*0.3)
        arrow2_label.rotate(arrow2.get_angle()+ PI)

        # self.add(arrow1_label, arrow2_label)

class Slide_Exclusion(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Exclusion Limits}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Image
        image = ImageMobject("assets/uv_reach.png")
        image.scale(0.8)
        image.next_to(title, DOWN, buff=0.4)
        image.shift(LEFT*3.2)
        self.add(image)
        
        # Text
        text = MathTex(
            r"\mathfrak{L}_\textrm{Po} = \prod_{b\in\textrm{bins}}\textrm{Poiss}\left[\textrm{O}_b|\textrm{E}_b] ",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(image, RIGHT, buff=0.5).shift(UP*2.4)
        self.add(text)
        
        text = MathTex(
            r"\mathcal{L}_\textrm{prior}[\nu] = \prod_{\alpha,\beta,\gamma}\exp\left(-\frac{\nu_{\alpha\beta\gamma}^2}{2\sigma_\nu^2}\right)\,,\quad \textrm{baseline: }\sigma_\nu = 3   ",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.3).shift(RIGHT*1.2)
        self.add(text)
        
        
        # Text 2
        text2 = MathTex(
            r"\mathfrak{L}[G,\nu;\textrm{O}] = \mathfrak{L}_\textrm{Po}[\textrm{E}_b(G,\nu);\textrm{O}]\times \mathfrak{L}_\textrm{prior}[\nu]",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.3).shift(RIGHT*0.)
        self.add(text2)
        
        # Text 3
        text3 = MathTex(
            r"t(G) = 2 \textrm{log}\frac{\mathfrak{L}[\hat G,\hat\nu;\textrm{O}]}{\mathfrak{L}[G,\hat{\hat\nu}_G;\textrm{O}]}",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.3).shift(RIGHT*-0.9)
        self.add(text3)
        
        
        # Text 5
        text5 = Tex(
            r"\textbf{• Plain EFT limit is \textit{stronger} than t-channnel \\UV model limit}",
            font_size=26,
            color=ManimColor([0.5, 0.15, 0.15]),
            tex_template=my_template
        ).next_to(text3, DOWN, buff=0.5).shift(RIGHT*1)
        self.add(text5)
        
        # Text 4
        text4 = Tex(
            r"\textbf{• Our limit is weaker than UV-model limits}",
            font_size=26,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text5, DOWN, buff=0.5).shift(RIGHT*0.)
        self.add(text4)

class Slide_Exclusion_2(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Exclusion Limits}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Image
        image = ImageMobject("assets/uv_reach_M_vs_g_only_t.png")
        image.scale(0.8)
        image.next_to(title, DOWN, buff=0.4)
        image.shift(LEFT*0.5)
        self.add(image)

class Slide_Discovery(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Open Questions: Discovery}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Image
        image = ImageMobject("assets/discovery_reach.png")
        image.scale(0.6)
        image.next_to(title, DOWN, buff=0.5)
        image.shift(LEFT*0)
        self.add(image)

class Slide_Open_Questions(BaseSlide):
    def construct(self):
        self.setup_background()
        
        # Title
        title = Tex(
            r"\textbf{Open Questions: Three Point Couplings}",
            color=BLACK,
            font_size=42,
            tex_template=my_template
        ).to_edge(UP, buff=1.3)
        self.add(title)
        
        # equation 
        equation = MathTex(
            r"""
                \mathcal{L}_\text{SM} &= \tfrac 12 (\partial h)^2 - \tfrac 12 m_h^2 h^2
                - \frac{g_{hhh}}{3} h^3 
                + \bar{t} i \gamma^\mu \partial_\mu t -
                \frac{y_t}{\sqrt{2}} \left(v + h \right) \bar{t} t + \cdots,\quad \mathcal{L}_\text{BSM} = -\frac{1}{3}G_{hhh}h^3""",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation)
        
        # text
        text = MathTex(
            r"\downarrow{\textbf{\tiny{\tiny{Theory Uncertainties}}}}",
            font_size=75,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.2).shift(RIGHT*1)
        self.add(text)
        
        #equation 2
        equation2 = MathTex(
            r"""\mathcal{L}_\text{BSM} = 
                -\tfrac{1}{3} G_{hhh} \Bigg[ &
                h^3 + \frac{c_1}{M^2} h^2 \Box h
                + \frac{c_2}{M^4} h^2 \Box^2 h 
                + \frac{c_3}{M^4} h (\Box h)^2+ \cdots 
                \bigg]""",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.2).shift(RIGHT*-1)
        self.add(equation2)
        
        equation3 = Tex(
            r"$\Box h \sim \bar t t $",
            font_size=36,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.8).shift(RIGHT*-4)
        self.add(equation3)
        
        # Text
        text2 = MathTex(
            r"\underbrace{\phantom{\Box h \sim \bar t t } }",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(equation3, DOWN, buff=0.2).shift(RIGHT*0)
        self.add(text2)
        
        # Text
        text3 = Tex(
            r"\textbf{EOM}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.2).shift(RIGHT*0)
        self.add(text3)
        
        # Diagram 
        diagram1 = ImageMobject("assets/gluon_fusion_1.png")
        diagram1.scale(0.6)
        diagram1.next_to(equation3, RIGHT, buff=2)
        self.add(diagram1)
        
        # Text
        text2 = MathTex(
            r"\underbrace{\phantom{a \quad \quad \quad  a } } ",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(diagram1, DOWN, buff=0.1).shift(RIGHT*0)
        self.add(text2)
        
        # Text
        text3 = Tex(
            r"\textbf{$G_{hhh}h^3$}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.2).shift(RIGHT*0)
        self.add(text3)
        # arrow 
        text4 = Tex(
            r"$\boldsymbol{\longleftrightarrow}$",
            font_size=60,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(diagram1, RIGHT, buff=0.2).shift(RIGHT*0)
        self.add(text4)
        
        # Diagram 
        diagram2 = ImageMobject("assets/gluon_fusion_2.png")
        diagram2.scale(0.6)
        diagram2.next_to(text4, RIGHT, buff=0.5)
        self.add(diagram2)
        
        # Text
        text2 = MathTex(
            r"\underbrace{\phantom{a \quad \quad \quad  a } } ",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(diagram2, DOWN, buff=0.1).shift(RIGHT*0)
        self.add(text2)
        # Text
        text3 = Tex(
            r"\textbf{$G_{hht\bar t}h^2\bar t t$}",
            font_size=28,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.2).shift(RIGHT*0)
        self.add(text3)
        # arrow 
        text4 = Tex(
            r"$\boldsymbol{\longleftrightarrow}$",
            font_size=60,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(diagram1, RIGHT, buff=0.2).shift(RIGHT*0)
        self.add(text4)
class Slide_Conclusions(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Conclusions}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Bullet points
        bullet1 = Tex(
            r"• Modeling EFT uncertainties is \textbf{\textcolor{IFAE_Color}{the solution}} to EFT validity problem",
            font_size=34,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=1.2).shift(LEFT*0.5)
        self.add(bullet1)
        
        # subtitle 
        text = Tex(
            r"\textbf{Our proposal:}",
            font_size=32,
            color=IFAE_Color,
            tex_template=my_template
        ).next_to(bullet1, DOWN, buff=0.8).shift(RIGHT*0.5)
        self.add(text)
        bullet2 = Tex(
            r"• Well defined \textbf{statistical methodology} that makes explicit \textbf{\textcolor{IFAE_Color}{prior assumptions}}",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.4).shift(LEFT*0)
        self.add(bullet2)
        
        bullet3 = Tex(
            r"• Precise notion of cutoff $M$ enables ``final' state'' combinations",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(bullet2, DOWN, buff=0.4).shift(LEFT*0.95)
        self.add(bullet3)

        bullet4 = Tex(
            r"• Can be \textbf{\textcolor{IFAE_Color}{easily implemented}} with \textbf{event reweighting}",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(bullet3, DOWN, buff=0.4).shift(LEFT*.5)
        self.add(bullet4)

class Slide_Backup(BaseSlide):
    # Title "Backup Slides" in the middle
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Backup Slides}",
            color=BLACK,
            font_size=56,
            tex_template=my_template
        ).to_edge(UP, buff=4)
        self.add(title)

class Slide_Nuisance_Cancellation(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Nuisance Parameters Cancellation}",
            color=BLACK,
            font_size=36,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagram 
        diagram1 = ImageMobject("assets/bin_diff.png")
        diagram1.scale(0.8)
        diagram1.next_to(title, DOWN, buff=0.5).shift(LEFT*0.2)
        self.add(diagram1)

class Slide_s_t_u_nuisances(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{$s,t,u$ Nuisance Parameters  }",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagram 
        diagram1 = ImageMobject("assets/reach_s_t_u_vs_s.png")
        diagram1.scale(0.6)
        diagram1.next_to(title, DOWN, buff=0.5)
        self.add(diagram1)

class Slide_Different_Form_Factor(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Different Form Factor Choices}",
            color=BLACK,
            font_size=36,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Diagram 
        diagram1 = ImageMobject("assets/reach_s_ptbin_baseline_vs_F_x=x.png")
        diagram1.scale(0.6)
        diagram1.next_to(title, DOWN, buff=0.5)
        self.add(diagram1)

class Slide_Reweighting_Implementation(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Reweighting Procedure}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Text 
        text = Tex(
            r"The Feynman amplitude depends \textbf{linearly on $G$}, so the weight is a quadratic polynomial",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=1.2).shift(LEFT*0)
        self.add(text)
        
        # Equation
        equation = MathTex(
            r"w_e^{\textsc{eft}}(G)=w_e^{\textsc{sm}}\left[1+{\mathfrak{l}}_e\,\!G+{\mathfrak{q}}_e\,\!G^2\right]",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation)
        
        # Text
        text2 = Tex(
            r"where $w_e^{\textsc{sm}}$ are the event weights in the SM, normalized to $\sum_ew_e^{\textsc{sm}}=\sigma^{\textsc{sm}}$.\\ The linear and quadratic coefficients ${\mathfrak{l}}_e$ and ${\mathfrak{q}}_e$ are computed by \textbf{reweighting the MC sample} with two different nonzero values of $G$",
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(text2)

class Slide_Backup_Open_Questions(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Open Questions: Three Point Couplings}",
            color=BLACK,
            font_size=42,
            tex_template=my_template
        ).to_edge(UP, buff=1.3)
        self.add(title)

        # equation 
        equation = MathTex(
            r"""
                \mathcal{L}_\text{SM} &= \tfrac 12 (\partial h)^2 - \tfrac 12 m_h^2 h^2
                - \frac{g_{hhh}}{3} h^3 
                + \bar{t} i \gamma^\mu \partial_\mu t -
                \frac{y_t}{\sqrt{2}} \left(v + h \right) \bar{t} t + \cdots,\quad \mathcal{L}_\text{BSM} = -\frac{1}{3}G_{hhh}h^3""",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation)
        
        # text
        text = Tex(
            r"We could incorporate \textbf{\textcolor{IFAE_Color}{higher order EFT corrections}} to the Higgs cubic coupling similarly to what done for four-point interactions",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(text)
        
        #equation 2
        equation2 = MathTex(
            r"""\mathcal{L}_\text{BSM} = 
                -\tfrac{1}{3} G_{hhh} \Bigg[ &
                h^3 + \frac{c_1}{M^2} h^2 \Box h
                + \frac{c_2}{M^4} h^2 \Box^2 h 
                + \frac{c_3}{M^4} h (\Box h)^2+ \cdots 
                \bigg]""",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation2)
        
        text = Tex(
            r"However, \textbf{\textcolor{IFAE_Color}{higher derivative corrections}} to 3-point couplings can be eliminated by field redefinitions, effectively modifying only contact interactions.",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(text)

class Slide_Backup_Open_Questions_2(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Open Questions: Three Point Couplings}",
            color=BLACK,
            font_size=42,
            tex_template=my_template
        ).to_edge(UP, buff=1.3)
        self.add(title)
        
        # text
        text = Tex(
            r"Effectively using the \textbf{\textcolor{IFAE_Color}{equations of motion}} for the Higgs field, we obtain",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(title, DOWN, buff=0.6)
        self.add(text)
        

        # equation 2
        equation2 = MathTex(
            r"""
            \mathcal{L}_\text{BSM} \rightarrow
            -\frac 13 G_{hhh} \Bigg[&
            \left(1-c_1\frac{m_h^2}{M^2}+(c_2+c_3)\frac{m_h^4}{M^4}\right) h^3\\
            &-\frac{y_t}{\sqrt{2}} \left(\frac{c_1}{M^2}-\frac{(c_2+2c_3) m_h^2}{M^4}\right) h^2 \bar{t}t-\frac{y_t c_2}{\sqrt{2}M^4}  h^2 \Box(\bar{t}t) \Bigg]+O(G_{hhh}^2) 
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(text, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation2)
        
        # text 2
        text2 = Tex(
            r"""The $h^3$ form factor  is equivalent to \textbf{further modification
                of the coupling itself}, along with the \textbf{\textcolor{IFAE_Color}{addition of 4-point couplings}}""",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(equation2, DOWN, buff=0.5).shift(RIGHT*0) 
        self.add(text2)
        
        # equation 3
        equation3 = MathTex(
            r"""
            \mathcal{L}_\text{BSM} \rightarrow
            -\frac 13 G_{hhh}h^3 +\frac 12 G_{hht\bar t} h^2 \bar{t}t
            """,
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(text2, DOWN, buff=0.5).shift(RIGHT*0)
        self.add(equation3)




