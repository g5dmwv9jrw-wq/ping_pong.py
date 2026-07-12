from pygame import *

win_width = 700
win_height = 500
back = (100, 250, 150)

window = display.set_mode((win_width, win_height))

display.set_caption('ping + pong')

run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_size_x, player_size_y, player_x, player_y, player_speed_x, player_speed_y ):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys [K_s] and self.rect.y < win_height - 140:
            self.rect.y += self.speed_y
    def update_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys [K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed_y

ball = Player('ball0.png', 50, 50, 200, 200, 10, 5)
player_l = Player('platform.png', 30, 150, 0, 200, 0 ,10)
player_r = Player('platform.png', 30, 150, 670, 200, 0, 10)
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(back)
    ball.reset()
    player_l.reset()
    player_r.reset()
    ball.update_ball()
    player_r.update_r()
    player_l.update_l()

    time.delay(50)
    display.update()
