%%manim -qm -v WARNING TestB
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab
# Syntax Tex bisa diubah ke syntax MathTex dengan menghilangkan $$, 
# namun dengan kekurangan font-size string MathTex tidak fleksibel 

class TestB(Scene):
   def construct(self):
    symbol = Tex(r'$\mathbb{N}$', color=YELLOW).shift(LEFT*4)
    text = Text("Natural Numbers", font_size=14).next_to(symbol, DOWN*1)
    textD = Tex(r"$ 0\ 1\ 2\ 3\ 4\ 5\ 6\ \cdots $")
    b = Brace(mobject=textD, direction=DOWN, buff=0.2)
    b_textN = Text("Bilangan Asli atau Bilangan Cacah ?", font_size=20).shift(DOWN*1)
    self.play(Write(symbol), Write(text), Write(textD), run_time=1.5)
    self.play(GrowFromCenter(b), Create(b_textN), run_time=1.5)
    self.wait(1.5)
    self.play(FadeOut(b), Uncreate(b_textN), run_time=0.5)
    self.remove(b, b_textN)

    self.play(
        Transform(symbol, Tex(r'$\mathbb{Z}$', color=YELLOW).shift(LEFT*4)),
        Transform(text, Text("Integers", font_size=14).next_to(symbol, DOWN*1), run_time=1.5),
        Transform(textD, Tex(r"$ -3\ -2\ -1\ 0\ 1\ 2\ 3\ \cdots $"), run_time=1.5),
        )
    b_textI = Text("Tidak termasuk Bilangan Pecahan", font_size=20).shift(DOWN*1)
    self.play(GrowFromCenter(b), Create(b_textI), run_time=1.5)
    self.wait(1.5)
    self.play(FadeOut(b), Uncreate(b_textI), run_time=0.5)
    self.remove(b, b_textI)

    self.play(
        Transform(symbol, Tex(r'$\mathbb{Q}$', color=YELLOW).shift(LEFT*4)),
        Transform(text, Text("Rational Numbers", font_size=14).next_to(symbol, DOWN*1), run_time=1.5),
        Transform(textD, Tex(r"$ -4\ \frac{1}{3}\ \frac{3}{5}\ \frac{5}{6}\ 1\ 2\ \frac{23}{11}\ \cdots $"), run_time=1.5),
        )
    b_textR = Text("Bilangan Bulat dan Bilangan Pecahan", font_size=20).shift(DOWN*1)
    self.play(GrowFromCenter(b), Create(b_textR), run_time=1.5)
    self.wait(1.5)
    self.play(FadeOut(b), Uncreate(b_textR), run_time=0.5)
    self.remove(b, b_textR)

    self.play(
        Transform(symbol, Tex(r'$\mathbb{R}$', color=YELLOW).shift(LEFT*4)),
        Transform(text, Text("Real Numbers", font_size=14).next_to(symbol, DOWN*1), run_time=1.5),
        Transform(textD, Tex(r"$ -\frac{1}{2}\ \ln(2)\ 1\ \varphi\ \sqrt{2}\ e\ \pi\ \cdots $"), run_time=1.5),
        )
    b_textRl = Text("Bilangan Rasional dan Bilangan Irrasional", font_size=20).shift(DOWN*1)
    self.play(GrowFromCenter(b), Create(b_textRl), run_time=1.5)
    self.wait(1.5)
    self.play(FadeOut(b), Uncreate(b_textRl), Unwrite(symbol), Unwrite(text), Unwrite(textD), run_time=0.5)
    self.remove(b, b_textRl, symbol, text, textD)

    symbolC = Tex(r"$\mathbb{C}$\ ?  $\sqrt{-1}$\ ?", color=TEAL)
    textC = Text("waduh terlalu dalam", font_size=20).shift(DOWN*2)
    self.play(FadeIn(symbolC, run_time=2))
    self.play(Write(textC))
    self.wait(1.5)
