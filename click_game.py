character = Actor('character')
character.pos = 100,100

WIDTH=900
HEIGHT=700
BACKGROUND_COLOR= (223, 186, 178)

def draw():
    screen.fill(BACKGROUND_COLOR)
    character.draw()

def update():
    character.left= character.left + 2
    if character.left > WIDTH:
        character.right=0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        set_character_hurt()
        clock.schedule_unique(set_character_normal, 1.0)

def set_character_hurt():
    character.image = 'characterclicked'

def set_character_normal():
    character.image = 'character'

