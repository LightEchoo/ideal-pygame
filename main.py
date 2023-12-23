import map
import player
import pygame
import STATIC_DATA

"""Hello"""

class main:
    def __init__(self) -> None:
        self.Window = pygame.init()
        self.Screen = pygame.display.set_mode((STATIC_DATA.BORDER_LR, STATIC_DATA.BORDER_TD))
        pygame.display.set_caption("Start It!")
        self.Icon = pygame.image.load('images/floor_block.png')
        pygame.display.set_icon(self.Icon)
        self.fontFreesansbold = pygame.font.Font("freesansbold.ttf", 32)
        self.Clock = pygame.time.Clock()

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
            
            for block in Map.blocks:
                Player.check_collision(block)
            Player.outForEventOperator(self.Screen)
            Map.show_block_floor(self.Screen)
            pygame.display.flip()
            self.Clock.tick(120) #设置帧数

    def quit(Event):
        if Event.type == pygame.QUIT:
            return False  #判定关闭游戏

    def clock_control(self, newClock):
        self.Clock.tick(newClock)


        
Run = main()
Run.run_it()

# in Event
# not in Event