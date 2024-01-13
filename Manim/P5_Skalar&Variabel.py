%%manim -qm -v WARNING TestE
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab
# Beberapa referensi code: https://infograph.tistory.com/158

class TestE(Scene):
    def construct(self):
      D1 = NumberLine(
            x_range=[-10, 10, 1],
            include_numbers=True,
            unit_size=0.5,
            tick_size=0.1,
            font_size=20
        )
      text = Text("Skalar", weight=BOLD, font_size=30).shift(DOWN*2+LEFT*3)
      eqS = Tex(r"$\vec{p}$ = ", "1", font_size=30).shift(DOWN*2)
      vX_1 = Vector([0.5, 0], color=BLUE)
      labelX_1 = Tex(r"$\vec{p}$", font_size=20).next_to(vX_1, UP)
      self.play(DrawBorderThenFill(D1), run_time=2.5)
      self.play(Create(vX_1), Write(labelX_1))
      self.play(Write(text), Write(eqS))
      self.wait(1.5)

      tracker = ValueTracker(1)
      def get_line_obj():
          sp = D1.number_to_point(tracker.get_value())
          ep = sp + UP*1.5
          arrow = Arrow(sp,ep,buff=0,color=RED)
          num = DecimalNumber(tracker.get_value(), color=YELLOW).next_to(arrow, UP)
          return VGroup(arrow, num)
      obj = always_redraw(get_line_obj)
      labelX_1.add_updater(lambda labelX_1: labelX_1.next_to(vX_1, UP))
      self.add(obj)
      self.wait()
        
      self.play(
          Transform(eqS[1], Tex("5", font_size=30).next_to(eqS[0])),
          tracker.animate.set_value(5),
          Transform(vX_1, Vector([2.5, 0], color=BLUE)),
          run_time=3,
      )
      self.play(
          Transform(eqS[1], Tex("-10", font_size=30).next_to(eqS[0])),
          tracker.animate.set_value(-10),
          Transform(vX_1, Vector([-5, 0], color=BLUE)),
          run_time=3,
      )
      self.wait()
      self.play(Uncreate(vX_1), Unwrite(text), Unwrite(labelX_1), Unwrite(eqS))
      self.remove(vX_1, text, labelX_1, eqS, obj)

      eqA = Tex("persamaan = ","1", font_size=30).shift(DOWN*2)
      eqJ_1 = Tex("= x", font_size=30).next_to(eqA[1])
      vX_1 = Vector([0.5, 0], color=RED)
      labelX_1 = Tex("x", font_size=24).next_to(vX_1, UP)
      self.play(
          Transform(text, Text("Variabel", weight=BOLD, font_size=30).shift(DOWN*2+LEFT*3)),
          Create(vX_1), 
          Write(labelX_1),
          Write(eqA)
      )
      self.play(TransformMatchingShapes(labelX_1.copy(), eqJ_1))

      eqA_2 = Tex("persamaan = ","2", font_size=30).shift(DOWN*2)
      eqJ_2 = Tex("= x + x", font_size=30).next_to(eqA[1])
      eqJ_3 = Tex("= 2x", font_size=30).next_to(eqA[1])
      vS_1 = vX_1.copy()
      vS_2 = vX_1.copy().shift(RIGHT*0.5) 
      vS_2.set_color(YELLOW)
      labelS_1 = Tex("x", font_size=24).next_to(vS_2, UP)
      self.play(Transform(vS_1, vS_2, path_arc=-90*DEGREES)) # animasi menambah vektor dengan rotasi searah jarum jam
      self.play(Write(labelS_1))
      self.play(
          Transform(eqA[1], eqA_2[1]),
          TransformMatchingShapes(labelS_1.copy(), eqJ_2)
      )
      self.remove(eqJ_1, eqJ_2)
      self.play(Transform(eqJ_2, eqJ_3))
      self.wait(1.5)
      self.play(Uncreate(D1), Uncreate(vX_1), Uncreate(vS_1), Uncreate(vS_2), Unwrite(text),
                Unwrite(labelX_1), Unwrite(labelS_1), Unwrite(eqA), Unwrite(eqJ_2), Unwrite(eqJ_3))
      self.remove(D1, vX_1, text, vS_1, vS_2, labelX_1, labelS_1, eqA, eqJ_2, eqJ_3)
      
      quesC = VGroup(
            Text("Persamaan Kuadrat ?", font_size=30, color=TEAL),
            Text("Pertidaksamaan Linear ?", font_size=30, color=TEAL),
            Text("Pertidaksamaan Kuadrat ?", font_size=30, color=TEAL)
        )
      quesC.arrange(DOWN)
      textC = Text("masih terbatas pada 1 variabel (x)", font_size=20).shift(DOWN*2)
      self.play(FadeIn(quesC, run_time=2))
      self.play(Write(textC))
      self.wait(1.5)
