%%manim -qm -v WARNING TestA
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

class TestA(Scene):
   def construct(self):
      triangle = Triangle()
      self.play(Create(triangle))
      text = Text("Segitiga").shift(UP*2.5)
      self.play(Write(text))
      self.wait()

      self.play(triangle.animate.set_x(-3))
      textL = Text("Luas =", font_size=32).shift(RIGHT*2)
      eqST1 = MathTex(r"\frac{alas \times tinggi}{2}").next_to(textL)
      eqST2 = MathTex(r"\frac{at}{2}").next_to(textL)
      self.play(Write(textL))
      self.play(Write(eqST1))
      self.wait(1.5)
      self.play(Transform(eqST1, eqST2))
      self.wait(1.5)
      self.play(Unwrite(eqST1))
      self.remove(eqST1)

      square = Square().shift(LEFT*3)
      eqP1 = MathTex(r"sisi \times sisi").next_to(textL)
      eqP2 = MathTex(r"s^2").next_to(textL)
      self.play(ReplacementTransform(triangle, square))
      self.play(Transform(text, Text("Persegi").shift(UP*2.5), run_time=0.5))
      self.play(Write(eqP1))
      self.wait(1.5)
      self.play(Transform(eqP1, eqP2))
      self.wait(1.5)
      self.play(Unwrite(eqP1))
      self.remove(eqP1)

      circle = Circle().shift(LEFT*3)
      eqL1 = MathTex(r"\pi \times jari-jari^2").next_to(textL)
      eqL2 = MathTex(r"\pi r^2").next_to(textL)
      self.play(ReplacementTransform(square, circle))
      self.play(Transform(text, Text("Lingkaran").shift(UP*2.5), run_time=0.5))
      self.play(Write(eqL1))
      self.wait(1.5)
      self.play(Transform(eqL1, eqL2))
      self.wait(1.5)
      self.play(Uncreate(circle), Unwrite(text), Unwrite(eqL1), Unwrite(textL))
      self.remove(circle, text, eqL1, textL)

      star = Star()
      pentagon = RegularPolygon(n=5)
      VGroup(star,pentagon).arrange(RIGHT)
      textE = Text("kalau ini?", font_size=20).shift(DOWN*2)
      self.play(FadeIn(star, pentagon))
      self.play(Write(textE))
      self.wait(2.5)
