import pace
from manim import *
import numpy as np

C_V1 = "#0072B2"   # blue
C_V2 = "#D55E00"   # orange
C_U = "#009E73"    # green
A = [[3, 1], [0, 2]]


def clear_screen(scene):
    scene.play(*[FadeOut(m) for m in scene.mobjects])


def eigen_step(scene, title, mat_tex, eq_tex, row_tex, choose_txt,
               v_tex, check_tex, color):
    t = Text(title, font_size=32).to_edge(UP)
    m = MathTex(mat_tex).scale(0.9)
    e = MathTex(eq_tex).scale(0.9)
    r = MathTex(row_tex, color=YELLOW)
    top = VGroup(m, e, r).arrange(DOWN, buff=0.5).move_to(ORIGIN)
    scene.play(Write(t), Write(m))
    scene.wait(3)
    scene.play(Write(e))
    scene.wait(3)
    scene.play(Write(r))
    scene.wait(3)
    scene.play(FadeOut(m), FadeOut(e))
    scene.play(r.animate.next_to(t, DOWN, buff=0.6))
    c = Text(choose_txt, font_size=28)
    v = MathTex(v_tex, color=color).scale(1.1)
    chk = MathTex(check_tex, color=color).scale(0.9)
    low = VGroup(c, v, chk).arrange(DOWN, buff=0.4).next_to(r, DOWN, buff=0.5)
    scene.play(Write(c))
    scene.wait(2)
    scene.play(Write(v))
    scene.wait(3)
    scene.play(Write(chk))
    scene.wait(4)


class Scene4Algebra2(Scene):
    def construct(self):
        # ---- Step 1: set up (A - lambda I) v = 0 ----
        t = Text("Step 1: set up the equation", font_size=32).to_edge(UP)
        l1 = MathTex(r"A\mathbf{v}=\lambda\mathbf{v}")
        l2 = MathTex(r"A\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}")
        l3 = MathTex(r"(A-\lambda I)\mathbf{v}=\mathbf{0}")
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(t), Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.wait(3)
        self.play(FadeOut(l1), FadeOut(l2))
        self.play(l3.animate.next_to(t, DOWN, buff=0.5))

        note = Text("(we write λv as λIv, so v factors out)",
                    font_size=24, color=GREY_B)
        ident = VGroup(
            MathTex(r"I=\begin{pmatrix}1&0\\0&1\end{pmatrix}"),
            Text("I: the identity matrix. It leaves every vector unchanged.",
                 font_size=26),
        ).arrange(DOWN, buff=0.2)
        det_txt = Text("A non-zero v exists only if A - λI squashes space, so:",
                       font_size=26)
        det_eq = MathTex(r"\det(A-\lambda I)=0", color=YELLOW)
        below = VGroup(note, ident, det_txt, det_eq).arrange(
            DOWN, buff=0.35).next_to(l3, DOWN, buff=0.4)
        for item in (note, ident, det_txt, det_eq):
            self.play(FadeIn(item))
            self.wait(3)
        clear_screen(self)

        # ---- Step 2: eigenvalues ----
        t2 = Text("Step 2: find the eigenvalues", font_size=32).to_edge(UP)
        m1 = MathTex(r"A-\lambda I=\begin{pmatrix}3-\lambda&1\\0&2-\lambda\end{pmatrix}")
        rem = MathTex(r"\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc",
                      color=GREY_B).scale(0.8)
        VGroup(m1, rem).arrange(DOWN, buff=0.5).move_to(UP * 0.8)
        self.play(Write(t2), Write(m1))
        self.wait(3)
        self.play(Write(rem))
        self.wait(3)
        self.play(FadeOut(rem))
        d1 = MathTex(r"\det(A-\lambda I)=(3-\lambda)(2-\lambda)-(1)(0)")
        d2 = MathTex(r"(3-\lambda)(2-\lambda)=0")
        res = MathTex(r"\lambda_1=3,\qquad \lambda_2=2", color=YELLOW).scale(1.2)
        VGroup(d1, d2, res).arrange(DOWN, buff=0.5).next_to(m1, DOWN, buff=0.6)
        self.play(Write(d1))
        self.wait(3)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(res))
        self.wait(3)
        clear_screen(self)

        # ---- Step 3: eigenvector for lambda = 3 ----
        eigen_step(
            self, "Step 3: eigenvector for λ = 3",
            r"A-3I=\begin{pmatrix}0&1\\0&-1\end{pmatrix}",
            r"\begin{pmatrix}0&1\\0&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}"
            r"=\begin{pmatrix}0\\0\end{pmatrix}",
            r"y=0,\quad x\ \text{is free}",
            "Choose x = 1",
            r"\mathbf{v}_1=\begin{pmatrix}1\\0\end{pmatrix}",
            r"A\mathbf{v}_1=\begin{pmatrix}3\\0\end{pmatrix}=3\,\mathbf{v}_1\ \checkmark",
            C_V1,
        )
        clear_screen(self)

        # ---- Step 4: eigenvector for lambda = 2 ----
        eigen_step(
            self, "Step 4: eigenvector for λ = 2",
            r"A-2I=\begin{pmatrix}1&1\\0&0\end{pmatrix}",
            r"\begin{pmatrix}1&1\\0&0\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}"
            r"=\begin{pmatrix}0\\0\end{pmatrix}",
            r"x+y=0\ \Rightarrow\ y=-x",
            "Choose x = -1",
            r"\mathbf{v}_2=\begin{pmatrix}-1\\1\end{pmatrix}",
            r"A\mathbf{v}_2=\begin{pmatrix}-2\\2\end{pmatrix}=2\,\mathbf{v}_2\ \checkmark",
            C_V2,
        )


class Scene4Decomp2(LinearTransformationScene):
    """u = v1 + v2, so Au = 3 v1 + 2 v2 = (1, 2)."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        d1 = DashedLine([1, 0, 0], [0, 1, 0], color=GREY_B)    # v1 tip to u tip
        d2 = DashedLine([-1, 1, 0], [0, 1, 0], color=GREY_B)   # v2 tip to u tip
        self.add_transformable_mobject(d1, d2)
        self.add_vector([1, 0], color=C_V1)
        self.add_vector([-1, 1], color=C_V2)
        self.add_vector([0, 1], color=C_U)
        lab = MathTex(
            r"\mathbf{u}=\mathbf{v}_1+\mathbf{v}_2=(1,0)+(-1,1)=(0,1)",
            color=C_U).scale(0.7).to_corner(UL)
        self.add_foreground_mobject(lab)
        self.wait(6)
        self.apply_matrix(A)
        lab2 = MathTex(
            r"A\mathbf{u}=3\mathbf{v}_1+2\mathbf{v}_2=(3,0)+(-2,2)=(1,2)",
            color=C_U).scale(0.7).to_corner(UL)
        self.play(Transform(lab, lab2))
        self.wait(7)
