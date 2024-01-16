%%manim -qm -v WARNING Effc_TestB
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

class Effc_TestB(Scene):
   def construct(self):
      tipe = VGroup(
        Tex(r'$\mathbb{N}$', color=YELLOW),     
        Text("Natural Numbers", font_size=14)
        )
      number = Tex(r"$ 1\ 2\ 3\ 4\ 5\ 6\ 7\ \cdots $")
      b = Brace(mobject=number, direction=DOWN, buff=0.2)
      b_text = Text("Bilangan Asli atau Bilangan Cacah ?", font_size=20).shift(DOWN*1)
      self.play(
          Write(tipe.arrange(DOWN).shift(LEFT*4)), 
          Write(number), run_time=1.5)
      self.play(GrowFromCenter(b), Create(b_text), run_time=1.5)
      self.wait(1.5)
      self.play(FadeOut(b), Uncreate(b_text), run_time=0.5)
      self.remove(b, b_text)

      self.play(
          Transform(tipe[0], Tex(r'$\mathbb{Z}$', color=YELLOW).shift(LEFT*4)),
          Transform(tipe[1], Text("Integers", font_size=14).next_to(tipe[0], DOWN), run_time=1.5),
          Transform(number, Tex(r"$ -3\ -2\ -1\ 0\ 1\ 2\ 3\ \cdots $"), run_time=1.5),
          )
      self.play(
          Transform(b_text, Text("Tidak termasuk Bilangan Pecahan", font_size=20).shift(DOWN)), 
          GrowFromCenter(b), run_time=1.5)
      self.wait(1.5)
      self.play(FadeOut(b), Uncreate(b_text), run_time=0.5)
      self.remove(b, b_text)

      self.play(
          Transform(tipe[0], Tex(r'$\mathbb{Q}$', color=YELLOW).shift(LEFT*4)),
          Transform(tipe[1], Text("Rational Numbers", font_size=14).next_to(tipe[0], DOWN*1), run_time=1.5),
          Transform(number, Tex(r"$ -4\ \frac{1}{3}\ \frac{3}{5}\ \frac{5}{6}\ 1\ 2\ \frac{23}{11}\ \cdots $"), run_time=1.5),
          )
      self.play(
          Transform(b_text, Text("Bilangan Bulat dan Bilangan Pecahan", font_size=20).shift(DOWN)), 
          GrowFromCenter(b), run_time=1.5)
      self.wait(1.5)
      self.play(FadeOut(b), Uncreate(b_text), run_time=0.5)
      self.remove(b, b_text)

      self.play(
          Transform(tipe[0], Tex(r'$\mathbb{R}$', color=YELLOW).shift(LEFT*4)),
          Transform(tipe[1], Text("Real Numbers", font_size=14).next_to(tipe[0], DOWN*1), run_time=1.5),
          Transform(number, Tex(r"$ -\frac{1}{2}\ \ln(2)\ 1\ \varphi\ \sqrt{2}\ e\ \pi\ \cdots $"), run_time=1.5),
          )
      self.play(
          Transform(b_text, Text("Bilangan Rasional dan Bilangan Irrasional", font_size=20).shift(DOWN)),
          GrowFromCenter(b), run_time=1.5)
      self.wait(1.5)
      self.play(FadeOut(b), Uncreate(b_text), Unwrite(tipe), Unwrite(number), run_time=0.5)
      self.remove(b, b_text, tipe, number)
    
      symbolC = Tex(r"$\mathbb{C}$\ ?  $\sqrt{-1}$\ ?", color=TEAL)
      textC = Text("waduh terlalu dalam", font_size=20).shift(DOWN*2)
      self.play(FadeIn(symbolC, run_time=2), Write(textC))
      self.wait(1.5)
