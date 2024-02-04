%%manim -qm -v WARNING TestF
config.media_width = "100%"

# Coding ini dijalankan melalui website Google Colab

def Prolog(Scene):
    defi = VGroup(
        Text("Aljabar adalah suatu bentuk matematika yang disajikan dengan memuat",
          t2c={'Aljabar':GREEN},
          disable_ligatures=True,
          font_size=24),
        Text("huruf-huruf untuk mewakili bilangan yang belum diketahui.",
             font_size=24)
        ).arrange(DOWN)
    Scene.play(Write(defi), run_time=2)
    Scene.wait(1.5)
    Scene.play(FadeOut(defi), run_time=0.5)

def Orientasi(Scene):
    contoh = MathTex(r"2x^2 + 7x + 3")
    contoh.save_state()
    Scene.play(Write(contoh[0][5]))
    Scene.wait(2)
    Scene.play(FadeIn(contoh[0][:5]), FadeIn(contoh[0][6:]))

    b = Brace(mobject=contoh[0][:3], direction=DOWN, buff=0.2)
    b_text = Text("Suku", font_size=20).next_to(b, DOWN)
    a1 = Arrow(DOWN, UP, tip_length=0.2).next_to(contoh[0][4], UP*0.1).scale(0.5)
    a2 = Arrow(UP, DOWN, tip_length=0.2).next_to(contoh[0][5], DOWN*0.1).scale(0.5)
    a3 = Arrow(DOWN, RIGHT, tip_length=0.15).next_to(contoh[0][7], UP*0.1+RIGHT*0.1).scale(0.5)
    a1_t = Text("Koefisien", font_size=20).next_to(a1, UP)
    a2_t = Text("Variabel", font_size=20).next_to(a2, DOWN)
    a3_t = Text("Konstanta", font_size=20).next_to(a3, UP)

    Scene.play(GrowFromCenter(b), FadeIn(b_text))
    contoh[0][1:3].set_color(BLUE)
    contoh[0][5].set_color(BLUE)
    Scene.play(
        Create(a1),
        Create(a2),
        Create(a3),
        Write(a1_t, run_time=2),
        Write(a2_t, run_time=2),
        Write(a3_t, run_time=2)
    )
    Scene.play(Indicate(contoh[0][0]), Indicate(b_text))
    Scene.play(Indicate(contoh[0][4]), Indicate(a1_t))
    Scene.play(Indicate(contoh[0][5]), Indicate(a2_t))
    Scene.play(Indicate(contoh[0][7]), Indicate(a3_t))

    Scene.wait(2.5)
    Scene.play(
        Restore(contoh),
        FadeOut(b),
        FadeOut(b_text),
        FadeOut(a1),
        FadeOut(a2),
        FadeOut(a3),
        FadeOut(a1_t),
        FadeOut(a2_t),
        FadeOut(a3_t),
    )
    Scene.remove(b, b_text, a1, a2, a3, a1_t, a2_t, a3_t)
    Scene.wait(1.5)
    Scene.remove(contoh)

def OperasiTK(Scene):
    Pers = MathTex(r"2x^2 + 7x + 3")
    PersMain = Pers.copy()
    line = Line(start=[-1.5,-0.5,0], end=[1.5,-0.5,0]);
    symbol = Text("+", font_size=28).next_to(line, RIGHT)
    operate = VGroup(
        Text("Penjumlahan", weight=BOLD, font_size=30),
        Text("Aljabar", weight=BOLD, font_size=30),
        ).arrange(DOWN).shift(LEFT*4)
    result = MathTex(r"6x^2 + 14x - 2").shift(DOWN)

    Scene.add(Pers)
    Scene.play(PersMain.animate.shift(UP*0.75))
    Scene.play(
        Transform(Pers, MathTex(r"4x^2 + 7x - 5")),
        Create(line),
        Write(symbol),
        Write(operate)
    )
    Scene.wait()
    Scene.play(Write(result), reverse=True)
    Scene.wait(2)
    Scene.play(FadeOut(result))
    Scene.remove(result)

    results = MathTex(r"-2x^2 + 8").shift(DOWN)
    Scene.play(
        Transform(symbol, MathTex(r"-", font_size=28).next_to(line, RIGHT)),
        Transform(operate[0], Text("Pengurangan", weight=BOLD, font_size=30).next_to(operate[1], UP))
    )
    Scene.wait()
    Scene.play(Write(results), reverse=True)
    Scene.wait(2)
    Scene.remove(Pers, PersMain, line, symbol, operate, results)

def OperasiKB(Scene):
    Scene.wait()

    Pers = MathTex(r"(2x + 1) \times (x + 4)")
    a = Arrow(DOWN, UP, tip_length=0.15).shift(UP*0.75+RIGHT*0.15).scale(0.5)
    a_t = Text("simbol perkalian", slant=ITALIC, font_size=20).next_to(a, UP)
    Scene.play(FadeIn(Pers), run_time=2)
    Scene.play(Create(a), Write(a_t))
    Scene.wait(2)

    Scene.play(Transform(Pers, MathTex(r"(2x + 1) \cdot (x + 4)"), run_time=0.5))
    Scene.play(
        Transform(Pers, MathTex(r"(2x + 1)(x + 4)"), run_time=0.5),
        Transform(a_t, Text("tanpa simbol", slant=ITALIC, font_size=20).next_to(a, UP))
    )
    Scene.wait()
    Scene.play(
        FadeOut(a, run_time=0.5),
        FadeOut(a_t, run_time=0.5),
        Pers.animate.shift(UP)
    )
    Scene.remove(a, a_t)
    Scene.wait()

    result = VGroup(
        MathTex(r"= 2x^2 + 8x + x + 4"),
        MathTex(r"= 2x^2 + 9x + 4"),
    ).arrange(DOWN, aligned_edge=LEFT)
    Scene.play(
        Write(result[0][0][:4]),
        Indicate(Pers[0][1:4], run_time=1.5),
        Indicate(Pers[0][8], run_time=1.5)
    )
    Scene.play(
        Write(result[0][0][4:7]),
        Indicate(Pers[0][1:4], run_time=1.5),
        Indicate(Pers[0][10], run_time=1.5)
    )
    Scene.play(
        Write(result[0][0][7:9]),
        Indicate(Pers[0][5], run_time=1.5),
        Indicate(Pers[0][8], run_time=1.5)
    )
    Scene.play(
        Write(result[0][0][9:]),
        Indicate(Pers[0][5], run_time=1.5),
        Indicate(Pers[0][10], run_time=1.5)
    )
    Scene.play(FadeIn(result[1]))
    Scene.wait()

    Scene.play(
        FadeOut(Pers, run_time=0.5),
        FadeOut(result[0], run_time=0.5)
    )
    Scene.remove(Pers, result[0], result[1])

    PersMain = result[1][0][1:].copy()
    lineH = Line(start=[-1.75,2.25,0], end=[1.5,2.25,0]);
    lineV = Line(start=[-1.75,2.25,0], end=[-1.75,1,0]);
    Divider = MathTex(r"x + 5").next_to(lineV, LEFT)
    result = MathTex(r"2x - 1", color=BLUE).shift(UP*2.75+LEFT*0.75)
    Scene.play(PersMain.animate.shift(UP*2))
    Scene.play(
        Create(lineH),
        Create(lineV),
        FadeIn(Divider, run_time=2)
    )
    Scene.play(
        Circumscribe(Divider[0][0]),
        Circumscribe(PersMain[:3]),
        FadeIn(result[0][:2], run_time=1.5)
    )

    div1 = Divider.copy()
    div2 = Divider.copy()
    subtr_op1 = VGroup(
        Line(start=[-1.1,0,0], end=[2,0,0], color=ORANGE),
        MathTex("-", color=ORANGE, font_size=28)
    ).arrange(RIGHT).shift(UP*0.5)
    subtr_op2 = VGroup(
        Line(start=[-1.1,0,0], end=[2,0,0], color=ORANGE),
        MathTex("-", color=ORANGE, font_size=28)
    ).arrange(RIGHT).shift(DOWN)
    div_r1 = MathTex(r"0", "- x + 4").shift(LEFT*0.2)
    div_r2 = MathTex(r"9").shift(DOWN*1.5+RIGHT*0.75)
    Scene.play(
        Transform(div1, MathTex(r"2x^2 + 10x").shift(UP+LEFT*0.5)),
        Create(subtr_op1[0], run_time=2),
        Write(subtr_op1[1], run_time=2)
    )
    Scene.play(FadeIn(div_r1, shift=DOWN))
    Scene.play(FadeOut(div_r1[0], run_time=1.5))
    Scene.remove(div_r1[0])
    Scene.play(
        Circumscribe(Divider[0][0]),
        Circumscribe(div_r1[1][:2]),
        FadeIn(result[0][2:], run_time=1.5)
    )
    Scene.play(
        Transform(div2, MathTex(r"- x - 5").shift(DOWN*0.5)),
        Create(subtr_op2[0], run_time=2),
        Write(subtr_op2[1], run_time=2)
    )
    Scene.play(FadeIn(div_r2, shift=DOWN))
    Scene.wait(2)

    PersFi = MathTex(r"2x^2 + 9x + 4 = (2x - 1)(x + 5) + 9")
    Scene.play(
        FadeOut(PersMain),
        FadeOut(lineH),
        FadeOut(lineV),
        FadeOut(div1),
        FadeOut(div2),
        FadeOut(div_r1[1]),
        FadeOut(subtr_op1),
        FadeOut(subtr_op2)
    )
    Scene.remove(PersMain, lineH, lineV, div1, div2, div_r1[1], subtr_op1, subtr_op2)
    Scene.play(
        Write(PersFi[0][:9], run_time=1.5),
        TransformMatchingShapes(result, PersFi[0][10:14]),
        TransformMatchingShapes(Divider, PersFi[0][16:19]),
        TransformMatchingShapes(div_r2, PersFi[0][21])
    )
    Scene.play(
        FadeIn(PersFi[0][9]),
        FadeIn(PersFi[0][14:16]),
        FadeIn(PersFi[0][19:21]),
        run_time=0.5
    )
    Scene.wait()

class TestF(Scene):
   def construct(self):
      Prolog(self)
      Orientasi(self)
      OperasiTK(self)
      OperasiKB(self)
