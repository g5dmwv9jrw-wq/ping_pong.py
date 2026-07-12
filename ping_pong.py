from pygame import *

win_width = 700
win_height = 500
back = (100, 250, 150)

window = display.set_mode((win_width, win_height))

display.set_caption('ping + pong')

score_l = 0
score_r = 0

run = True
finish = False

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER_R LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER_L LOSE!', True, (180, 0, 0))

text_score_l = font1.render('SCORE L:' + str(score_l), True, (0, 0, 180))
text_score_r = font1.render('SCORE R:' + str(score_r), True, (0, 0, 180))
restart = font1.render('Хочешь начать заново - жми ПРОБЕЛ', True, (0, 0, 0))

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
        if self.rect.y > win_height - 50 or self.rect.y < 0:
            self.speed_y *= -1
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys [K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed_y

ball = Player('ball0.png', 50, 50, 200, 200, 10, 10)
player_l = Player('platform.png', 30, 150, 0, 200, 0 ,10)
player_r = Player('platform.png', 30, 150, 670, 200, 0, 10)
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                score_l = 0
                score_r = 0
                text_score_l = font1.render('SCORE L:' + str(score_l), True, (0, 0, 180))
                text_score_r = font1.render('SCORE R:' + str(score_r), True, (0, 0, 180))
                time.delay(1000)
                finish = False
    if not finish:
        window.fill(back)
        ball.reset()
        player_l.reset()
        player_r.reset()
        ball.update_ball()
        player_r.update_r()
        player_l.update_l()
        if sprite.collide_rect(player_r, ball) or sprite.collide_rect(player_l, ball):
            ball.speed_x *= -1
        if ball.rect.x < 0:
            score_r += 1
            text_score_r = font1.render('SCORE R:' + str(score_r), True, (0, 0, 180))
            
            
            ball.rect.x = 300
            ball.rect.y = 200
            if score_r >= 5:
                window.blit(lose1, (200, 200))
                window.blit(restart, (150, 450))
                finish = True



        if ball.rect.x > 700:
            score_l += 1
            text_score_l = font1.render('SCORE L:' + str(score_l), True, (0, 0, 180))
            
            
            
            ball.rect.x = 300
            ball.rect.y = 200
            if score_l >= 5:
                window.blit(lose2, (200, 200))
                window.blit(restart, (150, 450))
                finish = True
        window.blit(text_score_r, (540, 20))
        window.blit(text_score_l, (40, 20))
            
    time.delay(50)
    display.update()
