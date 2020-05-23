from manimlib.imports import *
import random

def objPath(shift, pathset):
    new_path = []
    for p in pathset:
        new_path.append(np.add(p, [0, shift, 0]))
    pathobj = VMobject().set_points_as_corners(new_path)
    return pathobj


def trace_small_path(path, shift_x, shift_y):
    fig_Path = []
    for p in path:
        fig_Path.append(np.add(np.multiply(p, 0.5), [shift_x, shift_y, 0]))
    fig_Path_obj = VMobject().set_points_as_corners(fig_Path)
    return fig_Path_obj



def interpolate(points):
    def func(xvar):
        ret = 0
        for i in range(0,len(points)):
            prod = points[i][1]
            for j in range(0,len(points)):
                if(i!=j):
                    prod *= (xvar - points[j][0]) / (points[i][0]-points[j][0])
            ret += prod
        return ret
    return func


class MountainAnimation(Scene):
    def construct(self): 

        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)
        fig_2 = fig.copy()
        self.wait()
        self.add(fig)
        self.play(
            FadeIn(fig),
        )
        self.wait()

        self.wait()
        pk = VMobject(color = BLUE).set_points_as_corners([[3,2,0],[4,-2,0],[-4,-2,0]])
        start_pt = [-4,-2,0]
        end_pt = [3,2,0]

        pathset = []
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])
        pathset.append([[-4, -2, 0], [-3, 0, 0], [0, -0.5, 0], [0.5,0.25,0] , [1, 1, 0], [3, 2, 0]])
        pathset.append([[-4, -2, 0], [3, 2, 0]])
        pathset.append([[-4, -2, 0], [-3.5, 0, 0], [-3, -1, 0], [-2.5, 1, 0], [-2, 0.5, 0],
                        [-1.5,1.5,0],[-1,1,0],[-0.5,-1.5,0],[0,1.5,0],[0.5,1,0],[1,1,0],
                        [1.5,1.7,0],[2,1,0],[2.5,1.8,0],[3,2,0]])
        pathset.append([[-4, -2, 0], [-1.4,-0.5,0],[-2.4,0.8,0],[0.65,0.65,0], [3, 2, 0]])




        hill = []

        for paths in pathset :
            hill.append(VMobject(color = BLUE).set_points_as_corners(paths))

        defpath = VMobject(color = BLUE).set_points_as_corners(pathset[0])

        self.add(hill[0])
        self.play(
            ShowCreation(hill[0]),
            run_time = 2,
            rate_func = linear
        )
        self.add(pk)
        self.play(
            ShowCreation(pk),
            run_time = 2,
            rate_func = linear
        )
        self.wait()
        self.play(
            Broadcast(start_pt,big_radius = 0.5, color = YELLOW),
            Broadcast(end_pt,big_radius = 0.5, color = YELLOW)
        )
        hill_num = len(hill)
        for i in range(0,hill_num-1):
            self.play(
                Transform(hill[i],hill[i+1]),
                Broadcast(start_pt, big_radius=0.5, color=YELLOW),
                Broadcast(end_pt, big_radius=0.5, color=YELLOW)
            )
            self.remove(hill[i])
            self.add(hill[i+1])
            self.wait()
        self.play(
            Transform(hill[-1],defpath)
        )
        self.remove(hill[-1])

        self.add(defpath)
        self.add(pk)
        self.wait()
        self.play(
            ApplyMethod(
                fig.move_to,np.add(pathset[0][0],[0,0.35,0])
            )
        )

        def trace_path(mobj, shift, path,rt):
            new_path = []
            for p in path:
                new_path.append(np.add(p, [0, shift, 0]))
            pathobj = VMobject().set_points_as_corners(new_path)
            self.play(
                MoveAlongPath(mobj, pathobj),
                run_time = rt
            )


        trace_path(fig, 0.35, pathset[0],10)


class FirstMonkMove(Scene):
    def construct(self):
        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)


        pk = VMobject(color = BLUE).set_points_as_corners([[3,2,0],[4,-2,0],[-4,-2,0]])
        start_pt = [-4,-2,0]
        end_pt = [3,2,0]


        pathset = [[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]]
        defpath = VMobject(color = BLUE).set_points_as_corners(pathset)

        self.play(ShowCreation(defpath))
        self.play(ShowCreation(pk))

        self.play(
            Broadcast(start_pt,big_radius = 0.5, color = YELLOW),
            Broadcast(end_pt,big_radius = 0.5, color = YELLOW)
        )

        self.play(FadeIn(fig))
        self.play(
            ApplyMethod(
                fig.move_to, np.add(pathset[0], [0, 0.35, 0])
            )
        )

        self.play(
            MoveAlongPath(fig, objPath(0.35, pathset)),
            run_time = 10
        )


class SecondMonkMove(Scene):
    def construct(self):
        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)


        pk = VMobject(color = BLUE).set_points_as_corners([[3,2,0],[4,-2,0],[-4,-2,0]])
        start_pt = [-4,-2,0]
        end_pt = [3,2,0]


        pathset = [[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]]

        pathset_reversed = [[3, 2, 0], [2.5,1,0],[2,1.5,0],[1.5,0.5,0],[0.5,0,0],[0,0.25,0],[-0.5,0.5,0],[-1, 0, 0],[-2, -1, 0], 
                        [-2.5, -0.5, 0], [-3.5, -0.5, 0],[-4, -2, 0]]


        defpath = VMobject(color = BLUE).set_points_as_corners(pathset)

        self.play(ShowCreation(defpath))
        self.play(ShowCreation(pk))

        self.play(
            Broadcast(start_pt,big_radius = 0.5, color = YELLOW),
            Broadcast(end_pt,big_radius = 0.5, color = YELLOW)
        )

        self.play(FadeIn(fig))
        self.play(
            ApplyMethod(
                fig.move_to, np.add(pathset[-1], [0, 0.35, 0])
            )
        )

        self.play(
            MoveAlongPath(fig, objPath(0.35, pathset_reversed)),
            run_time = 10
        )


class SixMountainsOneScene(Scene):


    def construct(self):
        # self.add(NumberPlane())

        fig = []

        for i in range(0,6):
            body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
            head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
            head.move_to(body.get_start() + head.get_center())
            fig.append(VGroup(body, head))
            fig[i].scale(0.5)

        fig[0].move_to(np.array([-6.6, 3, 0])-fig[0].get_center())
        fig[1].move_to(np.array([-2, 3, 0])-fig[1].get_center())
        fig[2].move_to(np.array([2.6, 3, 0])-fig[2].get_center())
        fig[3].move_to(np.array([-6.6, -1, 0])-fig[3].get_center())
        fig[4].move_to(np.array([-2, -1, 0])-fig[4].get_center())
        fig[5].move_to(np.array([2.6, -1, 0])-fig[5].get_center())

        pathset = []
        pathset.append([[-4, -2, 0], [-3, 0, 0], [0, -0.5, 0], [0.5,0.25,0] , [1, 1, 0], [3, 2, 0]])
        pathset.append([[-4, -2, 0], [-3.5, 0, 0], [-3, -1, 0], [-2.5, 1, 0], [-2, 0.5, 0],[-1.5,1.5,0],[-1,1,0],[-0.5,-1.5,0],[0,1.5,0],[0.5,1,0],[1,1,0],[1.5,1.7,0],[2,1,0],[2.5,1.8,0],[3,2,0]])
        pathset.append([[-4, -2, 0], [-1.4,-0.5,0],[-2.4,0.8,0],[0.65,0.65,0], [3, 2, 0]])
        pathset.append([[-4, -2, 0], [3, 2, 0]])
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],[0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])

        curve = []
        pointset = [[-4,-2],[-3,-1],[0,0],[2,0],[3,2]]
        poly = interpolate(pointset)
        x_ = -4
        random.seed = 5
        cnt = 0
        while(1==1):
            rtk = 1
            x_next = x_ + (random.uniform(0,0.5))**rtk
            curve.append(np.array([x_,poly(x_),0]))
            x_ = x_next
            cnt = cnt + 1
            if(x_ > 3):
                curve.append(np.array([3,2,0]))
                break
        pathset.append(curve)


        pk = []
        hill = []
        mountain = []

        for i in range(0,6):
            hill.append(VMobject(color = BLUE).set_points_as_corners(pathset[i]))            
            pk.append(VMobject(color = BLUE).set_points_as_corners([[3,2,0],[4,-2,0],[-4,-2,0]]))
            mountain.append(VGroup(hill[i], pk[i]))

        for i in range(0, len(mountain)):
            mountain[i].scale(0.5)

        mountain[0].move_to(np.array([-4.6111, 2, 0]))
        mountain[1].move_to(np.array([0, 2, 0]))
        mountain[2].move_to(np.array([4.6111, 2, 0]))
        mountain[3].move_to(np.array([-4.6111, -2, 0]))
        mountain[4].move_to(np.array([0, -2, 0]))
        mountain[5].move_to(np.array([4.6111, -2, 0]))
        self.play(
            ShowCreation(mountain[0]),
            ShowCreation(mountain[1]),
            ShowCreation(mountain[2]),
            ShowCreation(mountain[3]),
            ShowCreation(mountain[4]),
            ShowCreation(mountain[5])
        )
        # self.play(ShowCreation(mountain[0]))
        # self.play(ApplyMethod(mountain[0].move_to, np.array([-4.6111, 2, 0]), run_time = 0.5))
        # self.play(ShowCreation(mountain[1]))
        # self.play(ApplyMethod(mountain[1].move_to, np.array([0 , 2, 0]), run_time = 0.5))
        # self.play(ShowCreation(mountain[2]))
        # self.play(ApplyMethod(mountain[2].move_to, np.array([4.6111, 2, 0]), run_time = 0.5))
        # self.play(ShowCreation(mountain[3]))
        # self.play(ApplyMethod(mountain[3].move_to, np.array([-4.6111, -2, 0]), run_time = 0.5))
        # self.play(ShowCreation(mountain[4]))
        # self.play(ApplyMethod(mountain[4].move_to, np.array([0, -2, 0]), run_time = 0.5))
        # self.play(ShowCreation(mountain[5]))
        # self.play(ApplyMethod(mountain[5].move_to, np.array([4.6111, -2, 0]), run_time = 0.5))
        self.play(*[FadeIn(f) for f in fig])

        self.play(
            ApplyMethod(fig[0].move_to, np.array([-6.6, 1.1625, 0])),
            ApplyMethod(fig[1].move_to, np.array([-2, 1.1625, 0])),
            ApplyMethod(fig[2].move_to, np.array([2.6, 1.1625, 0])),
            ApplyMethod(fig[3].move_to, np.array([-6.6, -2.8375, 0])),
            ApplyMethod(fig[4].move_to, np.array([-2, -2.8375, 0])),
            ApplyMethod(fig[5].move_to, np.array([2.6, -2.8375, 0])),
        )

        self.play(
            MoveAlongPath(fig[0], trace_small_path(pathset[0], -4.6111, 2.1625)),
            MoveAlongPath(fig[1], trace_small_path(pathset[1], 0, 2.1625)),
            MoveAlongPath(fig[2], trace_small_path(pathset[2], 4.6111, 2.1625)),
            MoveAlongPath(fig[3], trace_small_path(pathset[3], -4.6111, -1.8375)),
            MoveAlongPath(fig[4], trace_small_path(pathset[4], 0, -1.8375)),
            MoveAlongPath(fig[5], trace_small_path(pathset[5], 4.6111, -1.8375)),
            run_time = 5
        )



        self.wait(3)


class BothMonksMove(Scene):
    def construct(self):
        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)
        fig_2 = fig.copy()


        pk = VMobject(color = BLUE).set_points_as_corners([[3,2,0],[4,-2,0],[-4,-2,0]])
        start_pt = [-4,-2,0]
        end_pt = [3,2,0]


        pathset = [[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]]
        defpath = VMobject(color = BLUE).set_points_as_corners(pathset)
        
        self.play(ShowCreation(defpath))
        self.play(ShowCreation(pk))

        self.play(
            Broadcast(start_pt,big_radius = 0.5, color = YELLOW),
            Broadcast(end_pt,big_radius = 0.5, color = YELLOW)
        )


        self.play(FadeIn(fig))
        self.play(
            ApplyMethod(
                fig.move_to, np.add(pathset[0], [0, 0.35, 0])
            )
        )

        self.play(FadeIn(fig_2))
        self.play(
            ApplyMethod(
                fig_2.move_to, np.add(pathset[-1], [0, 0.35, 0])
            )
        )        

        self.play(
            MoveAlongPath(fig, objPath(0.35, pathset)),
            MoveAlongPath(fig_2, objPath(0.35, list(reversed(pathset)))),
            run_time = 10
        )



        self.wait(5)


class FirstMonkPathAndGraph(Scene):
    def construct(self):
        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)
        self.add(fig)
        self.wait()
        pk = VMobject(color=BLUE).set_points_as_corners([[3, 2, 0], [4, -2, 0], [-4, -2, 0]])
        start_pt = [-4, -2, 0]
        end_pt = [3, 2, 0]

        pathset = []
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])


        defpath = VMobject(color=BLUE).set_points_as_corners(pathset[0])

        self.add(defpath)
        self.add(pk)
        self.wait()

        y_start = np.array([2.5,-1,0])
        y_end = np.array([2.5,3.3,0])
        x_start = np.array([2.5,-1,0])
        x_end = np.array([6.8,-1,0])
        peak_label = TextMobject("Peak").scale(0.5)
        peak_label.move_to(np.array([2.15, 3.2, 0]))
        ground_label = TextMobject("Ground").scale(0.5)
        ground_label.move_to(np.array([2, -0.9, 0]))
        morning_label = TextMobject("8:00 am").scale(0.5)
        morning_label.move_to(np.array([2.9, -1.2, 0]))
        noon_label = TextMobject("12:00pm").scale(0.5)
        noon_label.move_to(np.array([6.5, -1.2, 0]))

        def dist(a,b):
            return np.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )

        total_len = 0
        x_axis = []
        y_axis = []

        x_axis.append(x_start)
        y_axis.append(y_start)

        for i in range(1,len(pathset[0])):
            total_len = total_len + dist(pathset[0][i-1],pathset[0][i])

        # print(total_len)

        x_axis_path = Line(x_start,x_end,color = ORANGE)
        y_axis_path = Line(y_start,y_end,color = ORANGE)

        graph_path =  []
        graph_path.append(x_start)

        for i in range(0,len(pathset[0])-1):
            graph_path.append(
                [graph_path[0][0] + 4 * (i+1) /(len(pathset[0])-1),graph_path[-1][1] + 4 * dist(pathset[0][i],pathset[0][i+1]) / total_len, 0 ]
            )
        #graph_path[-1] = [6.4,2.9,0]
        #print(graph_path)

        self.play(
            ApplyMethod(
                defpath.shift,
                2.5*LEFT
            ),
            ApplyMethod(
                pk.shift,
                2.5*LEFT
            )
        )

        self.wait()

        self.add(x_axis_path)
        self.add(y_axis_path)

        self.play(
            ShowCreation(x_axis_path),
            ShowCreation(y_axis_path)
        )
        self.wait()

        self.play(
            Transform(defpath.copy(),y_axis_path)
        )
        self.play(
            ShowCreation(peak_label),
            ShowCreation(ground_label),
            ShowCreation(morning_label),
            ShowCreation(noon_label)
        )

        self.wait()

        self.play(
            ApplyMethod(
                fig.move_to,np.add(pathset[0][0],[-2.5,0.35,0])
            )
        )

        fig_2 = Dot(x_start,color = GREEN,radius = 0.05)

        def trace_path(mobj, mobj_2, shift, path, path_2, rt):
            new_path = []
            new_path_2 = []
            for p in path:
                new_path.append(np.add(p, [0, shift, 0]))
            for p in path_2:
                new_path_2.append(p)
            pathobj = VMobject().set_points_as_corners(new_path)
            pathobj.shift(2.5*LEFT)
            pathobj_2 = VMobject().set_points_as_corners(new_path_2)
            path = VMobject(color = GREEN).set_points_as_corners([mobj_2.get_center(),mobj_2.get_center()+UP*0.001])
            def update_group(path):
                old_path = path.copy()
                old_path.append_vectorized_mobject(Line(old_path.points[-1], mobj_2.get_center()))
                path.become(old_path)

            self.add(path)
            path.add_updater(update_group)
            self.play(
                MoveAlongPath(mobj, pathobj),
                MoveAlongPath(mobj_2,pathobj_2),
                run_time = rt,
                rate_func = linear
            )




        trace_path(fig, fig_2, 0.35, pathset[0], graph_path, 10)
        self.wait()


class SecondMonkPathAndGraph(Scene):
    def construct(self):
        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)
        self.add(fig)
        self.wait()
        pk = VMobject(color=BLUE).set_points_as_corners([[3, 2, 0], [4, -2, 0], [-4, -2, 0]])
        start_pt = [-4, -2, 0]
        end_pt = [3, 2, 0]

        pathset = []
        pathset.append([[3, 2, 0], [2.5,1,0],[2,1.5,0],[1.5,0.5,0],[0.5,0,0],[0,0.25,0],[-0.5,0.5,0],[-1, 0, 0],[-2, -1, 0], 
                        [-2.5, -0.5, 0], [-3.5, -0.5, 0],[-4, -2, 0]])

        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])
        defpath = VMobject(color=BLUE).set_points_as_corners(pathset[1])

        self.add(defpath)
        self.add(pk)
        self.wait()

        y_start = np.array([2.5,-1,0])
        y_end = np.array([2.5,3,0])
        x_start = np.array([2.5,-1,0])
        x_end = np.array([6.5,-1,0])
        peak_label = TextMobject("Peak").scale(0.5)
        peak_label.move_to(np.array([2.15, 3.2, 0]))
        ground_label = TextMobject("Ground").scale(0.5)
        ground_label.move_to(np.array([2, -0.9, 0]))
        morning_label = TextMobject("8:00 am").scale(0.5)
        morning_label.move_to(np.array([2.9, -1.2, 0]))
        noon_label = TextMobject("12:00pm").scale(0.5)
        noon_label.move_to(np.array([6.5, -1.2, 0]))

        def dist(a,b):
            return np.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )

        total_len = 0
        x_axis = []
        y_axis = []

        x_axis.append(x_start)
        y_axis.append(y_start)

        for i in range(1,len(pathset[0])):
            total_len = total_len + dist(pathset[0][i-1],pathset[0][i])

        # print(total_len)

        x_axis_path = Line(x_start,x_end,color = ORANGE)
        y_axis_path = Line(y_start,y_end,color = ORANGE)

        graph_path =  []
        graph_path.append(y_end)

        for i in range(0,len(pathset[0])-1):
            graph_path.append(
                [graph_path[0][0] + 4 * (i+1) /(len(pathset[0])-1),graph_path[-1][1] - 4 * dist(pathset[0][i],pathset[0][i+1]) / total_len, 0 ]
            )
        #graph_path[-1] = [6.4,2.9,0]
        #print(graph_path)

        self.play(
            ApplyMethod(
                defpath.shift,
                2.5*LEFT
            ),
            ApplyMethod(
                pk.shift,
                2.5*LEFT
            )
        )

        self.wait()

        self.add(x_axis_path)
        self.add(y_axis_path)

        self.play(
            ShowCreation(x_axis_path),
            ShowCreation(y_axis_path)
        )
        self.wait()

        self.play(
            Transform(defpath.copy(),y_axis_path)
        )
        self.play(
            ShowCreation(peak_label),
            ShowCreation(ground_label),
            ShowCreation(morning_label),
            ShowCreation(noon_label)
        )

        self.wait()

        self.play(
            ApplyMethod(
                fig.move_to,np.add(pathset[0][0],[-2.5,0.35,0])
            )
        )

        fig_2 = Dot(x_start,color = GREEN,radius = 0.05)

        def trace_path(mobj, mobj_2, shift, path, path_2, rt, y_axis_path):
            new_path = []
            new_path_2 = []
            for p in path:
                new_path.append(np.add(p, [0, shift, 0]))
            for p in path_2:
                new_path_2.append(p)
            pathobj = VMobject().set_points_as_corners(new_path)
            pathobj.shift(2.5*LEFT)
            pathobj_2 = VMobject().set_points_as_corners(new_path_2)
            path = VMobject(color = GREEN).set_points_as_corners([mobj_2.get_center(),mobj_2.get_center()])
            def update_group(path):
                self.add(y_axis_path)
                old_path = path.copy()
                old_path.append_vectorized_mobject(Line(old_path.points[-1], mobj_2.get_center()))
                path.become(old_path)

            self.add(path)
            path.add_updater(update_group)
            self.play(
                MoveAlongPath(mobj, pathobj),
                MoveAlongPath(mobj_2,pathobj_2),
                run_time = rt,
                rate_func = linear
            )       

        trace_path(fig, fig_2, 0.35, pathset[0], graph_path, 10, y_axis_path)

        # self.add(y_axis_path)  


        self.wait()


class BothMonksPathAndGraph(Scene):
    def construct(self):
        def trace_path(mobj, mobjGraph, mobj_2, mobj_2Graph, shift, path, pathGraph, path_2, path_2Graph, rt):
            new_path_1 = []
            new_path_2 = []
            new_path_1Graph = []
            new_path_2Graph = []
            for p in path:
                new_path_1.append(np.add(p, [0, shift, 0]))
            for p in path_2:
                new_path_2.append(np.add(p, [0, shift, 0]))
            for p in pathGraph:
                new_path_1Graph.append(p)
            for p in path_2Graph:
                new_path_2Graph.append(p)
            pathobj = VMobject().set_points_as_corners(new_path_1)
            pathobj.shift(2.5*LEFT)
            pathobj_2 = VMobject().set_points_as_corners(new_path_2)
            pathobj_2.shift(2.5*LEFT)
            pathobjGraph = VMobject().set_points_as_corners(new_path_1Graph)
            pathobjGraph_2 = VMobject().set_points_as_corners(new_path_2Graph)
            path = VMobject(color = GREEN).set_points_as_corners([mobjGraph.get_center(),mobjGraph.get_center()+UP*0.001])
            path_2 = VMobject(color = GREEN).set_points_as_corners([mobj_2Graph.get_center(),mobj_2Graph.get_center()+UP*0.001])
            def update_group(path):
                old_path = path.copy()
                old_path.append_vectorized_mobject(Line(old_path.points[-1], mobjGraph.get_center()))
                path.become(old_path)
            def update_group_2(path_2):
                self.add(y_axis_path)
                old_path_2 = path_2.copy()
                old_path_2.append_vectorized_mobject(Line(old_path_2.points[-1], mobj_2Graph.get_center()))
                path_2.become(old_path_2)

            self.add(path)
            path.add_updater(update_group)
            self.add(path_2)
            path_2.add_updater(update_group_2)
            self.play(
                MoveAlongPath(mobj, pathobj),
                MoveAlongPath(mobjGraph,pathobjGraph),
                MoveAlongPath(mobj_2, pathobj_2),
                MoveAlongPath(mobj_2Graph,pathobjGraph_2),
                run_time = rt,
                rate_func = linear
            )

        body = Line([0, 0.5, 0], [0, 0, 0], color=ORANGE)
        head = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        head.move_to(body.get_start() + head.get_center())
        fig = VGroup(body, head)
        fig.move_to(fig.get_center() + 4.5 * LEFT)
        fig_2 = fig.copy()

        pk = VMobject(color=BLUE).set_points_as_corners([[3, 2, 0], [4, -2, 0], [-4, -2, 0]])
        start_pt = [-4, -2, 0]
        end_pt = [3, 2, 0]

        pathset = []
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])
        pathset_2 = []
        pathset_2.append([[3, 2, 0],  [2.5,1,0], [2,1.5,0],[1.5,0.5,0],[0.5,0,0], [0,0.25,0],[-0.5,0.5,0],[-1, 0, 0],[-2, -1, 0],[-2.5, -0.5, 0],[-3.5, -0.5, 0],[-4, -2, 0]])
        # print(pathset)
        # print(pathset_2)


        # Here was the curve generator

        defpath = VMobject(color=BLUE).set_points_as_corners(pathset[0])

        self.add(defpath)
        self.add(pk)
        self.wait()

        y_start = np.array([2.5,-1,0])
        y_end = np.array([2.5,3,0])
        x_start = np.array([2.5,-1,0])
        x_end = np.array([6.5,-1,0])
        peak_label = TextMobject("Peak").scale(0.5)
        peak_label.move_to(np.array([2.15, 3.2, 0]))
        ground_label = TextMobject("Ground").scale(0.5)
        ground_label.move_to(np.array([2, -0.9, 0]))
        morning_label = TextMobject("8:00 am").scale(0.5)
        morning_label.move_to(np.array([2.9, -1.2, 0]))
        noon_label = TextMobject("12:00pm").scale(0.5)
        noon_label.move_to(np.array([6.5, -1.2, 0]))


        def dist(a,b):
            return np.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )

        total_len = 0
        # x_axis = []
        # y_axis = []

        # x_axis.append(x_start)
        # y_axis.append(y_start)

        for i in range(1,len(pathset[0])):
            total_len = total_len + dist(pathset[0][i-1],pathset[0][i])

        # print(total_len)

        x_axis_path = Line(x_start,x_end,color = ORANGE)
        y_axis_path = Line(y_start,y_end,color = ORANGE)

        graph_path =  []
        graph_path.append(y_start)

        for i in range(0,len(pathset[0])-1):
            graph_path.append(
                [graph_path[0][0] + 4 * (i+1) /(len(pathset[0])-1),graph_path[-1][1] + 4 * dist(pathset[0][i],pathset[0][i+1]) / total_len, 0 ]
            )

        graph_path[-1] = [6.4,2.9,0]

        graph_path_2 =  []
        graph_path_2.append(y_end)

        for i in range(0,len(pathset_2[0])-1):
            graph_path_2.append(
                [graph_path_2[0][0] + 4 * (i+1) /(len(pathset_2[0])-1),graph_path_2[-1][1] - 4 * dist(pathset_2[0][i],pathset_2[0][i+1]) / total_len, 0 ]
            )



        self.play(
            ApplyMethod(
                defpath.shift,
                2.5*LEFT
            ),
            ApplyMethod(
                pk.shift,
                2.5*LEFT
            )
        )

        self.wait()
        # grid = NumberPlane()
        # self.add(grid)

        self.add(x_axis_path)
        self.add(y_axis_path)

        self.play(
            ShowCreation(x_axis_path),
            ShowCreation(y_axis_path)
        )
        self.wait()

        self.play(
            Transform(defpath.copy(),y_axis_path)
        )
        self.play(
            ShowCreation(peak_label),
            ShowCreation(ground_label),
            ShowCreation(morning_label),
            ShowCreation(noon_label)
        )

        self.wait()

        fig_graph = Dot(x_start,color = GREEN,radius = 0.05)
        fig_graph_2 = Dot(y_end,color = GREEN,radius = 0.05)

        self.play(FadeIn(fig))
        self.play(
            ApplyMethod(
                fig.move_to,np.add(pathset[0][0],[-2.5,0.35,0])
            )
        )

        self.play(FadeIn(fig_2))
        self.play(
            ApplyMethod(
                fig_2.move_to,np.add(pathset[0][-1],[-2.5,0.35,0])
            )
        )

        trace_path(fig, fig_graph, fig_2, fig_graph_2, 0.35, pathset[0], graph_path, pathset_2[0], graph_path_2, 10)
        self.wait()


class Superpositioning(Scene):
    def construct(self):

        pathset = []
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])
        pathset.append([[-4, -2, 0], [-3.5, -0.5, 0], [-2.5, -0.5, 0], [-2, -1, 0], [-1, 0, 0], [-0.5,0.5,0], [0,0.25,0],
                       [0.5,0,0], [1.5,0.5,0], [2,1.5,0], [2.5,1,0] , [3, 2, 0]])


        # self.play(ShowCreation(NumberPlane()))

        y_start = np.array([1, -2,0])
        y_end = np.array([1, 2,0])
        x_start = np.array([1,-2,0])
        x_end = np.array([5, -2,0])
        peak_label = TextMobject("Peak").scale(0.5)
        peak_label.move_to(np.array([.65, 2, 0]))
        ground_label = TextMobject("Ground").scale(0.5)
        ground_label.move_to(np.array([.5, -2, 0]))
        morning_label = TextMobject("8:00 am").scale(0.5)
        morning_label.move_to(np.array([1.4, -2.2, 0]))
        noon_label = TextMobject("12:00pm").scale(0.5)
        noon_label.move_to(np.array([4.7, -2.2, 0]))


        y_start_2 = np.array([-5, -2,0])
        y_end_2 = np.array([-5, 2,0])
        x_start_2 = np.array([-5,-2,0])
        x_end_2 = np.array([-1, -2,0])
        peak_label_2 = TextMobject("Peak").scale(0.5)
        peak_label_2.move_to(np.array([-5.35, 2, 0]))
        ground_label_2 = TextMobject("Ground").scale(0.5)
        ground_label_2.move_to(np.array([-5.5, -2, 0]))
        morning_label_2 = TextMobject("8:00 am").scale(0.5)
        morning_label_2.move_to(np.array([-4.6, -2.2, 0]))
        noon_label_2 = TextMobject("12:00pm").scale(0.5)
        noon_label_2.move_to(np.array([-1.3, -2.2, 0]))


        def dist(a,b):
            return np.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )

        total_len = 0
        x_axis = []
        y_axis = []

        total_len_2 = 0
        x_axis_2 = []
        y_axis_2 = []

        x_axis.append(x_start)
        y_axis.append(y_start)

        x_axis_2.append(x_start_2)
        y_axis_2.append(y_start_2)

        for i in range(1,len(pathset[0])):
            total_len = total_len + dist(pathset[0][i-1],pathset[0][i])

        for i in range(1,len(pathset[1])):
            total_len_2 = total_len_2 + dist(pathset[1][i-1],pathset[1][i])

        x_axis_path = Line(x_start,x_end,color = ORANGE)
        y_axis_path = Line(y_start,y_end,color = ORANGE)

        x_axis_path_2 = Line(x_start_2,x_end_2,color = ORANGE)
        y_axis_path_2 = Line(y_start_2,y_end_2,color = ORANGE)

        graph_path =  []
        graph_path.append(x_start)

        graph_path_2 =  []
        graph_path_2.append(y_end_2)

        for i in range(0,len(pathset[0])-1):
            graph_path.append(
                [graph_path[0][0] + 4 * (i+1) /(len(pathset[0])-1),graph_path[-1][1] + 4 * dist(pathset[0][i],pathset[0][i+1]) / total_len, 0 ]
            )
        graph_path[-1] = [5,2,0]

        for i in range(0,len(pathset[1])-1):
            graph_path_2.append(
                [graph_path_2[0][0] + 4 * (i+1) /(len(pathset[1])-1),graph_path_2[-1][1] - 4 * dist(pathset[1][i],pathset[1][i+1]) / total_len_2, 0 ]
            )
        graph_path_2[-1] = [-1,-2,0]

        self.wait()

        self.add(x_axis_path)
        self.add(y_axis_path)

        self.add(x_axis_path_2)
        self.add(y_axis_path_2)

        self.play(
            ShowCreation(x_axis_path),
            ShowCreation(y_axis_path),
            ShowCreation(x_axis_path_2),
            ShowCreation(y_axis_path_2)
        )
        self.wait()

        self.wait()

        fig = Dot(x_start,color = GREEN,radius = 0.05)
        fig_2 = Dot(x_start_2,color = GREEN,radius = 0.05)

        self.play(
            ShowCreation(peak_label),
            ShowCreation(ground_label),
            ShowCreation(morning_label),
            ShowCreation(noon_label),
            ShowCreation(peak_label_2),
            ShowCreation(ground_label_2),
            ShowCreation(morning_label_2),
            ShowCreation(noon_label_2)
        )


        pathobj = VMobject(color = GREEN).set_points_as_corners(graph_path)
        pathobj_2 = VMobject(color = GREEN).set_points_as_corners(graph_path_2)

        path = VMobject(color = GREEN).set_points_as_corners([fig.get_center(), fig.get_center()+UP*0.001])
        def update_group(path):
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1], fig.get_center()))
            path.become(old_path)

        self.add(path)
        path.add_updater(update_group)

        path_2 = VMobject(color = GREEN).set_points_as_corners([fig_2.get_center(), fig_2.get_center()+DOWN*0.001])
        def update_group_2(path_2):
            self.add(y_axis_path_2)
            old_path_2 = path_2.copy()
            old_path_2.append_vectorized_mobject(Line(old_path_2.points[-1], fig_2.get_center()))
            path_2.become(old_path_2)

        self.add(path_2)
        path_2.add_updater(update_group_2)


        self.play(
            MoveAlongPath(fig, pathobj),
            MoveAlongPath(fig_2, pathobj_2),
            run_time = 10,
            rate_func = linear
        )
        self.remove(path)
        self.remove(path_2)
        self.add(pathobj)
        self.add(pathobj_2)

        self.play(
            ApplyMethod(x_axis_path.shift, 3*LEFT),
            ApplyMethod(x_axis_path_2.shift, 3*RIGHT),
            ApplyMethod(y_axis_path.shift, 3*LEFT),
            ApplyMethod(y_axis_path_2.shift, 3*RIGHT),
            ApplyMethod(pathobj.shift, 3*LEFT),
            ApplyMethod(pathobj_2.shift, 3*RIGHT),
            ApplyMethod(fig.shift, 3*LEFT),
            ApplyMethod(fig_2.shift, 3*RIGHT),
            ApplyMethod(peak_label.shift, 3*LEFT),
            ApplyMethod(peak_label_2.shift, 3*RIGHT),
            ApplyMethod(ground_label.shift, 3*LEFT),
            ApplyMethod(ground_label_2.shift, 3*RIGHT),
            ApplyMethod(morning_label.shift, 3*LEFT),
            ApplyMethod(morning_label_2.shift, 3*RIGHT),
            ApplyMethod(noon_label.shift, 3*LEFT),
            ApplyMethod(noon_label_2.shift, 3*RIGHT)

        )

        self.wait()

# class ProblemStatement(Scene):
#     def construct(self):
        # statement = TextMobject("""একজন সাধুবাবা পাহাড়ে উঠবে। সে সকাল ৮ টায় যাত্রা শুরু করে এবং দুপুর ১২ টায় পাহাড়ের চূড়ায় পৌছায়। 
        #     সে রাতটুকু পাহাড়ে কাটায়। পরেরদিন সকালে সে সকাল ৮ টায় চূড়া থেকে যাত্রা শুরু করে দুপুর ১২ টায় পাদদেশে পৌছায়।
        #     প্রমাণ কর যে সকাল ৮ টা থেকে দুপুর ১২ টার মধ্যে এমন একটি সময় আছে যখন সাধুবাবা উভয়দিনই পাহাড়ের একই স্থানে অবস্থান করেছিলেন""")
