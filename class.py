# 1 task
class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        rectangle_area = self.lenght * self.width
        print("Rectangle area:", rectangle_area)

my_rectangle = Rectangle(8, 3)
my_rectangle.area()

# 2 task
class Rocket:
    def __init__(self):
        self.x=0
        self.y=0

    def move_up(self):
        self.y += 1
    def move_right(self):
        self.x += 1
    def mode_down(self):
        self.y -= 1
    def move_left(self):
        self.x -= 1

    def current_position(self):
        print("Current position:", self.x, self.y)

rocket_1 = Rocket()
rocket_1.move_up()
rocket_1.move_right()
rocket_1.mode_down()
rocket_1.move_left()
rocket_1.current_position()

rocket_1.move_up()
rocket_1.move_right()
rocket_1.current_position()

rocket_1.move_up()
rocket_1.move_right()
rocket_1.move_up()
rocket_1.move_right()
rocket_1.current_position()

