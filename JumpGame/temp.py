import pygame
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Keyboard Jump Game')
background = pygame.image.load('keyback.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
font = pygame.font.SysFont('comicsans', 40)

word_speed = 0.5
score = 0
last_typed_index = -1

LETTER_SPACING = 5

def new_word():
    global displayword, yourword, x_cor, y_cor, word_speed, last_typed_index
    x_cor = random.randint(300, 700)
    y_cor = 200
    word_speed += 0.10
    yourword = ''
    words = open("words.txt").read().split(', ')
    displayword = random.choice(words)
    last_typed_index = -1

font_name = pygame.font.match_font('comic.ttf')

def draw_text(display, text, size, x, y, color=black):
    font = pygame.font.Font(font_name, size)
    total_width = sum(font.size(letter)[0] for letter in text) + (len(text) - 1) * LETTER_SPACING
    x -= total_width // 2

    for i, letter in enumerate(text):
        if i < len(yourword) and text[i] == yourword[i]:
            text_surface = font.render(letter, True, (255, 255, 255))
        else:
            text_surface = font.render(letter, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        gameDisplay.blit(text_surface, text_rect)
        x += font.size(letter)[0] + LETTER_SPACING

def game_front_screen():
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4, black)
        draw_text(gameDisplay, "Score: " + str(score), 70, WIDTH / 2, HEIGHT / 2, black)
    else:
        draw_text(gameDisplay, "Press a key to begin!", 54, WIDTH / 2, 500, black)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False

game_over = True
game_start = True
yourword = ''  # Initialize yourword variable

while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
        game_over = False

        new_word()

    background = pygame.image.load('teacher-background.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50, 50))
    wood = pygame.image.load('wood-.png')
    wood = pygame.transform.scale(wood, (90, 50))

    gameDisplay.blit(background, (0, 0))

    y_cor += word_speed
    gameDisplay.blit(wood, (x_cor - 50, y_cor + 15))
    gameDisplay.blit(character, (x_cor - 100, y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score: ' + str(score), 40, WIDTH / 2, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            yourword += pygame.key.name(event.key)

            if displayword.startswith(yourword):
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
                    last_typed_index = -1
                else:
                    last_typed_index = len(yourword) - 1
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()

    if y_cor < HEIGHT - 5:
        pygame.display.update()
    else:
        game_front_screen()
