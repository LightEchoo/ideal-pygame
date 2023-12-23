from map_elem import block_floor
import pygame



# class map:
#     def __init__(self) -> None:
#         self.blockList = []
#         for i in range(0, 801, 60):
#             self.blockList.append(block_floor(x=i,
#                                               y=540, 
#                                               height=60, 
#                                               width=60, 
#                                               imgPath='/Users/ruochenqi/Documents/GitHub/ideal-pygame/images/floor_block.png'))
    
#     def show_block_floor(self, screen):
#         for b in self.blockList:
#             screen.blit(b.img, (b.loc[0], b.loc[1]))
            

class map:
    def __init__(self) -> None:
        self.blocks = pygame.sprite.Group()
        self.blocks.add(block_floor(0, 660, 22))
        self.blocks.add(block_floor(0, 540, 2))
        
    def show_block_floor(self, screen):
        self.blocks.draw(screen)
        
