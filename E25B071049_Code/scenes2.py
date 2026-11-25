import pace
from manim import *
import numpy as np

# ---- shared constants (same as scenes.py) ----
C_V1 = "#0072B2"   # blue   : v1
C_V2 = "#D55E00"   # orange : v2
C_U = "#009E73"    # green  : u
C_W = "#CC79A7"    # purple : test vector w
A = [[3, 1], [0, 2]]


def faint_plane():
    return NumberPlane(
        x_range=[-8, 8, 1], y_range=[-5, 5, 1],
        background_line_style={"stroke_opacity": 0.3},
    )


def clear_screen(scene):
    scene.play(*[FadeOut(m) for m in scene.mobjects])


# =====================================================================
# SCENE 1: Opening frame + hook
# =====================================================================
class Scene1Hook(Scene):
    def construct(self):
        # --- opening frame ---
        title = Text("Eigenvalues and Eigenvectors", font_size=54)
        sub = Text("The directions a matrix cannot turn", font_size=30, color=GREY_B)
        who = Text("Ansh Jangir  |  E25B071049  |  M3 Internal Assessment",
                   font_size=24)
        group = VGroup(title, sub, who).arrange(DOWN, buff=0.5)
        self.play(FadeIn(group, shift=UP * 0.3))
        self.wait(4)
        self.play(FadeOut(group))

        # --- house on a grid ---
        self.add(faint_plane())
        base = Polygon(
            [-1, 0, 0], [1, 0, 0], [1, 1.2, 0], [0, 2, 0], [-1, 1.2, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.35,
        )
        house = base.copy()
        self.play(Create(house))
        self.wait(1)

        shear = [[1, 1], [0, 1]]
        squash = [[1.6, 0], [0, 0.6]]
        rotate = [[0, -1], [1, 0]]
        for M in (shear, squash, rotate):
            self.play(Transform(house, base.copy().apply_matrix(M)), run_time=2)
            self.wait(0.5)
            self.play(Transform(house, base.copy()), run_time=1.5)

        # --- two directions stay put (for the matrix A used later) ---
        x_line = Line([-8, 0, 0], [8, 0, 0], color=C_V1, stroke_width=6)
        d_line = Line([-4, 4, 0], [4, -4, 0], color=C_V2, stroke_width=6)
        cap = Text("Some directions stay put.", font_size=34).to_edge(DOWN)
        self.play(Create(x_line), Create(d_line), Write(cap))
        self.play(Transform(house, base.copy().apply_matrix(A)), run_time=3)
        self.wait(2)


# =====================================================================
# SCENE 2: Concept introduction (notation first)
# =====================================================================
class Scene2Concept(Scene):
    def construct(self):
        self.add(faint_plane())

        # 1. vector
        v = Arrow(ORIGIN, np.array([1.0, 1.0, 0.0]), buff=0, color=YELLOW)
        v_lab = MathTex(r"\mathbf{v}", color=YELLOW).next_to(v.get_end(), UP, buff=0.1)
        cap = Text("vector v: an arrow, written as a column", font_size=28).to_edge(DOWN)
        col = MathTex(r"\mathbf{v}=\begin{pmatrix}x\\y\end{pmatrix}").to_corner(UR)
        self.play(GrowArrow(v), Write(v_lab), Write(cap), Write(col))
        self.wait(3)

        # 2. matrix moves v to Av
        a_mat = MathTex(r"A=\begin{pmatrix}3&1\\0&2\end{pmatrix}").to_corner(UL)
        cap2 = Text("matrix A: a rule that moves every vector",
                    font_size=28).to_edge(DOWN)
        av = Arrow(ORIGIN, np.array([4.0, 2.0, 0.0]), buff=0, color=RED_C)
        av_lab = MathTex(r"A\mathbf{v}", color=RED_C).next_to(av.get_end(), UP, buff=0.1)
        curve = CurvedArrow(v.get_end() + 0.1 * UP, av.get_end() + 0.1 * LEFT + 0.1 * UP,
                            angle=-TAU / 6, color=GREY_B)
        self.play(Write(a_mat), ReplacementTransform(cap, cap2))
        self.wait(1)
        self.play(GrowArrow(av), Write(av_lab), Create(curve))
        self.wait(3)

        clear_screen(self)

        # 3. definition
        eq = MathTex(r"A\mathbf{v}", r"=", r"\lambda", r"\mathbf{v}").scale(2)
        eq[2].set_color(YELLOW)
        self.play(Write(eq))
        lam_note = Text("λ (lambda): just a number, the eigenvalue",
                        font_size=30, color=YELLOW).next_to(eq, DOWN, buff=0.9)
        pointer = Arrow(lam_note.get_top(), eq[2].get_bottom(), buff=0.1, color=YELLOW)
        self.play(Write(lam_note), GrowArrow(pointer))
        self.wait(3)

        nz = MathTex(r"\mathbf{v}\neq\mathbf{0}").scale(1.2).to_edge(UP, buff=0.8)
        nz_note = Text("(the zero vector works for every A, so we exclude it)",
                       font_size=24, color=GREY_B).next_to(nz, DOWN, buff=0.2)
        self.play(Write(nz), FadeIn(nz_note))
        self.wait(3)

        clear_screen(self)

        # 4. what lambda does
        nl = NumberLine(x_range=[-3, 3, 1], length=10, include_numbers=True)
        nl.shift(DOWN * 0.8)
        eq_small = MathTex(r"A\mathbf{v}=\lambda\mathbf{v}").to_edge(UP)
        self.play(Create(nl), Write(eq_small))

        def arr(val, col):
            return Arrow(nl.n2p(0) + UP * 0.8, nl.n2p(val) + UP * 0.8,
                         buff=0, color=col)

        cur = arr(1, GREY_B)
        cur_lab = MathTex(r"\mathbf{v}", color=GREY_B).next_to(cur, UP, buff=0.1)
        self.play(GrowArrow(cur), Write(cur_lab))
        self.wait(1)

        cases = [
            (2, GREEN, "λ = 2 (λ > 1): stretches"),
            (0.5, ORANGE, "λ = 0.5 (0 < λ < 1): compresses"),
            (-1, RED, "λ = -1 (λ < 0): flips through the origin"),
        ]
        cap = Text("v", font_size=1).to_edge(DOWN)  # placeholder
        self.add(cap)
        for val, col, txt in cases:
            new = arr(val, col)
            new_cap = Text(txt, font_size=30, color=col).to_edge(DOWN, buff=1)
            self.play(ReplacementTransform(cur, new),
                      ReplacementTransform(cap, new_cap), run_time=1.5)
            cur, cap = new, new_cap
            self.wait(3)
        self.wait(1)


# =====================================================================
# SCENE 3 extras: test vector, eigen-lines, compression demo
# =====================================================================
class Scene3TestVector(LinearTransformationScene):
    """w = (1, 1) is knocked off its line; (4, 2) is not on y = x."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True, leave_ghost_vectors=True, **kwargs)

    def construct(self):
        orig_line = DashedLine([-6, -6, 0], [6, 6, 0], color=C_W)
        self.add(orig_line)
        w = self.add_vector([1, 1], color=C_W)
        lab = Text("w = (1, 1)", font_size=28, color=C_W).to_corner(UL)
        self.add_foreground_mobject(lab)
        self.wait(2)
        self.apply_matrix(A)
        lab2 = Text("Aw = (4, 2): off the line y = x", font_size=28,
                    color=C_W).to_corner(UL)
        self.play(Transform(lab, lab2))
        self.wait(3)


class Scene3EigenLines(LinearTransformationScene):
    """Vectors on the x-axis and on y = -x stay on their lines."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True, leave_ghost_vectors=True, **kwargs)

    def construct(self):
        x_line = Line([-9, 0, 0], [9, 0, 0], color=C_V1, stroke_width=6)
        d_line = Line([-6, 6, 0], [6, -6, 0], color=C_V2, stroke_width=6)
        self.add_transformable_mobject(x_line, d_line)
        self.add_vector([1, 0], color=C_V1)
        self.add_vector([-1, 1], color=C_V2)
        lab = Text("Blue: x-axis   Orange: y = -x", font_size=28).to_corner(UL)
        self.add_foreground_mobject(lab)
        self.wait(2)
        self.apply_matrix(A)
        lab2 = Text("Blue x3,  Orange x2: both stay on their lines",
                    font_size=28).to_corner(UL)
        self.play(Transform(lab, lab2))
        self.wait(3)


class Scene3Compress(LinearTransformationScene):
    """Side demo with a DIFFERENT matrix B (not A): lambda = 0.5 compresses."""
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True, leave_ghost_vectors=True, **kwargs)

    def construct(self):
        B = [[0.5, 0], [0, 1]]
        title = Text("A different matrix B, just for intuition",
                     font_size=28).to_corner(UL)
        b_mat = MathTex(r"B=\begin{pmatrix}0.5&0\\0&1\end{pmatrix}").next_to(
            title, DOWN, aligned_edge=LEFT)
        self.add_foreground_mobject(title, b_mat)
        self.add_vector([4, 0], color=YELLOW)
        self.wait(2)
        self.apply_matrix(B)
        lab = MathTex(r"\lambda=0.5:\ \text{compressed}", color=YELLOW).to_edge(DOWN)
        self.add_foreground_mobject(lab)
        self.wait(3)


# =====================================================================
# SCENE 5: Interpretation
# =====================================================================
class Scene5Interpret(Scene):
    def construct(self):
        v1 = np.array([1.0, 0.0, 0.0])
        v2 = np.array([-1.0, 1.0, 0.0])
        s = 0.3
        ks = range(-2, 3)

        def std_grid():
            g = VGroup()
            for k in ks:
                g.add(Line([k, -2, 0], [k, 2, 0]), Line([-2, k, 0], [2, k, 0]))
            return g.set_stroke(GREY_B, width=1.5, opacity=0.7)

        def eig_grid():
            g = VGroup()
            for k in ks:
                g.add(Line(k * v1 - 2 * v2, k * v1 + 2 * v2),
                      Line(k * v2 - 2 * v1, k * v2 + 2 * v1))
            g.set_stroke(GREY_B, width=1.5, opacity=0.7)
            g.add(Line(-2 * v1, 2 * v1, color=C_V1, stroke_width=5),
                  Line(-2 * v2, 2 * v2, color=C_V2, stroke_width=5))
            return g

        left = std_grid().scale(s, about_point=ORIGIN).shift(LEFT * 3.6)
        right = eig_grid().scale(s, about_point=ORIGIN)
        target = right.copy().apply_matrix(A)
        right.shift(RIGHT * 3.6)
        target.shift(RIGHT * 3.6)

        t_left = Text("Standard grid", font_size=26).move_to(LEFT * 3.6 + UP * 2.6)
        t_right = Text("Grid built from v1 and v2", font_size=26).move_to(
            RIGHT * 3.6 + UP * 2.6)
        self.play(FadeIn(left), FadeIn(right), Write(t_left), Write(t_right))
        self.wait(2)

        note = Text("Apply A: along each eigenvector it is a pure stretch",
                    font_size=28).to_edge(DOWN, buff=1.6)
        self.play(Write(note))
        self.play(Transform(right, target), run_time=3)
        self.wait(2)

        callouts = [
            "Any multiple of an eigenvector is also an eigenvector",
            "Eigenvectors need not be perpendicular (here they are 135° apart)",
            "Area scales by det A = 3 × 2 = 6",
            "Used in: Google PageRank, PCA, vibration modes",
        ]
        cur = None
        for txt in callouts:
            new = Text(txt, font_size=30, color=YELLOW).to_edge(DOWN, buff=0.6)
            if cur is None:
                self.play(Write(new))
            else:
                self.play(ReplacementTransform(cur, new))
            cur = new
            self.wait(4)


# =====================================================================
# SCENE 6: Summary and credits
# =====================================================================
class Scene6Summary(Scene):
    def construct(self):
        head = Text("Summary", font_size=48).to_edge(UP)
        self.play(Write(head))

        items = [
            (MathTex(r"A\mathbf{v}=\lambda\mathbf{v}"),
             "1. An eigenvector keeps its line; λ is its scale factor"),
            (MathTex(r"\det(A-\lambda I)=0,\quad (A-\lambda I)\mathbf{v}=\mathbf{0}"),
             "2. Solve for λ first, then for each eigenvector"),
            (MathTex(r"\mathbf{u}=c_1\mathbf{v}_1+c_2\mathbf{v}_2\ \Rightarrow\ "
                     r"A\mathbf{u}=c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2"),
             "3. Split a vector into eigenvector parts; scale each by its own λ"),
        ]
        rows = VGroup()
        for m, t in items:
            m.scale(0.9)
            rows.add(VGroup(Text(t, font_size=28), m).arrange(DOWN, buff=0.25))
        rows.arrange(DOWN, buff=0.6).next_to(head, DOWN, buff=0.6)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.2))
            self.wait(6)
        self.wait(2)
        clear_screen(self)

        # credits card
        lines = [
            Text("Credits", font_size=44),
            Text("Created by Ansh Jangir, E25B071049", font_size=28),
            Text("Tools: Manim Community v0.22.1, Python",
                 font_size=24),
            Text("AI disclosure: AI (Claude, by Anthropic) was used to help draft the "
                 "script, storyboard and animation code.", font_size=22),
            Text("All mathematics was independently verified by the student.",
                 font_size=22),
        ]
        credits = VGroup(*lines).arrange(DOWN, buff=0.35)
        self.play(FadeIn(credits))
        self.wait(6)
