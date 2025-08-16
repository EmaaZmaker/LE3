import random
import pygame

pygame.init()
#creating custom event type

sprite_color_change=pygame.USEREVENT+1
background_color_change=pygame.USEREVENT+2

# defining color
#background color

blue=pygame.Color('blue')
lightblue=pygame.Color('lightblue')
darkblue=pygame.Color('darkblue')

#sprite color

yellow=pygame.Color('yellow')
magenta=pygame.Color('magenta')
white=pygame.Color('white')
orange=pygame.Color('orange')

#sprite class

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary=False
        if self.rect.left <=0 or self.rect.right >=0:
            self.velocity[0]=-self.velocity[0]
            boundary=True
        if self.rect.top <=0 or self.rect.bottom >=0:
            self.velocity[0]=-self.velocity[0]
            boundary=True
        if boundary:
            pygame.event.post(pygame.event.Event(sprite_color_change))
            pygame.event.post(pygame.event.Event(background_color_change))
    def color_change(self):
        self.image.fill(random.choice[yellow,magenta,white,orange])
def background_change():
    global bgcolor
    bgcolor=random.choice([blue,lightblue,darkblue])
all_sprite=pygame.sprite.Group()
sp1=Sprite(white,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)
all_sprite.add(sp1)
screen = pygame.display.set_mode((500, 400))

# Set the window title

pygame.display.set_caption("Colorful Bounce")

# Set the initial background color

bgcolor = blue

# Apply the background color

screen.fill(bgcolor)

exit = False

# Create a clock object to control frame rate

clock = pygame.time.Clock()

while not exit:

# Event handling loop

    for event in pygame.event.get():

# If the window's close button is clicked, exit the game

        if event.type == pygame.QUIT:

            exit = True

# If the sprite color change event is triggered, change the sprite's color

        elif event.type == sprite_color_change:

            sp1.change_color()

# If the background color change event is triggered, change the background color

        elif event.type == background_color_change:

            background_change()

# Update all sprites

    all_sprite.update()

# Fill the screen with the current background color

    screen.fill(bgcolor)

# Draw all sprites to the screen

    all_sprite.draw(screen)

# Refresh the display

    pygame.display.flip()

# Limit the frame rate to 240 fps

    clock.tick(240)

# Uninitialize all pygame modules and close the window

pygame.quit()