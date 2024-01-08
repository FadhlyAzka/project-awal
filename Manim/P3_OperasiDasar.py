%%manim -qm -v WARNING TestC
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

class TestC(Scene):
   def construct(self):
    text = Text("Penjumlahan").shift(UP*2)
    START = (2,-0.3,0)
    END =   (4,-0.3,0)
    line = Line(START,END);
    od1 = Tex(r" 2 + 7 = 9 ").shift(LEFT*3)
    od2 = Tex(r" 13\\ 8\\ 21 ").shift(RIGHT*3.5)
    symbol = Text("+", font_size=28).next_to(line, RIGHT)
    self.play(Write(text), Write(od1), Write(od2), Create(line), Write(symbol))
    self.wait(2)

    self.play(
        Transform(text, Text("Pengurangan").shift(UP*2)),
        Transform(od1, Tex(r" 6 $-$ 1 = 5 ").shift(LEFT*3)),
        Transform(od2, Tex(r" 35\\ 8\\ 27 ").shift(RIGHT*3.5)),
        Transform(symbol, Tex(r"$-$", font_size=28).next_to(line, RIGHT))
    )
    self.wait(2)

    self.play(
        Transform(text, Text("Perkalian").shift(UP*2)),
        Transform(od1, Tex(r"$ 7 \times 6 = 42 $").shift(LEFT*3)),
        Transform(od2, Tex(r" 14\\ 11\\ 154 ").shift(RIGHT*3.5)),
        Transform(symbol, Tex(r"$\times$", font_size=28).next_to(line, RIGHT))
    )
    self.wait(2)

# Beberapa bentuk pembagian: a/bb = a \div  = {a\over b} = frac{a}{b}
    od3 = Tex("atau\\", r" 72 / 12 = 6").next_to(od1, DOWN)
    self.play(
        Transform(text, Text("Pembagian").shift(UP*2)),
        Transform(od1, Tex(r"$ 72 \div 12 = 6 $").shift(LEFT*3)),
        Transform(od2, Tex(r" 68\\ 4\\ 17 ").shift(RIGHT*3.5)),
        Transform(symbol, Tex(r"$\div$", font_size=28).next_to(line, RIGHT)),
        Write(od3)
    )
    self.wait(2)

    self.play(Unwrite(od1), Unwrite(od2), Unwrite(od3), Uncreate(line), Unwrite(symbol), run_time=0.5)
    self.remove(od1, od2, od3, line, symbol)

    ot1 = MathTex(r"2^n = ", substrings_to_isolate=["n"]).shift(LEFT*3+UP)
    ot1.set_color_by_tex("n", YELLOW)
    ot1d = MathTex(r"2\times2\times2\times2\times2\times \cdots").next_to(ot1, RIGHT)
    ot2 = Tex(r"$ 3^{\frac{1}{2}} = $", "$ \sqrt{3} $").shift(LEFT*4+DOWN*3)
    ot3 = Tex(r"$ 2^{4} = 16 $").shift(DOWN*3)
    ot4 = Tex(r"$ 5^{-1} = \frac{1}{5} $").shift(RIGHT*4+DOWN*3)
    b = Brace(mobject=ot1d, direction=DOWN, buff=0.2)
    b_ot1 = b.get_text("berulang sampai nx").next_to(b, DOWN)
    b_ot1.set_color(YELLOW)
    self.play(
        Transform(text, Text("Perpangkatan").shift(UP*3)),
        Write(ot1), Write(ot1d)
    )
    self.play(GrowFromCenter(b), Create(b_ot1), run_time=1.5)
    self.play(Write(ot4), run_time=0.5)
    self.play(Write(ot3), run_time=0.5)
    self.play(Write(ot2), run_time=0.5)
    self.wait(2)
