from pygame import *
from random import randint
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space shooter")
fire_sound = mixer.Sound("fire.ogg")
background = transform.scale(image.load("galaxy.jpg" (win_width, win_height))
rocket = ('rocket.png')
enemy = ('ufo.png')
bullet=("bullet.png")
font.init()
font2 = font.SysFont('Arial', 37)
win=font2.render("YOU WIN", True, (0,0,255))
lose=font2.render("YOU LOSE", True, (0,255,0))
score = 0
lost = 0
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 80: 
            self.rect.x += self.speed 
    def fire(self):
        pulka = Bullet(bullet, self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(pulka) 
        
class Enemy(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global lost 
        if self.rect.y >= win_height: 
            self.rect.x = randint(80, 620) 
            self.rect.y = -50 
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill() 
bullets=sprite.Group()
 
monsters = sprite.Group() 
for a in range(1, 6): 
    monster = Enemy(enemy, randint(80, 629), -60, 80, 80, randint(1,5) ) 
    monsters.add(monster) 
             
 
ship = player(rocket, 5, win_height - 100, 80, 100, 10)
pulka = Bullet(bullet, 350, 500, 10, 30, 50) 
 
finish = False 
game = True 
while game != False: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish: 
        window.blit(background, (0, 0)) 
 
        text_score = font2.render('Рахунок: ' + str(score), 1, (255, 255, 255)) 
 
        window.blit(text_score, (10, 20)) 
 
 
        text_lose = font2.render('Пропущено: ' + str(lost), 1, (255, 255, 255)) 
 
        window.blit(text_lose, (10, 50)) 
        ship.reset()

        ship.update() 
        monsters.update()
        bullets.update()
        bullets.draw(window)  
        monsters.draw(window)
        sprites_list = sprite.groupcollide(monsters,bullets,True,True)
        for i in sprites_list:
            score+=1
            monster=Enemy(enemy, randint(80, 629), -60, 80, 50, randint(1,5)) 
            monsters.add(monster)
        if sprite.spritecollide(ship,monsters,False)  or lost >= 3:
            finish=True
            window.blit(lose,(200,200))  
        if score>=11:
            finish=True
            window.blit(win,(200,200))

            


    display.update() 
    time.delay(40)