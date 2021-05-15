# ---------------------------------------------- imports
import pygame

# ---------------------------------------------- variables
running = True


# ---------------------------------------------- main game function
def play():
    pygame.init()  # initialize pygame

    global running  # global variables

    # ---------------------- Game Window
    window = pygame.display.set_mode((800, 450))  # initialise screen

    while running:  # main while loop
        for event in pygame.event.get():
            # ---------- Quit Window
            if event.type == pygame.QUIT:  # Quit window if close button pressed
                running = False
            # ---------- Track Buttons
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape Button Quit Window
                    running = False

        pygame.display.update()  # update screen


# ---------------------------------------------- required if statement
if __name__ == "__main__":
    play()
