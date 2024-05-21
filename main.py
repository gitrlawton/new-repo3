import pygame
import random
import math

# Initialize the pygame features
pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

# How large a tile is going to be.
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
# Speed at which the tiles will move (move velocity).
MOVE_VEL = 20

# Create a pygame window.
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]
    
    def __init__(self, value, row, col):
        self.value = value         # 2, 4, 8, etc.
        self.row = row             # row number of the grid.
        self.col = col             # column number of the grid.
        self.x = col * RECT_WIDTH  # starting x-coordinate for drawing the tile.
        self.y = row * RECT_HEIGHT # starting y-coordinate for drawing the tile.
        
    # Getter   
    def get_color(self):
        # Get the index of the color the tile currently is.
        color_index = int(math.log2(self.value)) - 1
        # Retrieve the color from the list of colors using the index.
        color = self.COLORS[color_index]
        
        return color
    
    # Method draws the tile on the screen.
    def draw(self, window):
        # Draw the tile.
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        
        # Set the text to be drawn on top of the tile.
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        # Set the position to draw the text at.
        x_position = self.x + (RECT_WIDTH / 2 - text.get_width() / 2)
        y_position = self.y + (RECT_HEIGHT / 2 - text.get_height() / 2)
        # Draw the number at that position.
        window.blit(text, (x_position, y_position))
    
    # Method sets the position of the tile in the grid.
    def set_position(self):
        pass
    
    # Method moves the tile.
    def move(self, delta):
        pass

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    
    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
    
    # Draw window border.
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw(window, tiles):
    # Paint the window the background color.
    window.fill(BACKGROUND_COLOR)
    
    # Draw each of the tiles.
    for tile in tiles.values():
        tile.draw(window)
    
    # Draw the grid.
    draw_grid(window)
    # Update window.
    pygame.display.update()
    
def get_random_pos(tiles):
    row = None
    col = None
    
    # Until we find a random row-col position that does not yet have a tile 
    # in it...
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)
        
        if f"{row}{col}" not in tiles:
            break
        
    return (row, col)
        
# Function to generate two initial tiles to start our game.   
def generate_tiles():
    # Create empty dictionary for tiles.
    tiles = {}
    # Execute loop 2 times.
    for _ in range(2):
        # generate random row and column for tile to be placed at.
        row, col = get_random_pos(tiles)
        # Add tile to the dictionary using the string version of its row/col 
        # for the key and the Tile object as the value.
        tiles[f"{row}{col}"] = Tile(2, row, col)
        
    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True
    
    # Tiles is a dictionary of tiles.  The keys are two-digit strings 
    # representing the row and column. Example: "00" is row 0 col 0 and 
    # "20" is row 2 col 0.  generate_tiles() generates two random tiles to
    # start our game.
    tiles = generate_tiles()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        # Draw the tiles on the window.
        draw(window, tiles)
    
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)