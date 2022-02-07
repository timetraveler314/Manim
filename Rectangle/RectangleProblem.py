from manimlib import *

class IntroduceSegmentPair(Scene):
    def construct(self):
        # self.play(word.animate.scale(0.8).to_edge(UP,buff=0.4))
        word1 = TexText("让我们来看一个关于长方形的问题", font_size=56)
        self.play(Write(word1))
        #self.play(FadeOut(word, shift=DOWN))
        self.wait(1)
        
        word2 = TexText("下图中每条线段都是水平或者竖直的", font_size=56)
        self.play(ReplacementTransform(word1, word2))
        
        self.wait(1)
        self.play(FadeOut(word2, shift=DOWN))

        rect_scale = 0.7
        _lens = [3, 5, 2]
        _heights = [2, 3, 1]
        lens = list(map(lambda num:num*rect_scale, _lens))
        heights = list(map(lambda num:num*rect_scale, _heights))
        rects = [[] for i in range(3)]
        special_rects = []

        rect_vg = VGroup()
        special_rect_vg = VGroup()
        brace_vg = VGroup()

        temp_x = 0
        temp_y = 0
        for i in range(3):
            for j in range(3):
                rect = Rectangle(
                    width=lens[i],
                    height=heights[j]
                )

                if i == 0 and j == 1:
                    srect = Rectangle(
                        width=lens[i] + lens[i+1],
                        height=heights[j]
                    )
                    srect.set_color(BLUE_C)
                    srect.set_fill(BLUE_C, opacity=0.5)
                    srect.move_to(np.array([temp_x + (lens[i] + lens[i+1]) / 2.0, temp_y - heights[j] / 2.0, 0]))
                    special_rect_vg.add(srect)
                    special_rects.append(srect)
                elif i == 1 and j == 0:
                    srect = Rectangle(
                        width=lens[i],
                        height=heights[j]+heights[j+1]+heights[j+2]
                    )
                    srect.set_color(GREEN_C)
                    srect.set_fill(GREEN_C, opacity=0.5)
                    srect.move_to(np.array([temp_x + lens[i] / 2.0, temp_y - (heights[j]+heights[j+1]+heights[j+2]) / 2.0, 0]))
                    special_rect_vg.add(srect)
                    special_rects.append(srect)
                elif i == 2 and j == 0:
                    srect = Rectangle(
                        width=lens[i],
                        height=heights[j]
                    )
                    srect.set_color(RED_C)
                    srect.set_fill(RED_C, opacity=0.5)
                    srect.move_to(np.array([temp_x + lens[i] / 2.0, temp_y - heights[j] / 2.0, 0]))
                    special_rects.append(srect)
                    special_rect_vg.add(srect)

                rect.move_to(np.array([temp_x + lens[i] / 2.0, temp_y - heights[j] / 2.0, 0]))
                temp_y -= heights[j]

                rect_vg.add(rect)
                rects[i].append(rect)

                if j == 2:
                    temp_y = 0
            temp_x += lens[i]

        for i in range(3):
            brace = BraceLabel(
                obj=rects[0][i],
                text=str(_heights[i]),
                brace_direction=LEFT
            )

            brace_vg.add(brace)
        
        for i in range(3):
            brace = BraceLabel(
                obj=rects[i][0],
                text=str(_lens[i]),
                brace_direction=UP
            )
            
            brace_vg.add(brace)
        
        rect_vg.add(brace_vg)
        #rect_vg.add(special_rect_vg)

        rect_vg.shift(np.array([-3.5, 1.75, 0]))
        special_rect_vg.shift(np.array([-3.5, 1.75, 0]))

        self.play(Write(rect_vg))

        srect1 = special_rects[0].copy()
        srect2 = special_rects[1].copy()
        srect3 = special_rects[2].copy()
        word1 = TexText("这些线段可以像这样把图形划分出许多矩形", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(Write(word1))
        self.wait(1)
        self.play(ShowCreation(srect1))
        self.wait(1)

        self.play(ReplacementTransform(srect1, srect2))

        self.wait(1)

        self.play(ReplacementTransform(srect2, srect3))

        self.wait()

        word2 = TexText("那么是否可以计算出", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word1, word2))

        self.wait(1)

        word1 = TexText(r"所有这些矩形的面积之和 $S$ ？", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word2, word1))

        self.wait(1)

        word2 = TexText(r"（可以暂停思考 \quad 5秒后视频继续）", font_size=50)
        word2.to_edge(UP,buff=0.4)
        self.play(Write(word2))

        self.wait(5)

        self.play(FadeOut(word2))
        self.play(FadeOut(srect3))

        word2 = TexText("问题的关键在于如何确定一个符合要求的矩形", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word1, word2))

        self.wait(1)

        rect_title = TexText("Rectangles")
        segment_title = TexText(r"Segment Pairs: $\left( -, \mid \right)$")
        for mob in rect_title, segment_title:
            mob.to_corner(UP+LEFT)
        segment_title.shift(FRAME_X_RADIUS*RIGHT)
        hline = Line(FRAME_X_RADIUS*LEFT, FRAME_X_RADIUS*RIGHT)
        hline.next_to(rect_title, DOWN)
        hline.to_edge(LEFT, buff = 0)
        vline = Line(FRAME_Y_RADIUS*UP, (FRAME_Y_RADIUS - 1)*DOWN)
        for mob in hline, vline:
            mob.set_color(BLUE_C)

        self.play(FadeIn(special_rects[0]))
        self.play(FadeIn(special_rects[1]))
        rect_vg.add(special_rect_vg)

        word1 = TexText("我们不妨来看矩形的长和宽", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word2, word1))

        self.wait(1)
        
        self.play(
            ShowCreation(VGroup(hline, vline)),
            rect_vg.animate.shift(3 * LEFT).scale(0.6),
        )

        self.play(
            Write(rect_title),
            run_time = 2
        )
        self.wait()
        self.play(Write(segment_title, run_time = 2))
        self.wait()

        # Segment Pairs 2 Start

        segment_height2 = Line(special_rects[2].get_corner(RIGHT+UP), special_rects[2].get_corner(RIGHT+DOWN), color=RED_B)
        segment_width2 = Line(special_rects[2].get_corner(LEFT+DOWN), special_rects[2].get_corner(RIGHT+DOWN), color=RED_B)

        segments_vg2 = VGroup(segment_width2, segment_height2)

        self.play(Write(segments_vg2))

        word2 = TexText("容易知道，在这个图形中给定了一个矩形", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word1, word2))

        self.wait()

        word1 = TexText("我们都可以确定其长和宽在侧边上对应的线段对", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word2, word1))


        segment_box2 = RoundedRectangle(width=2, height=1.5).shift(2*RIGHT + 1*UP)
        segment_tex2 = Tex(r"\left( \quad , \quad \right)")
        segment_tex2.move_to(segment_box2.get_center())

        self.play(segment_width2.animate.move_to((rects[2][2].get_corner(LEFT+DOWN) + rects[2][2].get_corner(RIGHT+DOWN)) / 2.0))

        segment_width2.save_state()
        segment_height2.save_state()

        self.play(
            ShowCreation(segment_box2),
            ShowCreation(segment_tex2), 
            segments_vg2.animate.move_to(segment_box2.get_center()).scale(0.5),
            play_time=2
        )

        self.play(
            segment_height2.animate.shift(0.20*RIGHT + 0.4 * DOWN),
            segment_width2.animate.shift(0.36*LEFT + 0.6 * UP)
        )

        segment_box_arrow2 = Arrow(
            start=special_rects[2].get_center(),
            end=segment_tex2.get_corner(LEFT+DOWN),
            color=RED_B,
            thickness=3,
            tip_width_ratio=5,
            tip_angle=PI / 2.
        )

        segment_box_arrow2.set_color(RED_B)

        self.play(Write(segment_box_arrow2), play_time=2)

        # Segment Pairs 2 End

        # Segment Pairs 1 Start

        segment_height1 = Line(special_rects[1].get_corner(RIGHT+UP), special_rects[1].get_corner(RIGHT+DOWN), color=GREEN_B)
        segment_width1 = Line(special_rects[1].get_corner(LEFT+DOWN), special_rects[1].get_corner(RIGHT+DOWN), color=GREEN_B)

        segments_vg1 = VGroup(segment_width1, segment_height1)

        self.play(Write(segments_vg1))

        self.wait()

        segment_box1 = RoundedRectangle(width=2, height=1.5).shift(3*RIGHT + 1*DOWN)
        segment_tex1 = Tex(r"\left( \quad , \quad \right)")
        segment_tex1.move_to(segment_box1.get_center())

        #self.play(segment_width1.animate.move_to((rects[0][2].get_corner(LEFT+DOWN) + rects[1][2].get_corner(RIGHT+DOWN)) / 2.0))
        self.play(segment_width1.animate.move_to((rects[2][0].get_corner(RIGHT+UP) + rects[2][2].get_corner(RIGHT+DOWN)) / 2.0))

        segment_width1.save_state()
        segment_height1.save_state()

        self.play(
            ShowCreation(segment_box1),
            ShowCreation(segment_tex1), 
            segments_vg1.animate.move_to(segment_box1.get_center()).scale(0.25),
            play_time=2
        )

        self.play(
            segment_height1.animate.shift(0.4*RIGHT),
            segment_width1.animate.shift(0.25*LEFT + 0.05 * UP)
        )

        segment_box_arrow1 = Arrow(
            start=special_rects[1].get_center(),
            end=segment_tex1.get_corner(LEFT+UP),
            color=GREEN_B,
            thickness=3,
            tip_width_ratio=5,
            tip_angle=PI / 2.
        )

        segment_box_arrow1.set_color(GREEN_B)

        self.play(Write(segment_box_arrow1), play_time=2)

        self.wait()

        # Segment Pairs 2 Start

        segment_height0 = Line(special_rects[0].get_corner(RIGHT+UP), special_rects[0].get_corner(RIGHT+DOWN), color=BLUE_B)
        segment_width0 = Line(special_rects[0].get_corner(LEFT+DOWN), special_rects[0].get_corner(RIGHT+DOWN), color=BLUE_B)

        segments_vg0 = VGroup(segment_width0, segment_height0)

        self.play(Write(segments_vg0))

        self.wait()

        segment_box0 = RoundedRectangle(width=2, height=1.5).shift(5*RIGHT + 1*UP)
        segment_tex0 = Tex(r"\left( \quad , \quad \right)")
        segment_tex0.move_to(segment_box0.get_center())

        self.play(segment_width0.animate.move_to((rects[0][2].get_corner(LEFT+DOWN) + rects[1][2].get_corner(RIGHT+DOWN)) / 2.0))
        self.play(segment_height0.animate.move_to((rects[2][1].get_corner(RIGHT+UP) + rects[2][1].get_corner(RIGHT+DOWN)) / 2.0))

        segment_width0.save_state()
        segment_height0.save_state()

        self.play(
            ShowCreation(segment_box0),
            ShowCreation(segment_tex0), 
            segments_vg0.animate.move_to(segment_box0.get_center()).scale(0.25),
            play_time=2
        )

        self.play(
            segment_height0.animate.shift(0*LEFT),
            segment_width0.animate.shift(0.25*LEFT + 0.25 * UP)
        )

        segment_box_arrow0 = Arrow(
            start=special_rects[0].get_center(),
            end=segment_tex0.get_corner(LEFT+UP),
            color=BLUE_B,
            thickness=3,
            tip_width_ratio=5,
            tip_angle=PI / 2.
        )

        segment_box_arrow0.set_color(BLUE_B)

        self.play(Write(segment_box_arrow0), play_time=2)

        self.wait()

        tex_etc = Tex(r"\cdots").shift(5 * RIGHT + 2*DOWN)
        self.play(Write(tex_etc))

        self.wait()

        word2 = TexText("同样也不难看出", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word1, word2))

        self.wait()

        word1 = TexText(r"这样的每一个线段对\,唯一对应一个长方形", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(ReplacementTransform(word2, word1))

        self.play(
            FadeOut(special_rects[0]),
            FadeOut(special_rects[1]),
            FadeOut(special_rects[2]),
            FadeOut(segment_box_arrow0),
            FadeOut(segment_box_arrow1),
            FadeOut(segment_box_arrow2)
        )

        self.wait()

        self.play(
            segment_width0.animate.restore(),
            segment_height0.animate.restore()
        )

        self.play(
            segment_width0.animate.move_to((special_rects[0].get_corner(LEFT+DOWN) + special_rects[0].get_corner(RIGHT+DOWN)) / 2.0),
            segment_height0.animate.move_to((special_rects[0].get_corner(RIGHT+DOWN) + special_rects[0].get_corner(RIGHT+UP)) / 2.0),
        )

        self.play(Write(special_rects[0]))

        self.wait()

        self.play(FadeOut(special_rects[0]))

        self.play(
            segment_width1.animate.restore(),
            segment_height1.animate.restore()
        )

        self.play(
            segment_width1.animate.move_to((special_rects[1].get_corner(LEFT+DOWN) + special_rects[1].get_corner(RIGHT+DOWN)) / 2.0),
            segment_height1.animate.move_to((special_rects[1].get_corner(RIGHT+DOWN) + special_rects[1].get_corner(RIGHT+UP)) / 2.0),
        )

        self.play(Write(special_rects[1]))

        self.wait()

        self.play(FadeOut(special_rects[1]))

        self.play(
            segment_width2.animate.restore(),
            segment_height2.animate.restore()
        )

        self.play(
            segment_width2.animate.move_to((special_rects[2].get_corner(LEFT+DOWN) + special_rects[2].get_corner(RIGHT+DOWN)) / 2.0),
            segment_height2.animate.move_to((special_rects[2].get_corner(RIGHT+DOWN) + special_rects[2].get_corner(RIGHT+UP)) / 2.0),
        )

        self.play(Write(special_rects[2]))

        self.wait()

        self.play(FadeOut(special_rects[2]))

        segment_vg = VGroup()
        segment_vg.add(segment_box0, segment_box1, segment_box2, segment_tex0, segment_tex1, segment_tex2, segment_width0, segment_width1, segment_width2, segment_height0, segment_height0, segment_height1, segment_height2)

        # ClearUp
        self.play(
            FadeOut(special_rect_vg),
            FadeOut(rect_title),
            FadeOut(segment_title),
            FadeOut(VGroup(hline, vline)),

            FadeOut(segment_vg),
            FadeOut(rect_vg),
            FadeOut(tex_etc),

            word1.animate.center()
        )

        self.play(FadeOut(word1))

        self.wait()

class Solving(Scene):
    def construct(self):
        word1 = TexText("给出了这些，接下来怎样计算？", font_size=50)
        self.play(Write(word1))
        self.play(word1.animate.to_edge(DOWN,buff=0.4))

        self.wait(1.5)

        word2 = TexText("不妨从面积的式子算起", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2),
            rate_func=exponential_decay
        )

        self.wait(1.5)

        to_isolate = ["a", "b", "x", "y"]
        t2c_map1 = {
                "a": BLUE,
                "b": TEAL,
                "x": YELLOW_C,
                "y": GOLD_C
            }

        lines = VGroup(
            Tex("S=", "a", r"\cdot ", "b"),
            Tex("S", "=", "ax+ay+bx+by", isolate=to_isolate),
            Tex(r"S=  \sum_{i=1}^{n} a_i  \cdot \sum_{i=1}^{m} b_i", isolate=to_isolate),
        )
        lines.arrange(DOWN, buff=MED_LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map(t2c_map1)

        lines[1].shift(0.25*RIGHT)

        new_line0 = Tex(r"S=( a + b ) \cdot ( x + y )", isolate=to_isolate)
        new_line0.set_color_by_tex_to_color_map(t2c_map1)

        play_kw = {"run_time": 2}
        fplay_kw = {"run_time": 0.75}
        self.play(Write(lines[0]))

        word1 = TexText("这是对于单独一个长方形的表达", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.wait(1.5)

        word2 = TexText("如果我们想同时算多个，还能找到起作用的式子吗？", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait(2)

        word1 = TexText("或许可以想一想多项式乘法", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.wait(1.5)

        word2 = TexText(r"把面积式子中长与宽写入多个 $\dots$", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait(1.5)

        new_line0.to_edge(UP,buff=LARGE_BUFF)

        self.play(
            TransformMatchingTex(
                lines[0], new_line0,
                transform_mismatches=True
            ),
            **fplay_kw
        )
        self.wait(1.5)

        lines.to_edge(UP,buff=LARGE_BUFF)

        word1 = TexText("逐项展开这个积", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.wait(1.5)

        # Rect_AX

        rect_ax_vg = VGroup()
        rect_ax = Rectangle(
            width=1,
            height=0.75
        )
        
        rect_ax.set_color_by_gradient((BLUE, YELLOW))

        rect_ax_tex = Tex("ax", isolate=to_isolate)
        rect_ax_tex.set_color_by_tex_to_color_map(t2c_map1)

        rect_ax.move_to(5*LEFT+1.5*DOWN)

        rect_ax_vg.add(rect_ax)

        brace_ax_a = BraceLabel(
            obj=rect_ax,
            text="",
            brace_direction=UP
        )
        brace_ax_x = BraceLabel(
            obj=rect_ax,
            text="",
            brace_direction=RIGHT
        )

        a_copy = new_line0[1].copy()
        x_copy = new_line0[5].copy()

        rect_ax_vg.add(brace_ax_a)
        rect_ax_vg.add(brace_ax_x)
        rect_ax_vg.add(a_copy, x_copy, rect_ax_tex)

        self.play(
            a_copy.animate.next_to(brace_ax_a, UP),
            x_copy.animate.next_to(brace_ax_x, RIGHT),
            Write(brace_ax_a),
            Write(brace_ax_x),
        )

        rect_ax_tex.move_to(rect_ax.get_center())

        self.play(ShowCreation(rect_ax), Write(rect_ax_tex))

        rect_ax_tex_copy = rect_ax_tex.copy()

        self.play(
            FadeIn(lines[1][1]), # =
            FadeIn(lines[1][4]), # +
            ReplacementTransform(
                rect_ax_tex_copy[0], lines[1][2], # a
            ),
            ReplacementTransform(
                rect_ax_tex_copy[1], lines[1][3], # x
            ),
            **fplay_kw
        )

        ''' AY '''

        rect_ay_vg = VGroup()
        rect_ay = Rectangle(
            width=1,
            height=0.5
        )

        rect_ay.set_color_by_gradient((BLUE, GOLD))

        rect_ay_tex = Tex("ay", isolate=to_isolate)
        rect_ay_tex.set_color_by_tex_to_color_map(t2c_map1)

        rect_ay.move_to(2.5*LEFT+1.5*DOWN)

        rect_ay_vg.add(rect_ay)

        brace_ay_a = BraceLabel(
            obj=rect_ay,
            text="",
            brace_direction=UP
        )
        brace_ay_y = BraceLabel(
            obj=rect_ay,
            text="",
            brace_direction=RIGHT
        )

        a_copy = new_line0[1].copy()
        y_copy = new_line0[7].copy()

        rect_ay_vg.add(brace_ay_a)
        rect_ay_vg.add(brace_ay_y)
        rect_ay_vg.add(a_copy, y_copy, rect_ay_tex)

        self.play(
            a_copy.animate.next_to(brace_ay_a, UP),
            y_copy.animate.next_to(brace_ay_y, RIGHT),
            Write(brace_ay_a),
            Write(brace_ay_y),
        )

        rect_ay_tex.move_to(rect_ay.get_center())

        self.play(ShowCreation(rect_ay), Write(rect_ay_tex))

        rect_ay_tex_copy = rect_ay_tex.copy()

        self.play(
            FadeIn(lines[1][7]), # +
            ReplacementTransform(
                rect_ay_tex_copy[0], lines[1][5], # a
            ),
            ReplacementTransform(
                rect_ay_tex_copy[1], lines[1][6], # y
            ),
            **fplay_kw
        )


        ''' BX '''

        rect_bx_vg = VGroup()
        rect_bx = Rectangle(
            width=1.5,
            height=0.75
        )

        rect_bx.set_color_by_gradient((TEAL, YELLOW))

        rect_bx_tex = Tex("bx", isolate=to_isolate)
        rect_bx_tex.set_color_by_tex_to_color_map(t2c_map1)

        rect_bx.move_to(1.5*RIGHT+1.5*DOWN)

        rect_bx_vg.add(rect_bx)

        brace_bx_b = BraceLabel(
            obj=rect_bx,
            text="",
            brace_direction=UP
        )
        brace_bx_x = BraceLabel(
            obj=rect_bx,
            text="",
            brace_direction=RIGHT
        )

        b_copy = new_line0[3].copy()
        x_copy = new_line0[5].copy()

        rect_bx_vg.add(brace_bx_b)
        rect_bx_vg.add(brace_bx_x)
        rect_bx_vg.add(b_copy, x_copy, rect_bx_tex)

        self.play(
            b_copy.animate.next_to(brace_bx_b, UP),
            x_copy.animate.next_to(brace_bx_x, RIGHT),
            Write(brace_bx_b),
            Write(brace_bx_x),
        )

        rect_bx_tex.move_to(rect_bx.get_center())

        self.play(ShowCreation(rect_bx), Write(rect_bx_tex))

        rect_bx_tex_copy = rect_bx_tex.copy()

        self.play(
            FadeIn(lines[1][10]), # +
            ReplacementTransform(
                rect_bx_tex_copy[0], lines[1][8], # a
            ),
            ReplacementTransform(
                rect_bx_tex_copy[1], lines[1][9], # x
            ),
            **fplay_kw
        )

        ''' BY '''

        rect_by_vg = VGroup()
        rect_by = Rectangle(
            width=1.5,
            height=0.5
        )

        rect_by.set_color_by_gradient((TEAL, GOLD))

        rect_by_tex = Tex("by", isolate=to_isolate)
        rect_by_tex.set_color_by_tex_to_color_map(t2c_map1)

        rect_by.move_to(4.5*RIGHT+1.5*DOWN)

        rect_by_vg.add(rect_by)

        brace_by_b = BraceLabel(
            obj=rect_by,
            text="",
            brace_direction=UP
        )
        brace_by_y = BraceLabel(
            obj=rect_by,
            text="",
            brace_direction=RIGHT
        )

        b_copy = new_line0[3].copy()
        y_copy = new_line0[7].copy()

        rect_by_vg.add(brace_by_b)
        rect_by_vg.add(brace_by_y)
        rect_by_vg.add(b_copy, y_copy, rect_by_tex)

        self.play(
            b_copy.animate.next_to(brace_by_b, UP),
            y_copy.animate.next_to(brace_by_y, RIGHT),
            Write(brace_by_b),
            Write(brace_by_y),
        )

        rect_by_tex.move_to(rect_by.get_center())

        self.play(ShowCreation(rect_by), Write(rect_by_tex))

        rect_by_tex_copy = rect_by_tex.copy()

        self.play(
            ReplacementTransform(
                rect_by_tex_copy[0], lines[1][11], # a
            ),
            ReplacementTransform(
                rect_by_tex_copy[1], lines[1][12], # x
            ),
            **fplay_kw
        )

        ''' Four Rects finished '''

        word2 = TexText("可以发现，结果正好是全部以第一个括号内的一个变量为长\\\\第二个括号内一个变量为宽的所有长方形面积和", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait(3)

        word1 = TexText("这个想法对于一般的情况也适用", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.wait(1.5)

        word2 = TexText(r"给定 $n$ 条长和 $m$ 条宽，我们给出能组成所有矩形的面积和", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.play(
            Uncreate(rect_ax_vg), Uncreate(rect_bx_vg), Uncreate(rect_ay_vg), Uncreate(rect_by_vg),
            FadeOut(new_line0), FadeOut(lines[1])
        )

        self.play(Write(lines[2]))

        self.wait(3)

        word1 = TexText("回到原问题，基于前面建立的线段对与矩形的关系", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.wait(2)

        word2 = TexText(r"所有矩形 $\Leftrightarrow$ 线段对， \\ 并可利用长、宽方向上每条线段长度的和做乘法计算面积", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait(3)

        word1 = TexText("每个方向上和的计算并不复杂，这里以宽为例", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1),
            FadeOut(lines[2])
        )

        segments = VGroup(
            Line(2*LEFT, 1*LEFT).set_color(BLUE),
            Line(1*LEFT, 0.5*RIGHT).set_color(TEAL),
            Line(0.5*RIGHT, 2*RIGHT).set_color(GREEN)
        )

        segment_braces = VGroup(
            BraceLabel(
                obj=segments[0],
                text="a",
                brace_direction=UP
            ),
            BraceLabel(
                obj=segments[1],
                text="b",
                brace_direction=UP
            ),
            BraceLabel(
                obj=segments[2],
                text="c",
                brace_direction=UP
            )
        )

        segments.add(segment_braces)

        self.play(Write(segments))

        word2 = TexText(r"先来看由一个最基本单位构成的所有线段", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait(1.5)

        to_isolate = ["a", "b", "c", "x", "y", "z"]
        segment_lines = VGroup(
            Tex("L=a+b+c+(a+b)+(b+c)+(a+b+c)", isolate=to_isolate),
            Tex("L=3a+4b+3c", isolate=to_isolate),
            Tex("M=3x+4y+3z", isolate=to_isolate)
        )
        segment_lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        segment_lines.to_edge(UP, buff=LARGE_BUFF)
        
        t2c_map2 = {
                "a": BLUE,
                "b": TEAL,
                "c": GREEN,
                "x": YELLOW,
                "Y": GOLD,
                "z": RED
            }

        for line in segment_lines:
            line.set_color_by_tex_to_color_map(t2c_map2)

        self.play(
            Write(segment_lines[0][0]),
            Write(segment_lines[0][2]),
            Write(segment_lines[0][4]),
            ReplacementTransform(segments[0].copy(), segment_lines[0][1]), # a
            ReplacementTransform(segments[1].copy(), segment_lines[0][3]), # b
            ReplacementTransform(segments[2].copy(), segment_lines[0][5]), # c
        )

        self.wait(1.5)

        word1 = TexText("再考虑由两段基本单位构成的线段", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1),
        )

        temp_line1 = Line(2*LEFT, 0.5*RIGHT).set_color(YELLOW)
        temp_line2 = Line(1*LEFT, 2*RIGHT).set_color(ORANGE)

        self.play(Write(temp_line1))

        self.play(temp_line1.shift(0.5*DOWN))

        self.play(
            Indicate(temp_line1),
            Write(segment_lines[0][6]),
            Write(segment_lines[0][8]),
            Write(segment_lines[0][10]),
            ReplacementTransform(temp_line1, VGroup(segment_lines[0][7], segment_lines[0][9])),
        )

        self.wait()

        self.play(Write(temp_line2))

        self.play(temp_line2.shift(0.5*DOWN))

        self.play(
            Indicate(temp_line2),
            Write(segment_lines[0][12]),
            Write(segment_lines[0][14]),
            ReplacementTransform(temp_line2, VGroup(segment_lines[0][11], segment_lines[0][13])),
        )

        self.wait(1.5)

        temp_line3 = Line(2*LEFT, 2*RIGHT).set_color(RED)

        word2 = TexText(r"最后是全长一段", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait()

        self.play(Write(temp_line3))
        self.play(temp_line3.shift(0.5*DOWN))
        self.play(
            Indicate(temp_line3),
            Write(segment_lines[0][16]),
            Write(segment_lines[0][18]),
            Write(segment_lines[0][20]),
            ReplacementTransform(temp_line3, VGroup(segment_lines[0][15], segment_lines[0][17], segment_lines[0][19])),
        )

        self.wait(1.5)

        word1 = TexText("合并同类项", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word2, word1)
        )

        self.play(
            TransformMatchingTex(
                segment_lines[0].copy(), segment_lines[1],
                transform_mismatches=False
            ),
            **play_kw
        )

        self.wait(2)

        word2 = TexText(r"对于宽方向同理", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.play(
            Write(segment_lines[2]),
            FadeOut(segments)
        )

        self.embed()