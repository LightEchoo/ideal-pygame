import map
# import player
import pygame

class main:
    def __init__(self) -> None:
        self.Window = pygame.init()
        self.Screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Start It!")
        self.Icon = pygame.image.load('floor_block.png')
        pygame.display.set_icon(self.Icon)
        self.fontFreesansbold = pygame.font.Font("freesansbold.ttf", 32)

    def get_data():
        Map = map.map()
        # Player = player.test()
        # return Map, Player
        return Map

    def run_it(self):
        # Map, Player = main.getData()
        Map =  main.getData()
        Running = True
        while Running == True:
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    Running = False  #判定关闭游戏
            # self.Window.blit(Player.image, (tuple(player.Location))) #渲染主角
            # Player.Moving() #调用移动函数
            Map.show_block_floor(self.Screen) #生成地图

            pygame.display.update()

    def event():
        pass

# Run = main()
# Run.run_it()