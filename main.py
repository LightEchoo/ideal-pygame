import map
import player
import pygame

"""Hello"""

class main:
    def __init__(self) -> None:
        self.Window = pygame.init()
        self.Screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Start It!")
        self.Icon = pygame.image.load('images/floor_block.png')
        pygame.display.set_icon(self.Icon)
        self.fontFreesansbold = pygame.font.Font("freesansbold.ttf", 32)
        self.Clock = pygame.time.Clock()
        self.Clock.tick(120) #设置帧数

    @staticmethod
    def get_data():
        Map = map.map()
        Player = player.player()
        return Map, Player    


    def run_it(self):
        Map, Player = main.get_data()
        # Player =  main.get_data()
        Running = True
        while Running == True:
            player.bgimage(self.Screen)
            
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    Running = False  #判定关闭游戏
                # Running = main.quit(Event)
                Player.inForEventOperator(Event) #调用移动函数
            
            # Map.show_block_floor(self.Screen) #生成地图
            # for block in Map.blocks:
            #     main.check_collision(Player, block)
            Player.outForEventOperator(self.Screen)
            Map.show_block_floor(self.Screen)
            pygame.display.flip()

    def quit(Event):
        if Event.type == pygame.QUIT:
            return False  #判定关闭游戏

    def clock_control(self, newClock):
        self.Clock.tick(newClock)

    def check_collision(player, block):
    # 检查玩家和块的碰撞
        if player.rect.colliderect(block.rect):
        # 检查是否在块的上方降落
            if player.velocity.y > 0:  # 下降时发生碰撞
                player.rect.bottom = block.rect.top  # 玩家站在块上
                player.on_ground = True
                player.velocity.y = 0

        # 检查是否从下方接近块
            elif player.velocity.y < 0 and player.rect.top < block.rect.bottom:
                player.rect.top = block.rect.bottom  # 防止穿过块
                player.velocity.y = 0  # 停止向上的运动

        else:
        # 如果玩家不在块的水平范围内，则不再算作在地面上
            if player.rect.right < block.rect.left or player.rect.left > block.rect.right:
                player.on_ground = False
Run = main()
Run.run_it()

# in Event
# not in Event