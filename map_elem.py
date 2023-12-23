import pygame



# class map_elem:
#     def __init__(self, x, y, height, width, imgPath) -> None:
#         self.Loc = [x, y]
#         self.Height = height
#         self.Width = width
#         self.crossAble = False
#         self.Img = pygame.image.load(imgPath)

class block_floor(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width, imgPath) -> None:
        super().__init__(x, y, height, width, imgPath)

class vault(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width, imgPath) -> None:
        super().__init__(x, y, height, width, imgPath)
        self.crossAble = True

class wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width, imgPath) -> None:
        super().__init__(x, y, height, width, imgPath)
    
        
    
        
    
       