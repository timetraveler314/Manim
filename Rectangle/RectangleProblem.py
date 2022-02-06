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

        word2 = TexText("给出了这些，接下来怎样计算？", font_size=50)
        word2.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        word1 = TexText("给出了这些，接下来怎样计算？", font_size=50)
        word1.to_edge(DOWN,buff=0.4)
        self.play(
            ReplacementTransform(word1, word2)
        )

        self.wait()

class IntroduceSegmentPair(Scene):
    def construct(self):