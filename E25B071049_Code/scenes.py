import pace
from manim import *

C_V1 = "#0072B2"   # blue
C_V2 = "#D55E00"   # orange
C_U  = "#009E73"   # green
C_W  = "#CC79A7"   # purple
A = [[3, 1], [0, 2]]


class Scene3(LinearTransformationScene):
    """Grid deforms; eigenvectors stay on their lines."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        v1 = self.add_vector([1, 0], color=C_V1)
        v2 = self.add_vector([-1, 1], color=C_V2)
        self.wait(1)
        self.apply_matrix(A)
        self.wait(2)


class Scene4Algebra(Scene):
    """Finding eigenvalues and eigenvectors by hand."""
    def construct(self):
        t1 = Text("Step 1: (A - λI)v = 0", font_size=36).to_edge(UP)
        eq1 = MathTex(r"A\mathbf{v}=\lambda\mathbf{v}").scale(1.2)
        eq2 = MathTex(r"(A-\lambda I)\mathbf{v}=\mathbf{0}").scale(1.2)
        self.play(Write(t1), Write(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(eq2), FadeOut(t1))

        t2 = Text("Step 2: eigenvalues", font_size=36).to_edge(UP)
        m = MathTex(r"\det\begin{pmatrix}3-\lambda & 1\\ 0 & 2-\lambda\end{pmatrix}"
                    r"=(3-\lambda)(2-\lambda)=0")
        res = MathTex(r"\lambda_1=3,\quad \lambda_2=2",
                      color=YELLOW_D).next_to(m, DOWN, buff=0.8)
        self.play(Write(t2), Write(m))
        self.wait(2)
        self.play(Write(res))
        self.wait(2)
        self.play(FadeOut(m), FadeOut(res), FadeOut(t2))

        t3 = Text("Step 3: eigenvectors", font_size=36).to_edge(UP)
        e1 = MathTex(r"\lambda_1=3:\ \mathbf{v}_1=\begin{pmatrix}1\\0\end{pmatrix}",
                     color=C_V1)
        e2 = MathTex(r"\lambda_2=2:\ \mathbf{v}_2=\begin{pmatrix}-1\\1\end{pmatrix}",
                     color=C_V2)
        VGroup(e1, e2).arrange(DOWN, buff=1).move_to(ORIGIN)
        self.play(Write(t3), Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.wait(3)


class Scene4Decomp(LinearTransformationScene):
    """u = v1 + v2, so Au = 3v1 + 2v2 = (1, 2)."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        v1 = self.add_vector([1, 0], color=C_V1)
        v2 = self.add_vector([-1, 1], color=C_V2)
        u = self.add_vector([0, 1], color=C_U)
        self.wait(2)
        self.apply_matrix(A)
        self.wait(3)
