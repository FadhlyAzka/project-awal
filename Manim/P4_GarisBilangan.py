%%manim -qm -v WARNING TestD
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

class TestD(Scene):
   def construct(self):
      D1 = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
        )
      text = Text("Garis Bilangan", weight=BOLD, font_size=36).to_corner(UP + LEFT)
      textD = Tex("Vektor pada Ruang Satu Dimensi ", r"($\mathbb{R}^1$)", font_size=20).next_to(text, DOWN)

      vT_1 = Vector([4, 0], color=RED)
      vT_2 = Vector([1, 0], color=YELLOW).shift(RIGHT*4)
      vT_3 = Vector([5, 0], color=BLUE).shift(DOWN*0.65)
      labelT_1 = Tex("4").next_to(vT_1, UP)
      labelT_2 = Tex("1").next_to(vT_2, UP)
      labelT_3 = Tex("5").next_to(vT_3, DOWN)
      eqT = MathTex("4", "+","1", "=", "5").shift(UP*2)
      self.play(Write(text), Write(textD), DrawBorderThenFill(D1), run_time=3.5)
      self.play(Create(vT_1), Write(labelT_1))
      self.play(Create(vT_2), Write(labelT_2))
      self.play(Create(vT_3), Write(labelT_3))
      self.play(
            TransformMatchingShapes(
                VGroup(labelT_1[0].copy(), labelT_2[0].copy(), labelT_3[0].copy()), eqT,
            ), 
            run_time=2
        ) 
      self.wait()
      self.play(Uncreate(vT_1), Uncreate(vT_2), Uncreate(vT_3), Unwrite(eqT),
                Unwrite(labelT_1), Unwrite(labelT_2), Unwrite(labelT_3))
      self.remove(vT_1, vT_2, vT_3, eqT, labelT_1, labelT_2, labelT_3)

      vK_1 = Vector([2, 0], color=RED)
      vK_2 = Vector([-5, 0], color=YELLOW).shift(RIGHT*2)
      vK_3 = Vector([-3, 0], color=BLUE).shift(DOWN*0.65)
      labelK_1 = Tex("2").next_to(vK_1, UP)
      labelK_2 = Tex("$-$5").next_to(vK_2, UP*1.3)
      labelK_3 = Tex("$-$3").next_to(vK_3, DOWN)
      eqK = MathTex("2 - 5 = -3").shift(UP*2)
      self.play(Create(vK_1), Write(labelK_1))
      self.play(Create(vK_2), Write(labelK_2))
      self.play(Create(vK_3), Write(labelK_3))
      self.play(
            TransformMatchingShapes(
                VGroup(labelK_1[0].copy(), labelK_2[0].copy(), labelK_3[0].copy()), eqK), 
            vK_1.animate.set_y(1), 
            vK_2.animate.set_y(1.3),
            run_time=2
        ) 
      self.wait()
      self.play(FadeOut(D1), Uncreate(vK_1), Uncreate(vK_2), Uncreate(vK_3), 
                Unwrite(eqK), Unwrite(labelK_1), Unwrite(labelK_2), Unwrite(labelK_3))
      self.remove(D1, vK_1, vK_2, vK_3, eqT, labelK_1, labelK_2, labelK_3)

      textC = Text("tenang, ini masih bisa dipahami", font_size=20).shift(DOWN*2)
      self.play(
          FadeOut(text), 
          FadeOut(textD),
          Transform(textD[1].copy(), Tex(r"$\mathbb{R}^2$\ ?", color=TEAL)),
          run_time=2
      )
      self.play(Write(textC))
      self.wait(1.5)
