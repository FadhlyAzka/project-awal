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
      vX_1 = Vector([0.5, 0], color=BLUE)
      labelX_1 = Tex("Posisi", font_size=20).next_to(vX_1, UP)
      self.play(DrawBorderThenFill(D1), run_time=2.5)
      self.play(Create(vX_1), Write(labelX_1))
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
      self.play(
          tracker.animate.set_value(5),
          Transform(vX_1, Vector([2.5, 0], color=BLUE)),
          run_time=3,
      )
      self.play(
          tracker.animate.set_value(-10),
          Transform(vX_1, Vector([-5, 0], color=BLUE)),
          run_time=3,
      )
      self.wait()
