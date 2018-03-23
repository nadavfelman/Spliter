    def move(self, speed):
        self_x, self_y = self.get_location()

        new_x = self_x + speed * math.cos(self.angle)
        new_y = self_y + speed * math.sin(self.angle)
        self.set_location((new_x, new_y))