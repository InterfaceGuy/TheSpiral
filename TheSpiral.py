import importlib
import DreamTalk.imports
importlib.reload(DreamTalk.imports)
from DreamTalk.imports import *

class CyclicalAndLinearMakeSpiral(ThreeDScene):

    def construct(self):
        circle = Circle(radius=0, creation=True, plane="xy", color=WHITE, arrow_end=True)
        line = Arrow((0,0,0), (0,0,0), creation=True, color=BLUE)
        spiral = Helix(start_radius=0, start_angle=0, end_radius=100, end_angle=8*PI, radial_bias=0.3, height=200, height_bias=0.3, plane="xz", y=-100, arrow_end=True, creation=True)
        self.camera.move_orbit(direction="front")

        self.play(circle.change_radius(radius=50), circle.move(x=-150), run_time=2)
        self.wait()
        self.play(line.move(x=150), line.start_null.move(x=-50, y=-50), line.end_null.move(x=50, y=50), run_time=2)
        self.wait()
        self.play(self.camera.move_orbit(theta=PI/8), circle.move(x=150), line.move(x=-150), circle.rotate(p=-PI/2), line.rotate(b=-PI/2), line.start_null.move(x=-50, y=50), line.end_null.move(x=50, y=-50), run_time=2)
        self.wait()
        self.play(
            Morph(circle, spiral),
            Morph(line.connection.path, spiral),
            run_time=2)
        self.wait()

if __name__ == "__main__":
    cyclical_and_linear_make_spiral = CyclicalAndLinearMakeSpiral()