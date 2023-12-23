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
        self.Clock = pygame.time.Clock()
        self.Clock.tick(120) #设置帧数

    def get_data():
        # Map = map.map()
        Player = player.player()
        # return Map, Player    
        return Player


    def run_it(self):
        # Map, Player = main.get_data()
        Player =  main.get_data()
        Running = True
        while Running == True:
            for Event in pygame.event.get():
                main.quit(Event)
                Player.inForEventOperator(Event) #调用移动函数
            
            # Map.show_block_floor(self.Screen) #生成地图
            Player.outForEventOperator()
            pygame.display.flip()

    def quit(Event):
        if Event.type == pygame.QUIT:
            Running = False  #判定关闭游戏

    def clock_control(self, newClock):
        self.Clock.tick(newClock)


Run = main()
Run.run_it()

# in Event
# not in Event