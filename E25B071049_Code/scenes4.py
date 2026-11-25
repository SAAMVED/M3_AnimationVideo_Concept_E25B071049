import pace
from manim import *

A = [[3, 1], [0, 2]]


class Scene3Columns(LinearTransformationScene):
    """Columns of A = where the basis arrows land."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        a_mat = MathTex(r"A=\begin{pmatrix}3&1\\0&2\end{pmatrix}").to_corner(UL)
        before = MathTex(r"\hat{\imath}=(1,0),\ \hat{\jmath}=(0,1)").next_to(
            a_mat, DOWN, aligned_edge=LEFT)
        self.add_foreground_mobject(a_mat, before)
        self.wait(4)
        self.apply_matrix(A)
        after = MathTex(
            r"A\hat{\imath}=(3,0),\ A\hat{\jmath}=(1,2)").next_to(
            a_mat, DOWN, aligned_edge=LEFT)
        note = Text("These are the columns of A", font_size=28).next_to(
            after, DOWN, aligned_edge=LEFT)
        self.play(Transform(before, after), Write(note))
        self.wait(5)
