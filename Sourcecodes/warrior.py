from manimlib.imports import *
import random
import numpy as np

class intro(Scene):
    def construct(self):

        #construction of the grid starts

        linex = []
        liney = []
        for i in range(-2,4,1):
            linex.append(Line(np.array([i-0.5,-1.5,0]),np.array([i-0.5,2.5,0]),color=BLUE))
        for i in range(0,6):
            self.add(linex[i])

        for i in range(-1,4,1):
            liney.append(Line(np.array([-2.5,i-0.5,0]),np.array([2.5,i-0.5,0]),color=BLUE))
        for i in range(0,5):
            self.add(liney[i])

        #construction of the grid ends

        #now we show movement of the warrior

        W = TexMobject("W")
        W.shift(DOWN)

        self.play(FadeIn(W))
        self.wait()

        arrow_1 = Arrow(np.array([-0.1,-0.9,0]),np.array([-1.9,0.9,0]))
        arrow_2 = Arrow(np.array([0.1,-0.9,0]),np.array([0.9,1.9,0]))

        self.play(ShowCreation(arrow_1))
        self.play(GrowArrow(arrow_2))

        self.wait()

        #W.move_to(DOWN+2*UP+2*LEFT)
        self.play(ApplyMethod(W.shift,2*UP+2*LEFT))
        self.wait()
        #W.move_to(DOWN)
        self.play(ApplyMethod(W.shift,2*DOWN+2*RIGHT))
        self.wait()
        # W.move_to(DOWN+3*UP+RIGHT)
        self.play(ApplyMethod(W.shift,3*UP+RIGHT))
        self.wait()
        #W.move_to(DOWN)
        self.play(ApplyMethod(W.shift,3*DOWN+LEFT))

        self.wait()

        self.play(FadeOut(arrow_1))
        self.play(FadeOut(arrow_2))
        self.play(FadeOut(W))
        self.wait()

        self.remove(W)
        self.remove(arrow_1)
        self.remove(arrow_2)

class magnify(MovingCameraScene):
    def construct(self):
        rects = []
        c = 0
        VGRa = []

        for i in range(0,25):
            VGRa.append(VGroup())

        for i in range(-25,26):
            for j in range(-25,26):
                rects.append(Rectangle(height=0.5, width=0.5, fill_color=BLACK, fill_opacity=1, color=BLUE))
                rects[c].move_to(0.5*i*UP+0.5*j*RIGHT)
                VGRa[c%25] = VGroup(VGRa[c%25],rects[c])
                c = c + 1

        VGR = VGroup()
        for i in range(0,25):
            VGR = VGroup(VGR,VGRa[i])

        self.add(VGR)
        self.wait()
        self.wait()
        self.wait()

        a = np.zeros((50,50),dtype=np.int)
        dx = [3, 3,-3,-3, 1, 1,-1,-1, 2, 2,-2,-2]
        dy = [1,-1, 1,-1, 3,-3, 3,-3, 2,-2, 2,-2]

        W = []
        c = 0
        for i in range(-22,23):
            for j in range(-22,23):
                if(random.random()<0.7):
                    p=1
                    for k in range(0,12):
                        p = p * (1-a[i+dx[k],j+dy[k]])
                    if(p==1):
                        a[i,j]=1
                        W.append(TexMobject("W"))
                        W[c].scale(0.5)
                        W[c].move_to(0.5*UP+0.5+RIGHT+0.5*i*UP+0.5*j*RIGHT)
                        c+=1
        WG = VGroup(W[0])
        for w in W:
            WG = VGroup(WG,w)

        self.play(FadeIn(WG))
        self.wait()
        self.wait()
        self.play(FadeOut(WG))
        self.wait()

        self.play(
            self.camera_frame.set_width, self.camera_frame.get_width()*0.5
        )
        self.wait()
        self.wait()

        rect2 = []

        c=0

        for i in range(-1,3):
            for j in range(-2,3):
                rect2.append(Rectangle(height=0.5, width=0.5, fill_color=BLACK, fill_opacity=1, color=BLUE))
                rect2[c].move_to(0.5 * i * UP + 0.5 * j * RIGHT)
                c += 1

        for rect in rect2:
            self.add(rect)

        self.wait()

        self.play(FadeOut(VGR))
        self.wait()
        self.wait()

class solution(Scene):
    def construct(self):
        linex = []
        liney = []
        for i in range(-2, 4, 1):
            linex.append(Line(np.array([i - 0.5, -1.5, 0]), np.array([i - 0.5, 2.5, 0]),color=BLUE))
        for i in range(0, 6):
            self.add(linex[i])

        for i in range(-1, 4, 1):
            liney.append(Line(np.array([-2.5, i - 0.5, 0]), np.array([2.5, i - 0.5, 0]),color=BLUE))
        for i in range(0, 5):
            self.add(liney[i])

        W = TexMobject("W")
        count_head = TexMobject("\\text{Count: }")

        n0 = TexMobject("0")
        n1 = TexMobject("1")
        n2 = TexMobject("2")
        n3 = TexMobject("3")
        n4 = TexMobject("4")
        n5 = TexMobject("5")
        n6 = TexMobject("6")
        n7 = TexMobject("7")
        n8 = TexMobject("8")

        count_head.move_to(2*DOWN + 2*LEFT)
        n0.move_to(2 * DOWN + LEFT)
        n1.move_to(2 * DOWN + LEFT)
        n2.move_to(2 * DOWN + LEFT)
        n3.move_to(2 * DOWN + LEFT)
        n4.move_to(2 * DOWN + LEFT)
        n5.move_to(2 * DOWN + LEFT)
        n6.move_to(2 * DOWN + LEFT)
        n7.move_to(2 * DOWN + LEFT)
        n8.move_to(2 * DOWN + LEFT)

        self.play(FadeIn(count_head))
        self.play(FadeIn(n0))

        cycle_1 = []
        for i in range(0,2):
            cycle_1.append(Rectangle(height = 1, width = 1,fill_color="#ff0000", fill_opacity=1, color=BLUE))
        cycle_1[1].move_to(2*LEFT+2*UP)
        for sq in cycle_1:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(2*LEFT+2*UP)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift,2*RIGHT+2*DOWN))
        self.wait()
        self.play(ApplyMethod(W.shift,2*LEFT+2*UP))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n0,n1))
        self.remove(n0)
        self.add(n1)

        cycle_2 = []
        for i in range(0, 2):
            cycle_2.append(Rectangle(height=1, width=1, fill_color="#7a3636", fill_opacity=1, color=BLUE))
        cycle_2[0].move_to(2 * LEFT + DOWN)
        cycle_2[1].move_to(UP)
        for sq in cycle_2:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(UP)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * LEFT + 2 * DOWN))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * RIGHT + 2 * UP))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n1, n2))
        self.remove(n1)
        self.add(n2)

        cycle_3 = []
        for i in range(0, 2):
            cycle_3.append(Rectangle(height=1, width=1, fill_color=GREEN, fill_opacity=1, color=BLUE))
        cycle_3[0].move_to(RIGHT)
        cycle_3[1].move_to(UP+2*LEFT)
        for sq in cycle_3:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(RIGHT)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * LEFT + UP))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * RIGHT + DOWN))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n2, n3))
        self.remove(n2)
        self.add(n3)

        cycle_4 = []
        for i in range(0, 2):
            cycle_4.append(Rectangle(height=1, width=1, fill_color="#fc03d3", fill_opacity=1, color=BLUE))
        cycle_4[0].move_to(UP+RIGHT)
        cycle_4[1].move_to(2 * LEFT)
        for sq in cycle_4:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(2 * LEFT)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * RIGHT + UP))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * LEFT + DOWN))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n3, n4))
        self.remove(n3)
        self.add(n4)

        cycle_5 = []
        for i in range(0, 3):
            cycle_5.append(Rectangle(height=1, width=1, fill_color="#0000ff", fill_opacity=1, color=BLUE))
        cycle_5[0].move_to(UP + LEFT)
        cycle_5[1].move_to(DOWN + RIGHT)
        cycle_5[2].move_to(2 * UP + 2 * RIGHT)
        for sq in cycle_5:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(UP + LEFT)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * RIGHT + 2 * DOWN))
        self.wait()
        self.play(ApplyMethod(W.shift, RIGHT + 3 * UP))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * LEFT + DOWN))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n4, n5))
        self.remove(n4)
        self.add(n5)

        cycle_6 = []
        for i in range(0, 3):
            cycle_6.append(Rectangle(height=1, width=1, fill_color="#fca503", fill_opacity=1, color=BLUE))
        cycle_6[0].move_to(LEFT)
        cycle_6[1].move_to(2 * UP + RIGHT)
        cycle_6[2].move_to(DOWN + 2 * RIGHT)
        for sq in cycle_6:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(LEFT)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * RIGHT + 2 * UP))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * DOWN + RIGHT))
        self.wait()
        self.play(ApplyMethod(W.shift, UP + 3 * LEFT))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n5, n6))
        self.remove(n5)
        self.add(n6)

        cycle_7 = []
        for i in range(0, 3):
            cycle_7.append(Rectangle(height=1, width=1, fill_color="#0b753c", fill_opacity=1, color=BLUE))
        cycle_7[0].move_to(DOWN)
        cycle_7[1].move_to(UP + 2 * RIGHT)
        cycle_7[2].move_to(2 * UP + LEFT)
        for sq in cycle_7:
            self.play(FadeIn(sq))
        self.wait()
        self.add(W)
        W.move_to(DOWN)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * RIGHT + 2 * UP))
        self.wait()
        self.play(ApplyMethod(W.shift, UP + 3 * LEFT))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * DOWN + RIGHT))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n6, n7))
        self.remove(n6)
        self.add(n7)

        self.wait()
        self.add(W)
        W.move_to(DOWN+LEFT)
        self.play(FadeIn(W))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * RIGHT + UP))
        self.wait()
        self.play(ApplyMethod(W.shift, 2 * UP + 2 * LEFT))
        self.wait()
        self.play(ApplyMethod(W.shift, 3 * DOWN + LEFT))
        self.wait()
        self.play(FadeOut(W))
        self.wait()
        self.remove(W)

        self.play(Transform(n7, n8))
        self.remove(n7)
        self.add(n8)

class text(Scene):
    def construct(self):
        line_1_1 = TextMobject("In any ")
        line_1_2 = TexMobject("5\\times 4")
        line_1_3 = TextMobject("অংশে আমরা সর্বোচ্চ ")
        line_1_4 = TexMobject("8")
        line_1_5 = TextMobject("টা যোদ্ধা রাখতে পারি,")
        #line_2 = TexMobject("\\text{আবার, }2020 = 5\\times 404 = 4\\times 505,")
        #line_3 = TexMobject("\\text{যেহেতু }2020\\times 2020\\text{ বোর্ড কে }4\\times 5\\text{ অংশ দিয়ে টাইল করে ফেলা যায়,}")
        #line_4 = TexMobject("\\text{আমরা পুরো বোর্ডের সর্বোচ্চ }\\frac{8}{5\\times 4}=\\frac{2}{5}\\text{ সংখ্যক ঘরে যোদ্ধা রাখতে পারবো।}")
        #line_1.move_to(2*UP)
        #line_2.move_to(UP)
        #line_4.move_to(DOWN)

        line_1_2.next_to(line_1_1,RIGHT)
        line_1_3.next_to(line_1_2,RIGHT)
        line_1_4.next_to(line_1_3,RIGHT)
        line_1_5.next_to(line_1_4,RIGHT)

        self.play(FadeIn(line_1_1,line_1_2,line_1_3,line_1_4))
        self.wait()
        #self.play(FadeIn(line_2))
        #self.wait()
        #self.play(FadeIn(line_3))
        #self.wait()
        #self.play(FadeIn(line_4))
        #self.wait()

class localtoglobal(MovingCameraScene):
    def construct(self):

        rec = Rectangle(height=4, width=5, fill_color=BLACK, fill_opacity=0, color=BLUE)
        rec.move_to(0.5*UP)
        self.add(rec)

        VG = VGroup()

        cycle_1 = []
        for i in range(0, 2):
            cycle_1.append(Rectangle(height=1, width=1, fill_color="#ff0000", fill_opacity=1, color=BLUE))
        cycle_1[1].move_to(2 * LEFT + 2 * UP)
        for sq in cycle_1:
            VG = VGroup(VG,sq)


        cycle_2 = []
        for i in range(0, 2):
            cycle_2.append(Rectangle(height=1, width=1, fill_color="#7a3636", fill_opacity=1, color=BLUE))
        cycle_2[0].move_to(2 * LEFT + DOWN)
        cycle_2[1].move_to(UP)
        for sq in cycle_2:
            VG = VGroup(VG,sq)

        cycle_3 = []
        for i in range(0, 2):
            cycle_3.append(Rectangle(height=1, width=1, fill_color=GREEN, fill_opacity=1, color=BLUE))
        cycle_3[0].move_to(RIGHT)
        cycle_3[1].move_to(UP + 2 * LEFT)
        for sq in cycle_3:
            VG = VGroup(VG,sq)

        cycle_4 = []
        for i in range(0, 2):
            cycle_4.append(Rectangle(height=1, width=1, fill_color="#fc03d3", fill_opacity=1, color=BLUE))
        cycle_4[0].move_to(UP + RIGHT)
        cycle_4[1].move_to(2 * LEFT)
        for sq in cycle_4:
            VG = VGroup(VG,sq)

        cycle_5 = []
        for i in range(0, 3):
            cycle_5.append(Rectangle(height=1, width=1, fill_color="#0000ff", fill_opacity=1, color=BLUE))
        cycle_5[0].move_to(UP + LEFT)
        cycle_5[1].move_to(DOWN + RIGHT)
        cycle_5[2].move_to(2 * UP + 2 * RIGHT)
        for sq in cycle_5:
            VG = VGroup(VG,sq)

        cycle_6 = []
        for i in range(0, 3):
            cycle_6.append(Rectangle(height=1, width=1, fill_color="#fca503", fill_opacity=1, color=BLUE))
        cycle_6[0].move_to(LEFT)
        cycle_6[1].move_to(2 * UP + RIGHT)
        cycle_6[2].move_to(DOWN + 2 * RIGHT)
        for sq in cycle_6:
            VG = VGroup(VG,sq)

        cycle_7 = []
        for i in range(0, 3):
            cycle_7.append(Rectangle(height=1, width=1, fill_color="#0b753c", fill_opacity=1, color=BLUE))
        cycle_7[0].move_to(DOWN)
        cycle_7[1].move_to(UP + 2 * RIGHT)
        cycle_7[2].move_to(2 * UP + LEFT)
        for sq in cycle_7:
            VG = VGroup(VG,sq)

        self.add(VG)
        self.wait()
        self.play(FadeOut(VG))
        self.wait()

        l1 = TexMobject("\\leq\\frac{8}{5\\times 4}")
        l2 = TexMobject("\\leq\\frac{2}{5}")

        l1.move_to(0.5*UP)
        l1.scale(2.8)
        l2.move_to(0.5*UP)
        l2.scale(3)

        self.play(FadeIn(l1))
        self.wait()
        self.play(Transform(l1,l2))
        self.remove(l1)
        self.add(l2)
        self.wait()
        self.wait()
        VG_2 = []
        VG_2r = []
        for i in range(0,25):
            VG_2.append(VGroup())
            VG_2r.append(VGroup())
        recs = []
        VGC = VGroup()
        lines = []
        c = 0
        for i in range(-25,26,1):
            for j in range(-25,26,1):
                recs.append(Rectangle(height=4, width=5, fill_color=BLACK, fill_opacity=0, color=BLUE))
                lines.append(TexMobject("\\leq\\frac{2}{5}"))
                recs[c].move_to(5*i*RIGHT+4*j*UP+0.5*UP)
                lines[c].move_to(5*i*RIGHT+4*j*UP+0.5*UP)
                lines[c].scale(3)
                if((i==0 or i==1 or i==-1) and (j==0 or j==1 or j==-1)):
                    VGC = VGroup(VGC,recs[c],lines[c])
                VG_2[c%25] = VGroup(VG_2[c%25],recs[c])
                VG_2r[c%25] = VGroup(VG_2r[c%25],lines[c])
                c = c + 1

        VG_3 = VGroup()
        VG_3r = VGroup()

        for i in range(0,25):
            VG_3=VGroup(VG_2[i],VG_3)
            VG_3r=VGroup(VG_2r[i],VG_3r)

        self.play(FadeIn(VGC))

        self.add(VG_3)
        self.add(VG_3r)
        self.remove(VGC)
        self.remove(l2)
        self.wait()
        self.wait()

        l2.scale(10)

        self.play(
            self.camera_frame.set_width, 90
        )
        self.wait()
        self.wait()

        self.play(Transform(VG_3r,l2))
        self.add(l2)
        self.remove(VG_3r)
        self.wait()

class simple(Scene):
    def construct(self):
        rect2 = []
        sc = 1
        c = 0

        for i in range(-1, 3):
            for j in range(-2, 3):
                rect2.append(Rectangle(height=sc, width=sc, fill_color=BLACK, fill_opacity=1, color=BLUE))
                rect2[c].move_to(sc * i * UP + sc * j * RIGHT)
                c += 1

        for rect in rect2:
            self.add(rect)

        self.wait()

        l1 = TexMobject("5\\times 4")
        l2 = TexMobject("20")
        l3 = TexMobject("\\times\\frac{2}{5}")
        l4 = TexMobject("8")

        l1.move_to(4*RIGHT)
        l2.move_to(4*RIGHT)
        l3.move_to(4.62*RIGHT)
        l4.move_to(4.125*RIGHT)

        self.play(FadeIn(l1))
        self.wait()
        self.play(Transform(l1,l2))
        self.remove(l1)
        self.add(l2)
        self.wait()
        self.play(FadeIn(l3))
        self.wait()
        VG = VGroup(l2,l3)
        self.remove(l2,l3)
        self.add(VG)
        self.wait()
        self.play(Transform(VG,l4))
        self.wait()
        self.add(l4)
        self.remove(VG)
        self.wait()


