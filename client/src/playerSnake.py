import snake
import math
import pygame


class playerSnake(snake.snake):
    """
    [summary] 
    """

    REGULAR_SPEED = 0.7
    BOOST_SPEED = 5

    MAX_ANGLE_CHANGE = math.radians(3)

    def __init__(self, location, name):
        super(playerSnake, self).__init__(location, name)

        self.regular_speed = playerSnake.REGULAR_SPEED
        self.boost_speed = playerSnake.BOOST_SPEED
        self.current_speed = self.regular_speed

    def move(self):
        self.head.move(self.current_speed)
        pre_location = self.head.get_location()
        for sector in self.tail:
            sector.relocate(pre_location)
            pre_location = sector.get_location()
    
    def set_angle(self, angle, limit=None):
        if limit:
            if abs(self.get_angle() - angle) > math.pi:
                dir_control = -1
            else:
                dir_control = 1

            if self.get_angle() < angle:
                new_angle = self.get_angle() + limit * dir_control
                new_angle += math.pi
                new_angle %= 2 * math.pi
                new_angle -= math.pi
                self.head.angle = new_angle
            else:
                new_angle = self.get_angle() - limit * dir_control
                new_angle += math.pi
                new_angle %= 2 * math.pi
                new_angle -= math.pi
                self.head.angle = new_angle
        else: 
            self.head.angle = angle

    def direct_to(self, location):
        self_x, self_y = self.get_location()
        loc_x, loc_y = location

        dx = loc_x - self_x
        dy = loc_y - self_y
        self.set_angle(math.atan2(dy, dx))
