import map
import player
import pygame

"""Hello"""

class main:
    def __init__(self) -> None:
        self.Window = pygame.init()
        self.Screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Start It!")
        self.Icon = pygame.image.load('images/floor_block.png')
        pygame.display.set_icon(self.Icon)
        self.fontFreesansbold = pygame.font.Font("freesansbold.ttf", 32)
        self.Clock = 120
        pygame.time.Clock.tick(self.Clock) #设置帧数

    def get_data():
        Map = map.map()
        Player = player()
        return Map, Player

    def run_it(self):
        Map, Player = main.get_data()
        # Map =  main.getData()
        Running = True
        while Running == True:
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    Running = False  #判定关闭游戏
            # self.Window.blit(Player.image, (tuple(player.Location))) #渲染主角
                Player.operator() #调用移动函数
            Map.show_block_floor(self.Screen) #生成地图
            Player.update()
            pygame.display.update()

    def event():
        pass

Run = main()
Run.run_it()