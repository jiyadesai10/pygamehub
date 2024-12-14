import pygame
import random
import math
import sys

# Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 30)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("./hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
words = ['ANSWER', 'IN', 'SOME', 'SPELL', 'OFTEN', 'LAND', 'IS', 'LAND', 'GO', 'LINE', 'HER', 'ARE', 'THOSE', 'ONE', 'FACE', 'ON', 'FAMILY', 'SMALL', 'LEAVE', 'OUR', 'OTHER', 'UNTIL', 'REALLY', 'INTO', 'BOTH', 'CHANGE', 'FALL', 'CUT', 'SEE', 'NEVER', 'GREAT', 'YOU', 'FIRE', 'GOOD', 'SAW', 'SO', 'GET', 'OFTEN', 'HAS', 'POINT', 'SEA', 'IF', 'DO', 'AT', 'WHERE', 'HER', 'FEET', 'BIG', 'GOT', 'WENT', 'TREE', 'AND', 'UNTIL', 'HEAD', 'OTHER', 'WORK', 'BY', 'ANIMAL', 'HE', 'WRITE', 'MADE', 'NUMBER', 'RED', 'BEFORE', 'TELL', 'RIGHT', 'HAVE', 'PUT', 'GO', 'WHERE', 'MUCH', 'THEM', 'LEARN', 'PLANT', 'JUST', 'PAGE', 'HIM', 'DAY', 'RUN', 'LIST', 'WAS', 'ONCE', 'TRY', 'MUST', 'SAW', 'FAMILY', 'VERY', 'GIVE', 'WITHOUT', 'DAY', 'ONE', 'ABOVE', 'TWO', 'NOT', 'BOY', 'NOT', 'BELOW', 'SEE', 'START', 'OFF', 'ASK', 'YEAR', 'LITTLE', 'WHERE', 'SAW', 'MOST', 'USE', 'STORY', 'BY', 'FATHER', 'AGAIN', 'BUT', 'FATHER', 'TRY', 'COUNTRY', 'OWN', 'WHITE', 'MUCH', 'MAY', 'THAT', 'WORK', 'FIRST', 'NEVER', 'ABOUT', 'SHOULD', 'ONE', 'HAD', 'SOON', 'MAN', 'LIFE', 'AT', 'GREAT', 'TRY', 'FALL', 'HER', 'PEOPLE', 'PLANT', 'ANSWER', 'MILE', 'WILL', 'WAS', 'SAY', 'MISS', 'CAR', 'KEEP', 'SONG', 'MOTHER', 'HER', 'FOLLOW', 'ABOVE', 'THEIR', 'STATE', 'PLACE', 'FACE', 'MY', 'IF', 'STATE', 'HOUSE', 'COUNTRY', 'GROUP', 'BUT', 'STUDY', 'RIVER', 'MEAN', 'GOT', 'THIS', 'POINT', 'THREE', 'ANY', 'MUCH', 'LITTLE', 'SHOULD', 'EYE', 'CAN', 'FIRST', 'HEAR', 'ABOVE', 'WORD', 'GROUP', 'WHY', 'MUST', 'AWAY', 'LARGE', 'MOVE', 'OWN', 'PLACE', 'OUR', 'LONG', 'LATER', 'POINT', 'CUT', 'AIR', 'STUDY', 'WAS', 'FORM', 'IT', 'STILL', 'CAME', 'MY', 'ITS', 'SHOW', 'STOP', 'OUR', 'IT', 'BE', 'BEGIN', 'FAR', 'SOME', 'TIMES', 'THEN', 'SAID', 'GET', 'HAS', 'MAKE', 'HERE', 'OUT', 'HIM', 'SHE', 'SOON', 'WITH', 'OUT', 'THIS', 'SEEM', 'ANOTHER', 'LIVE', 'TIME', 'BETWEEN', 'EXAMPLE', 'LINE', 'THERE', 'OLD', 'MUST', 'GOOD', 'MADE', 'LIVE', 'MOTHER', 'CARRY', 'MIGHT', 'CARRY', 'LIKE', 'THIS', 'TOGETHER', 'SEE', 'SEA', 'ANSWER', 'END', 'TALK', 'CHANGE', 'MIGHT', 'FEET', 'SO', 'BOY', 'USE', 'INTO', 'NO', 'JUST', 'LAND', 'THING', 'CITY', 'MOVE', 'YOUNG', 'TOGETHER', 'THING', 'BOOK', 'FATHER', 'FOUR', 'SEEM', 'TO', 'DAY', 'TELL', 'GO', 'THING', 'ITS', 'BELOW', 'RIGHT', 'MOVE', 'HOUSE', 'BECAUSE', 'YEAR', 'TREE', 'RIGHT', 'POINT', 'SAY', 'THOUGHT', 'NIGHT', 'CUT', 'FEET', 'DID', 'AN', 'WE', 'LET', 'AT', 'SO', 'WANT', 'LAST', 'GREAT', 'WORD', 'SHOULD', 'CUT', 'HEAR', 'AT', 'STOP', 'ALL', 'PLANT', 'A', 'HER', 'THEIR', 'WATCH', 'FEET', 'BEGIN', 'DOES', 'LINE', 'AIR', 'ME', 'EYE', 'FACE', 'CALL', 'VERY', 'FOR', 'START', 'AROUND', 'BY', 'THEY', 'SUCH', 'STILL', 'EYE', 'DID', 'NUMBER', 'HOME', 'HOME', 'THINK', 'SOME', 'TIMES', 'BEGIN', 'WORD', 'HIGH', 'MIGHT', 'SCHOOL', 'MAY', 'BELOW', 'THEIR', 'CAN', 'EVEN', 'MUCH', 'END', 'MEN', 'EARTH', 'START', 'ASK', 'FOLLOW', 'NO', 'SHE', 'AFTER', 'BOTH', 'STATE', 'LATER', 'ALWAYS', 'ON', 'SEE', 'CUT', 'FATHER', 'LATER', 'EYE', 'THIS', 'FEW', 'HIGH', 'THEN', 'DID', 'MILE', 'HIGH', 'WHERE', 'THOUGHT', 'LEARN', 'FROM', 'HER', 'SEE', 'AROUND', 'CAR', 'NUMBER', 'THROUGH', 'GREAT', 'ALMOST', 'SOME', 'HARD', 'REALLY', 'TREE', 'OLD', 'HAVE', 'BLACK', 'CAR', 'BECAUSE', 'ABOUT', 'THROUGH', 'YOU', 'EARTH', 'FIRST', 'THAT', 'IT', 'OVER', 'FAR', 'FALL', 'SAME', 'ASK', 'WILL', 'CUT', 'MY', 'HAD', 'WHAT', 'WORLD', 'HOW', 'AN', 'SMALL', 'FIND', 'WAR', 'STORY', 'WHERE', 'SOUND', 'THROUGH', 'INTO', 'HE', 'LIGHT', 'WATER', 'THEIR', 'BEING', 'KEEP', 'BOTH', 'ME', 'CHANGE', 'THEY', 'STOP', 'AGAIN', 'SHE', 'COUNTRY', 'CALL', 'SOMETIMES', 'OVER', 'SAME', 'BIG', 'THIS', 'END', 'CAME', 'COULD', 'SOUND', 'RIVER', 'MIGHT', 'READ', 'WELL', 'HAVE', 'FAR', 'YOU', 'LEARN', 'DO', 'ALL', 'UPON', 'THAT', 'UNTIL', 'DOES', 'ADD', 'WATER', 'HIGH', 'WELL', 'PLANT', 'SEEM', 'ONE', 'DAY', 'OPEN', 'NEED']
word = random.choice(words)
guessed = set()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw():
    win.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Draw hangman
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message, word=None):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))

    if word:
        word_text = WORD_FONT.render("The word was: " + word, 1, BLACK)
        win.blit(word_text, (WIDTH / 2 - word_text.get_width() / 2, HEIGHT / 2 - word_text.get_height() / 2 + 50))
    
    pygame.display.update()
    pygame.time.delay(3000)



def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    game_won = False  # Add a flag to track if the game has been won

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.add(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won and not game_won:  # Check if the game is won and the delay hasn't been triggered yet
            game_won = True  # Set the flag to True
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!", word)
            break

    pygame.quit()




if __name__ == '__main__':
    main()
