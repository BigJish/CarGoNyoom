from pygame import *

init()
clock = time.Clock()
WIN = display.set_mode((500, 300))


class Main:

    def __init__(self):
        self.game = Game()

    def run(self):
        while True:
            for i in event.get():
                if i.type == QUIT:
                    quit()

            self.game.run()

            clock.tick(60)
            display.update()


class Game:

    def __init__(self):
        self.car = Car_go_nyoom()
        self.bg = Background()

    def run(self):
        WIN.fill((100, 160, 230))
        self.bg.draw()
        self.car.draw()
        self.car.move()


class Car_go_nyoom:

    def __init__(self):
        self.image1 = image.load("SophieCar.png").convert_alpha()
        self.image = self.image1
        self.rect = Rect(200, 100, 50, 20)
        self.speed = 1

    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        k = key.get_pressed()

        if k[K_w]:
            self.rect.y -= self.speed
            self.image = transform.rotate(self.image1, 90)

        if k[K_s]:
            self.rect.y += self.speed
            self.image = transform.rotate(self.image1, -90)

        if k[K_a]:
            self.rect.x -= self.speed
            self.image = transform.rotate(self.image1, 180)

        if k[K_d]:
            self.rect.x += self.speed
            self.image = self.image1


class Background:

    def __init__(self):
        pass

    def draw(self):
        draw.rect(WIN, (79, 82, 82), (50, 50, 400, 200), 50)


main = Main()
main.run()
