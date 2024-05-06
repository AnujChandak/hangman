import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1250, 650
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN!!")

images = []
for i in range(1, 8):
    image = pygame.image.load("hangman " + str(i) + ".jpg") 
    images.append(image)
    
hangman_status = 0
word = ['MR AND MRS KHILADI','INTERNATIONAL KHILADI','SAINIK','ZANJEER','LAXMII','PAGALPANTI','MAI HOON NA',
         'WAZIR','SULTAN','BATLA HOUSE','DOSTANA','DHOOM','DHOOM 2','DHOOM 3','KALA PATTHAR','MUGHAL-E-AZAM',
         'TANHAJI:THE UNSUNG WARRIOR', 'Hindi Medium',' Flight','Uri-The Surgical Strike','Andhadhun','Bhaag Milkha Bhaag',
         ' Gangs of Wasseypur','Zindagi Na Milegi Dobara',' A Wednesday',' Black Friday',' Khosla Ka Ghosla',' Munna Bhai M.B.B.S.',
         'The Legend of Bhagat Singh','Sarfarosh','Dilwale Dulhania Le Jayenge','Jo Jeeta Wohi Sikandar','Aaj Ka Arjun',
         'Agneepath','	Kishen Kanhaiya','Thanedaar'"KAHO NA PYAAR HAI","WAR","KRRISH","GUZAARISH","ITTEFAQ","ALL IS WELL","ACTION REPLAY",
         "SHOLAY","ANDAZ APNA APNA","GOLMAAL","NAMAK HALAL","DAMINI","DEEWAR","PADOSAN",'CHAL MERE BHAI',
         "HERA PHERI","PHIR HERA PHERI","AMAR AKBAR ANTHONY",'KABIR SINGH','OM SHANTI OM',
         'GABBAR IS BACK','ROWDY RATHORE','BAAGHI','KOI MIL GAYA','KITES','KRRISH 3','GHAYAL',
         'BAAGHI 3','DEVDAS','shivaay','LAGAAN','PANGA','DARR','KHILADI 420','KHILADI','KHILADI 786']
word =  [x.upper() for x in word]
word = random.choice(word)
guessed = ["A","E","I","O","U"," ",'-',':','.']


black = (0,0,0)
 

radius = 20
gap = 15
letters = []
startx = round((200+WIDTH-(radius*2+gap)*13)/2)
starty = 400
A=65

for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i//13)* (gap + radius *2))
    letters.append([x,y, chr(A + i), True])

for i in range(26,36):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i//13)* (gap + radius *2))
    letters.append([x,y, str(i-26), True])

letter_font = pygame.font.SysFont("TimesNewRoman", 35)
word_font = pygame.font.SysFont("TimesNewRoman", 60)
word_font1 = pygame.font.SysFont("TimesNewRoman", 100)
letters[0][3] = False
letters[4][3] = False
letters[8][3] = False
letters[14][3] = False
letters[20][3] = False

FPS = 60
clock = pygame.time.Clock()
run = True
count = 0
def draw():
     win.fill((100,0,200))
     i = 0
     display_word = ["","","","","","","","","","",""]
     for letter in word:
         if letter in guessed:
             if letter == " ":
                 i += 1
                 continue
             display_word[i] += letter
         else:
             display_word[i] += "_ "
     x = 50
     y = 50
     for j in range(len(display_word)):
         text = word_font.render(display_word[j], 1, black)
         win.blit(text, (x, y))
         x += 50 * (len(display_word[j]) - display_word[j].count(" "))
         if len(display_word[j]) - display_word[j].count(" ") < 5:
             x += 40
         if x + (50 * (len(display_word[j]) - display_word[j].count(" ")))> 1250:
             y += 70
             x = 50
     
     for letter in letters:
         x, y, ltr, visible = letter
         if visible:
             pygame.draw.circle(win, black, (x, y), radius, 3)
             text = letter_font.render(ltr, 1, black)
             win.blit(text, (x - text.get_width()/2,y - text.get_height()/2))
     
     win.blit(images[hangman_status], (60, 300))
     pygame.display.update()

while run:
    clock.tick(FPS)
    draw()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < radius:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        if count:
            pygame.time.delay(1500)
            win.fill((135,206,235))
            text= word_font1.render("Congratulations!!", 3000, (150,50,30))
            win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - 100 - text.get_height()/2))
            text2= word_font.render("Movie is: " + word , 1, black)
            win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 + 200 - text2.get_height()/2))
            text3 = word_font.render("You have won :)", 1, black)
            win.blit(text3, (WIDTH/2 - text.get_width()/2 + 100, HEIGHT/2 - text.get_height()/2 + 50 ))
            pygame.display.update()
            pygame.time.delay(3500)
            break
        else:
            count+=1
            continue
    if hangman_status == 6:
        
        win.fill((135,206,235))
        text= word_font.render("Sorry you have lost, Better luck next time", 1, black)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        text2= word_font.render("Movie was: " + word , 1, black)
        win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 + 100 - text2.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
        break    
            
            
pygame.quit()


