from map_elem import block_floor



class map:
    def __init__(self) -> None:
        self.blockList = []
        for i in range(0, 801, 60):
            self.blockList.append(block_floor(x=i,
                                              y=540, 
                                              height=60, 
                                              width=60, 
                                              imgPath='/Users/ruochenqi/Documents/2D_game_project/pic/floor_block.png'))
    
    def show_block_floor(self, screen):
        for b in self.blockList:
            screen.blit(b.img, (b.loc[0], b.loc[1]))
            
