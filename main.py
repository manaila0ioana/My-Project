#Importing modules
import os
import sys
import pygame


#DATA
FPS = 24 #The number of frames the game is loading per second
WIDTH = 500 #The dimension of the window in pixels
HEIGHT = WIDTH * 1.777777777777778 #The dimension of the window based an exact proportion
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) #Opening the window
current_path = os.path.dirname(os.path.realpath(__file__))
Clock = pygame.time.Clock()
Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


#Setting the name of the aplication
pygame.display.set_caption("TicTacToe by Ioana_Manaila")


#Assets
#VS_AI_BUTTON_IMAGE= pygame.image.load(os.path.join('Assets', 'Vs_Ai_Button.png'))
#VS_AI_BUTTON_IMAGE = pygame.transform.scale(VS_AI_BUTTON_IMAGE, (VS_AI_BUTTON_IMAGE.get_width()*2, VS_AI_BUTTON_IMAGE.get_height()*2))

DOT_IMAGE= pygame.image.load(os.path.join(current_path, 'Assets', 'Dot.png'))
DOT_IMAGE = pygame.transform.scale(DOT_IMAGE, (DOT_IMAGE.get_width()*7.8, DOT_IMAGE.get_height()*7.8))

#PVP_BUTTON_IMAGE = pygame.image.load(os.path.join('Assets', 'Pvp_Button.png'))
#PVP_BUTTON_IMAGE = pygame.transform.scale(PVP_BUTTON_IMAGE, (PVP_BUTTON_IMAGE.get_width()*2, PVP_BUTTON_IMAGE.get_height()*2))

QUIT_BUTTON_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'Quit_Button.png'))
QUIT_BUTTON_IMAGE = pygame.transform.scale(QUIT_BUTTON_IMAGE, (QUIT_BUTTON_IMAGE.get_width()*7.8, QUIT_BUTTON_IMAGE.get_height()*7.8))

MENU_BUTTON_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'Menu_Button.png'))
MENU_BUTTON_IMAGE = pygame.transform.scale(MENU_BUTTON_IMAGE, (MENU_BUTTON_IMAGE.get_width()*7.8, MENU_BUTTON_IMAGE.get_height()*7.8))

PLAY_BUTTON_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'Play_Button.png'))
PLAY_BUTTON_IMAGE = pygame.transform.scale(PLAY_BUTTON_IMAGE, (PLAY_BUTTON_IMAGE.get_width()*7.8, PLAY_BUTTON_IMAGE.get_height()*7.8))

#X_TURN_IMAGE = pygame.image.load(os.path.join('Assets', 'X_Turn.png'))
#X_TURN_IMAGE = pygame.transform.scale(X_TURN_IMAGE, (X_TURN_IMAGE.get_width()*2, X_TURN_IMAGE.get_height()*2))

X_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'X.png'))
X_IMAGE = pygame.transform.scale(X_IMAGE, (X_IMAGE.get_width()*7.8, X_IMAGE.get_height()*7.8))

#O_TURN_IMAGE = pygame.image.load(os.path.join('Assets', 'O_Turn.png'))
#O_TURN_IMAGE = pygame.transform.scale(O_TURN_IMAGE, (O_TURN_IMAGE.get_width()*2, O_TURN_IMAGE.get_height()*2))

O_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'O.png'))
O_IMAGE = pygame.transform.scale(O_IMAGE, (O_IMAGE.get_width()*7.8, O_IMAGE.get_height()*7.8))

X_WON_MENU_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'X_Won_Menu.png'))
X_WON_MENU_IMAGE = pygame.transform.scale(X_WON_MENU_IMAGE, (X_WON_MENU_IMAGE.get_width()*10, X_WON_MENU_IMAGE.get_height()*10))

O_WON_MENU_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'O_Won_Menu.png'))
O_WON_MENU_IMAGE = pygame.transform.scale(O_WON_MENU_IMAGE, (O_WON_MENU_IMAGE.get_width()*10, O_WON_MENU_IMAGE.get_height()*10))

#PLAY_MENU_IMAGE = pygame.image.load(os.path.join('Assets', 'Play_Menu.png'))
#PLAY_MENU_IMAGE = pygame.transform.scale(PLAY_MENU_IMAGE, (PLAY_MENU_IMAGE.get_width()*7, PLAY_MENU_IMAGE.get_height()*7))

GAME_MENU_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'Game_Menu.png'))
GAME_MENU_IMAGE = pygame.transform.scale(GAME_MENU_IMAGE, (WIDTH, HEIGHT))

HOME_MENU_IMAGE = pygame.image.load(os.path.join(current_path, 'Assets', 'Home_Menu.png'))
HOME_MENU_IMAGE = pygame.transform.scale(HOME_MENU_IMAGE, (WIDTH, HEIGHT))


#functions
def main():
    #Data
    State = 0
    Run = True

    while Run:
        #Setting the game screen update speed constant
        Clock.tick(FPS)

        #Iterating trough the list of events that occur in the game
        for event in pygame.event.get():
            #Verifying if we close the program
            if event.type == pygame.quit:
                Run = False
        
        #Running the game menu selection 
        if State != 1:
            State = home_menu(State)
        if State == 1:
            State = game_menu()

    #Quiting the game
    pygame.quit()
    sys.exit()

def check_win(num):
    global Grid

    # Check rows and columns
    for i in range(len(Grid)):
        if all(cell == num for cell in Grid[i]) or all(Grid[j][i] == num for j in range(len(Grid))):
            return True

    # Check main diagonal
    if all(Grid[i][i] == num for i in range(len(Grid))):
        return True

    # Check secondary diagonal
    if all(Grid[i][len(Grid)-i-1] == num for i in range(len(Grid))):
        return True

    return False

def draw_window(img, x, y):
    #Updating the display
    pygame.display.update()
    #Setting a image at a specific location on the screen
    WINDOW.blit(img, (x, y))

def home_menu(State):
    draw_window(HOME_MENU_IMAGE, 0, 0)
    draw_window(PLAY_BUTTON_IMAGE, WIDTH/3.18, HEIGHT/2.09)
    draw_window(QUIT_BUTTON_IMAGE, WIDTH/3.18, HEIGHT/1.76)
    if State == 2:
        draw_window(X_WON_MENU_IMAGE, 0, 0)
    if State == 3:
        draw_window(O_WON_MENU_IMAGE, 0, 0)

    # Wait for a mouse click event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if Play button was clicked
                if PLAY_BUTTON_IMAGE.get_rect(topleft=(WIDTH/3.18, HEIGHT/2.09)).collidepoint(mouse_pos):
                    return 1  # Change state to game menu

                # Check if Quit button was clicked
                elif QUIT_BUTTON_IMAGE.get_rect(topleft=(WIDTH/3.18, HEIGHT/1.76)).collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        Clock.tick(FPS)

def game_menu():
    draw_window(GAME_MENU_IMAGE, 0,0)
    draw_window(MENU_BUTTON_IMAGE, WIDTH/3.18, HEIGHT/1.12)
    aux = 0;
    global Grid

    #Drawing grid

    draw_window(DOT_IMAGE, WIDTH/12, HEIGHT/3.1)   #[0][0]
    draw_window(DOT_IMAGE, WIDTH/2.65, HEIGHT/3.1)  #[0][1]
    draw_window(DOT_IMAGE, WIDTH/1.49, HEIGHT/3.1)  #[0][2]
    

    draw_window(DOT_IMAGE, WIDTH/12, HEIGHT/2.05) #[1][0]
    draw_window(DOT_IMAGE, WIDTH/2.65, HEIGHT/2.05) #[1][1]
    draw_window(DOT_IMAGE, WIDTH/1.49, HEIGHT/2.05) #[1][2]

    draw_window(DOT_IMAGE, WIDTH/12, HEIGHT/1.52)   #[2][0]
    draw_window(DOT_IMAGE, WIDTH/2.65, HEIGHT/1.52) #[2][1]
    draw_window(DOT_IMAGE, WIDTH/1.49, HEIGHT/1.52)   #[2][2]

    # Wait for a mouse click event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if Quit button was clicked
                if MENU_BUTTON_IMAGE.get_rect(topleft=(WIDTH/3.18, HEIGHT/1.12)).collidepoint(mouse_pos):
                    Grid = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
                    return 0  # Change state to home menu
                
                #Checl grid
                elif DOT_IMAGE.get_rect(topleft=(WIDTH/12, HEIGHT/3.1)).collidepoint(mouse_pos) and Grid[0][0] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/12, HEIGHT/3.1)
                        Grid[0][0] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/12, HEIGHT/3.1)
                        Grid[0][0] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/2.65, HEIGHT/3.1)).collidepoint(mouse_pos) and Grid[0][1] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/2.65, HEIGHT/3.1)
                        Grid[0][1] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/2.65, HEIGHT/3.1)
                        Grid[0][1] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/1.49, HEIGHT/3.1)).collidepoint(mouse_pos) and Grid[0][2] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/1.49, HEIGHT/3.1)
                        Grid[0][2] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/1.49, HEIGHT/3.1)
                        Grid[0][2] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/12, HEIGHT/2.05)).collidepoint(mouse_pos) and Grid[1][0] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/12, HEIGHT/2.05)
                        Grid[1][0] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/12, HEIGHT/2.05)
                        Grid[1][0] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/2.65, HEIGHT/2.05)).collidepoint(mouse_pos) and Grid[1][1] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/2.65, HEIGHT/2.05)
                        Grid[1][1] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/2.65, HEIGHT/2.05)
                        Grid[1][1] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/1.49, HEIGHT/2.05)).collidepoint(mouse_pos) and Grid[1][2] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/1.49, HEIGHT/2.05)
                        Grid[1][2] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/1.49, HEIGHT/2.05)
                        Grid[1][2] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/12, HEIGHT/1.52)).collidepoint(mouse_pos) and Grid[2][0] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/12, HEIGHT/1.52)
                        Grid[2][0] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/12, HEIGHT/1.52)
                        Grid[2][0] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/2.65, HEIGHT/1.52)).collidepoint(mouse_pos) and Grid[2][1] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/2.65, HEIGHT/1.52)
                        Grid[2][1] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/2.65, HEIGHT/1.52)
                        Grid[2][1] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3

                elif DOT_IMAGE.get_rect(topleft=(WIDTH/1.49, HEIGHT/1.52)).collidepoint(mouse_pos) and Grid[2][2] == 0:
                    if aux == 1:
                        aux = 0
                        draw_window(X_IMAGE, WIDTH/1.49, HEIGHT/1.52)
                        Grid[2][2] = 1
                        if check_win(1):  # Check if 'X' has won
                            print("Player 'X' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 2
                    elif aux == 0:
                        aux = 1
                        draw_window(O_IMAGE, WIDTH/1.49, HEIGHT/1.52)
                        Grid[2][2] = 2
                        if check_win(2):  # Check if 'O' has won
                            print("Player 'O' has won!")
                            Grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            return 3
        pygame.display.update()
        Clock.tick(FPS)

#Checking if there exists a main function in the file that we just ran and executing the main function if so
if __name__ == "__main__":
    main()
