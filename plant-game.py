from typing import Any
import pygame
import random
import os
import math

pygame.init()
pygame.mixer.init()

#遊戲框架
screenHigh = 760 #畫面高1000像素
screenWidth = 1000 #畫面寬1000像素
screen = pygame.display.set_mode((screenWidth, screenHigh)) #創建視窗
pygame.display.set_caption(這才不是1942) #視窗標題
clock = pygame.time.Clock() #創建對時間管理的物件
FPS = 60 #設置一個變數FPS = 60

#顏色
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

#載入圖片
backgroung_img = pygame.image.load(os.path.join(img, background.png)).convert() 
start_img = pygame.image.load(os.path.join(img, start.jpg)).convert()
player_img = pygame.image.load(os.path.join(img, player.png)).convert()
pygame.display.set_icon(player_img)
plane_img = pygame.image.load(os.path.join(img, plane.png)).convert()
bullet_img = pygame.image.load(os.path.join(img, bullet.png)).convert()
laser_img = pygame.image.load(os.path.join(img, laser.png)).convert()
attak_img = pygame.image.load(os.path.join(img, attak.png)).convert()
expl_anim = {}
expl_anim['lg'] = []
expl_anim['sm'] = []
for i in range(9)
    expl_img = pygame.image.load(os.path.join(img, fexpl{i}.png)).convert()
    expl_img.set_colorkey(BLACK)
    expl_anim[lg].append(pygame.transform.scale(expl_img, (100,100)))
    expl_anim[sm].append(pygame.transform.scale(expl_img, (50,50)))

power_imgs = {}
power_imgs['shield'] = pygame.image.load(os.path.join(img, shield.png)).convert()
power_imgs['gun'] = pygame.image.load(os.path.join(img, gun.png)).convert()

#載入音樂
shoot_sound = pygame.mixer.Sound(os.path.join(sound, shoot.wav))
gun_sound = pygame.mixer.Sound(os.path.join(sound, pow1.wav))
shield_sound = pygame.mixer.Sound(os.path.join(sound, pow0.wav))
kill_sound = pygame.mixer.Sound(os.path.join(sound, kill.mp3))
expl_sounds = [pygame.mixer.Sound(os.path.join(sound, expl0.wav)),
               pygame.mixer.Sound(os.path.join(sound, expl1.wav))]
pygame.mixer.music.load(os.path.join(sound, background.mp3))
pygame.mixer.music.set_volume(0.2)

#載入字體
font_name = os.path.join(font.ttf)

def drew_text(surf, text, size , x, y)
    font = pygame.font.Font(font_name, size) # 創建字體物件
    text_surface = font.render(text, True, WHITE) # 將文字渲染成圖像
    text_rect = text_surface.get_rect() # 取得文字圖像的矩形區域
    text_rect.centerx = x # 設定文字圖像的中心位置的x座標
    text_rect.top = y # 設定文字圖像的上方位置的y座標
    surf.blit(text_surface, text_rect) # 將文字圖像繪製到指定的表面上

def new_plane()
        p = Plane()
        all_sprites.add(p)
        planes.add(p)

def draw_health(surf, hp, x, y)
    if hp  0
        hp = 0
    BAR_LENGTH = 200
    BAR_HEIGHT = 20
    fill = (hp100)BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 4)

def draw_init()
    screen.blit(pygame.transform.scale(start_img,(1000,760)) , (0,0))
    drew_text(screen, '這才不是1942', 64, screenWidth2, screenHigh4)
    drew_text(screen, 'W A S D 移動飛機 空白鍵發射子彈', 24, screenWidth2, screenHigh2)
    drew_text(screen, '按任意鍵開始遊戲', 18, screenWidth2, screenHigh34)
    pygame.display.update()
    waiting = True
    while waiting
        clock.tick(FPS)
        #取得輸入
        for event in pygame.event.get()
            if event.type == pygame.QUIT
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP
                waiting = False
                return False

class Player(pygame.sprite.Sprite) #創建玩家飛機類別
    def __init__(self)
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.transform.scale(player_img, (100, 75 )) #設定玩家飛機圖片與大小
        self.image.set_colorkey(BLACK) #去除周圍黑色部分
        self.rect = self.image.get_rect() #定位圖片
        self.rect.centerx = screenWidth2
        self.rect.bottom = screenHigh - 10
        self.speedx = 4
        self.health = 100
        self.gun = 1
        self.gun_time = 0

    def update(self)
        now = pygame.time.get_ticks()
        if self.gun  1 and now - self.gun_time  20000
            self.gun -= 1
            self.gun_time = now

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_s]
            self.rect.y += self.speedx
        if key_pressed[pygame.K_w]
            self.rect.y -= self.speedx

        if self.rect.right  screenWidth
            self.rect.right = screenWidth
        if self.rect.left  0
            self.rect.left = 0
        if self.rect.top  0
            self.rect.top = 0
        if self.rect.bottom  screenHigh
            self.rect.bottom = screenHigh

    def shoot(self)
        if self.gun == 1
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()
        elif self.gun == 2
            bullet1 = Bullet(self.rect.left, self.rect.centery)
            bullet2 = Bullet(self.rect.right, self.rect.centery)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
            shoot_sound.play()
        elif self.gun == 3
            bullet1 = Bullet(self.rect.left, self.rect.centery)
            bullet2 = Bullet(self.rect.right, self.rect.centery)
            bullet3 = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet2)
            shoot_sound.play()
        elif self.gun = 4
            laser = Laser(self.rect.centerx, self.rect.top)
            all_sprites.add(laser)
            lasers.add(laser)
            shoot_sound.play()

    def gunup(self)
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()

class Plane(pygame.sprite.Sprite)
    def __init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(plane_img, (75 , 56 ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screenWidth - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-2, 2)

    def update(self)
        self.rect.y += self.speedy    
        self.rect.x += self.speedx
        if self.rect.top  screenHigh or self.rect.left  screenWidth or self.rect.right  0
            self.rect.x = random.randrange(0, screenWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)
            self.speedx = random.randrange(-2, 2)
    
    def plane_shoot(self)
        bullet = plane_attak(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        plane_shoot.add(bullet)

class plane_attak(pygame.sprite.Sprite)
    def __init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image = pygame.transform.scale(attak_img, (20, 35 ))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.speedy = 3

    def update(self)
        self.rect.y += self.speedy    
        if self.rect.top  screenHigh
            self.kill()

class Bullet(pygame.sprite.Sprite)
    def __init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image = pygame.transform.scale(bullet_img, (15, 60 ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self)
        self.rect.y += self.speedy    
        if self.rect.bottom  0
            self.kill()

class Laser(pygame.sprite.Sprite)
    def __init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        self.image = pygame.transform.scale(laser_img, (95, 60 ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -12

    def update(self)
        self.rect.y += self.speedy    
        if self.rect.bottom  0
            self.kill()

class Explosion(pygame.sprite.Sprite)
    def __init__(self, center, size)
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self)
        now = pygame.time.get_ticks()
        if now - self.last_update  self.frame_rate
            self.last_update = now
            self.frame +=1
            if self.frame == len(expl_anim[self.size])
                self.kill()
            else
                self.image = expl_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center


class Power(pygame.sprite.Sprite)
    def __init__(self, center)
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = power_imgs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self)
        self.rect.y += self.speedy    
        if self.rect.top   screenHigh
            self.kill()



pygame.mixer.music.play(-1)

#遊戲迴圈
show_init = True
running = True
game_paused = False  # 新增變數以判斷遊戲是否暫停
while running
    if show_init
        close = draw_init()
        if close
            break
        show_init = False
        all_sprites = pygame.sprite.Group() #創建all_sprites群組，將上面所創建的類別放到這裡
        planes = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        plane_shoot = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(6)
            new_plane()

        score = 0
        point = 10
        plane_cruh = 30
        plane_bomb = 20
        new_plane_add = 200

    clock.tick(FPS) #設定遊戲迴圈執行次數
    #取得輸入
    for event in pygame.event.get()
        if event.type == pygame.QUIT
            running = False
        elif event.type == pygame.KEYDOWN
            if event.key == pygame.K_SPACE
                player.shoot()
            elif event.key == pygame.K_ESCAPE  # 新增按下 ESC 鍵的事件
                game_paused = not game_paused  # 切換遊戲暫停狀態

    if game_paused
        continue  # 若遊戲暫停，則跳過更新遊戲的部分

    pygame.display.update()

    #更新遊戲
    all_sprites.update()

    # 敵軍飛機發射子彈
    for plane in planes
        if random.random()  0.004  
            plane.plane_shoot()

    #判斷敵軍與子彈相撞
    hits = pygame.sprite.groupcollide(planes, bullets, True, True)
    for hit in hits
        random.choice(expl_sounds).play()
        score += point
        #得分每上升200，增加敵軍飛機  
        if score = new_plane_add 
            new_plane()
            new_plane_add += 200  
         
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random()  0.95 
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_plane()

    #判斷敵軍與雷射相撞
    hits = pygame.sprite.groupcollide(planes, lasers, True, False)
    for hit in hits
        random.choice(expl_sounds).play()
        score += point
        #得分每上升200，增加敵軍飛機  
        if score = new_plane_add 
            new_plane()
            new_plane_add += 200   
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random()  0.95 
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_plane()

    #判斷玩家與敵軍相撞
    hits = pygame.sprite.spritecollide(player, planes, True, pygame.sprite.collide_mask)
    for hit in hits
        new_plane()
        player.health -= plane_cruh
        expl = Explosion(hit.rect.center, 'sm')
        kill_sound.play()
        all_sprites.add(expl)
        if player.health = 0
            show_init = True
            
    #判斷玩家與敵軍子彈相撞
    hits = pygame.sprite.spritecollide(player, plane_shoot, True, pygame.sprite.collide_mask)
    for hit in hits
        player.health -= plane_bomb
        expl = Explosion(hit.rect.center, 'sm')
        kill_sound.play()

        all_sprites.add(expl)
        if player.health = 0
            show_init = True
    
    #判斷玩家與寶物相撞
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits
        if hit.type == 'shield'
            player.health += 20
            if player.health  100
                player.health = 100
            shield_sound.play()
        elif hit.type == 'gun'
            player.gunup()
            gun_sound.play()
  


    #畫面顯示
    screen.fill((0,0,0))
    screen.blit(pygame.transform.scale(backgroung_img,(1000,760)) , (0, 0))
    all_sprites.draw(screen) #將所創建的物件放到畫面上
    drew_text(screen, str(score), 36, screenWidth2, 10) #顯示得分
    draw_health(screen, player.health, 5, 10) #顯示血條
    pygame.display.update() 
pygame.quit()