%%manim -qm -v WARNING Effc_TestA
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

class Effc_TestA(Scene):
   def construct(self):
      triangle = Triangle()
      text = Text("Segitiga").shift(UP*2.5)
      self.play(Create(triangle))
      self.play(Write(text))
      self.wait()

      eq = VGroup(
          Text("Luas =", font_size=32),
          MathTex(r"\frac{alas \times tinggi}{2}")
          )
      self.play(triangle.animate.set_x(-3))
      self.play(Write(eq.arrange(RIGHT).shift(RIGHT*2)))
      self.wait(1.5)
      self.play(Transform(eq[1], MathTex(r"\frac{at}{2}").next_to(eq[0],RIGHT)))
      self.wait(1.5)
      self.play(Unwrite(eq[1]))
      self.remove(eq[1])

      square = Square().shift(LEFT*3)
      self.play(
          ReplacementTransform(triangle, square),
          Transform(text, Text("Persegi").shift(UP*2.5), run_time=0.5),
          Transform(eq[1], MathTex(r"sisi \times sisi").next_to(eq[0],RIGHT))
          )
      self.wait(1.5)
      self.play(Transform(eq[1], MathTex(r"s^2").next_to(eq[0],RIGHT)))
      self.wait(1.5)
      self.play(Unwrite(eq[1]))
      self.remove(eq[1])

      circle = Circle().shift(LEFT*3)
      self.play(
          ReplacementTransform(square, circle),
          Transform(text, Text("Lingkaran").shift(UP*2.5), run_time=0.5),
          Transform(eq[1], MathTex(r"\pi \times jari-jari^2").next_to(eq[0],RIGHT))
          )
      self.wait(1.5)
      self.play(Transform(eq[1], MathTex(r"\pi r^2").next_to(eq[0],RIGHT)))
      self.wait(1.5)
      self.play(Uncreate(circle), Unwrite(text), Unwrite(eq))
      self.remove(circle, text, eq)

      figure = VGroup(Star(), RegularPolygon(n=5)).arrange(RIGHT)
      textE = Text("kalau ini?", font_size=20).shift(DOWN*2)
      self.play(FadeIn(figure), Write(textE))
      self.wait(2.5)
