import pygame



# class vault(map_elem):
#     def __init__(self, x, y, height, width, imgPath) -> None:
#         super().__init__(x, y, height, width, imgPath)
#         self.crossAble = True

# class wall(map_elem):
#     def __init__(self, x, y, height, width, imgPath) -> None:
#         super().__init__(x, y, height, width, imgPath)
    
        
class block(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('images/floor_block.png')
        self.rect = self.image.get_rect(topleft=(x,y))

class block_floor(pygame.sprite.Sprite):
    def __init__(self, x, y, num_stacks):
        super().__init__()
        original_image = pygame.image.load('images/floor_block.png')
        new_width = original_image.get_width() * num_stacks
        new_height = original_image.get_height()
        stacked_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
        
        for i in range(num_stacks):
            stacked_image.blit(original_image, (i * original_image.get_width(), 0))
        
        self.image = stacked_image
        self.rect = self.image.get_rect(topleft=(x, y))
        

  
       