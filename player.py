import pygame
import math
import STATIC_DATA


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.status = 'right'  # 用于匹配图片，默认向右

        self.imgList = {}  # 不同状态的图片字典
        self.imgList['right'] = pygame.image.load('images/player_default.png.')
        self.rect = self.imgList['right'].get_rect()  # 获取图片的尺寸作为精灵的尺寸

        self.rect.x = 100
        self.rect.y = STATIC_DATA.ground_position

        self.gravity = 0.3  # 重力
        # self.jump_height = 100  # 希望跳跃高度为100像素

        # 角色移动和跳跃的属性
        self.velocity = pygame.Vector2(0, 0)
        self.on_ground = True

        self.speed = 5  # 英雄用于计算的移动速度（可因某些因素而改变）

        self.jumpCnt = 0  # 跳跃次数
        self.maxJumps = 2  # 最多允许跳跃次数

        self.heroNo = 0
        self.name = "king"
        self.gender = "Male"

        self.health = 1000  # 最大生命值
        self.healthCnt = 1000  # 当前生命值

        self.x = 0
        self.y = 0
        self.width = 64
        self.height = 64

        self.meleeWeapon = 0  # 近战武器类型

        self.rangedWeapon = 0  # 远程武器类型
        self.arrowType = 0  # 弓箭类型
        self.arrowNum = 10  # 弓箭数量上限
        self.arrowCnt = 10  # 当前弓箭数量
        self.shootNum = 1  # 每次射击射出的投掷物数量（某些英雄可能不同，默认为1）

        self.bags = []  # 物品栏列表

        self.activeProps = []  # 动态存储所有生效中的道具的列表

        self.coins = 0  # 货币数量

        self.j1 = False  # 是否正在进行一段跳
        self.j2 = False  # 是否正在进行二段跳


    def update(self):
        self.moveX()
        self.jump()
        self.fall()

    def moveX(self):
        self.rect.x += self.velocity.x
        self.rect.x = max(0, min(self.rect.x, STATIC_DATA.BORDER_LR - self.rect.width))  # 防止出界

    def jump(self):
        if not self.on_ground:
            self.velocity.y += self.gravity  # 重力
            self.rect.y += self.velocity.y
            if self.rect.y > STATIC_DATA.ground_position:  # 检查是否着陆
                self.rect.y = STATIC_DATA.ground_position
                self.on_ground = True
                self.velocity.y = 0
                self.jumpCnt = 0  # 重置跳跃次数

    def jump_key(self):
        if self.on_ground or self.jumpCnt < self.maxJumps:
            self.velocity.y = -10  # 初始跳跃速度
            self.jumpCnt += 1
            self.on_ground = False

    def fall(self):
        if not self.on_ground:
            # 应用重力
            self.velocity.y += self.gravity
            self.rect.y += self.velocity.y

    def changeHP(self):
        pass

    def attack_melee(self):
        pass

    def attack_ranged(self):
        pass

    def use_item(self):
        pass

    def check_img(self):
        pass

    def check_collision(self, block):
        if self.rect.y < STATIC_DATA.ground_position:  # 地面以上
            # 检查玩家和块的碰撞
            if self.rect.colliderect(block.rect):
                # 检查是否在块的上方降落
                if self.velocity.y > 0:  # 下降时发生碰撞
                    self.rect.bottom = block.rect.top  # 玩家站在块上
                    self.on_ground = True
                    self.velocity.y = 0

                # 检查是否从下方接近块
                elif self.velocity.y < 0 and self.rect.top < block.rect.bottom:
                    self.rect.top = block.rect.bottom  # 防止穿过块
                    self.velocity.y = 0  # 停止向上的运动

            else:
                # 如果玩家不在块的水平范围内，则不再算作在地面上
                if self.rect.right < block.rect.left or self.rect.left > block.rect.right:
                    self.on_ground = False

    def inForEventOperator(self, event):
        # 通过键盘事件控制移动
        if event.type == pygame.KEYDOWN:  # 按下就移动
            if event.key == pygame.K_RIGHT:
                self.velocity.x = self.speed
            elif event.key == pygame.K_LEFT:
                self.velocity.x = -self.speed
            # elif event.key == pygame.K_SPACE:
            #     print('发射子弹....')
            elif event.key == pygame.K_UP:
                self.jump_key()
        if event.type == pygame.KEYUP:  # 抬起来就不动
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.velocity.x = 0

    def outForEventOperator(self, screen):
        self.update()
        screen.blit(self.imgList['right'], self.rect)

def bgimage(screen):
    bgImg = pygame.image.load('images/bg.jpg')
    screen.blit(bgImg, (0, 0))

class block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))  # 给块填充一个颜色
        self.rect = self.image.get_rect(topleft=(x, y))
#
# class block(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.image.load("imagepath")
#         self.rect = self.image.get_rect(topleft=(x, y))

if __name__ == "__main__":
    # 初始化界面
    pygame.init()
    screen = pygame.display.set_mode((STATIC_DATA.BORDER_LR, STATIC_DATA.BORDER_TD))
    pygame.display.set_caption('pygame')
    icon = pygame.image.load('images/ufo.png')
    pygame.display.set_icon(icon)
    bgImg = pygame.image.load('images/bg.jpg')

    # 添加背景音效
    # pygame.mixer.music.load('resource/bg.wav')
    # pygame.mixer.music.play(-1)  # 单曲循环

    player = player()

    # #创建块实例
    # blocks = pygame.sprite.Group()
    # blocks.add(block(200, 830, 200, 50))  # 块的位置和尺寸
    # blocks.add(block(500, 830, 200, 50))
    # blocks.add(block(800, 830, 200, 50))
    # blocks.add(block(1100, 830, 200, 50))

    block = block(200, 830, 200, 50)

    # 游戏主循环
    running = True
    clock = pygame.time.Clock()
    while running:
        bgimage(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.inForEventOperator(event)
            # forEventOperator()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     player.velocity.x = -player.speed
        # elif keys[pygame.K_RIGHT]:
        #     player.velocity.x = player.speed
        # else:
        #     player.velocity.x = 0
        #
        # if keys[pygame.K_UP]:
        #     player.jump_key()
        #
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False

        player.outForEventOperator(screen)

        # player.update()
        # # for block in blocks:
        # #     check_collision(player, block)  # 检查玩家和块的碰撞
        # check_collision(player, block)  # 检查玩家和块的碰撞
        # # blocks.draw(screen)
        # screen.blit(player.imgList['right'], player.rect)
        # screen.blit(block.image, block.rect)
        pygame.display.flip()
        clock.tick(120)  # 设置帧率为 120 fps


