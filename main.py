# ---------------------------------------------- imports
import pygame

# ---------------------------------------------- variables
running = True
left_x = 50
right_x = 100
add_x = 3
add_y = 1

right_up = False
right_down = False

left_up = False
left_down = False

left_points = 0
right_points = 0

r, g, b = 242, 91, 53


# ---------------------------------------------- main game function
def play():
    pygame.init()  # initialize pygame

    global running, left_x, right_x, add_x, add_y, right_up, right_down, left_down, left_up, r, g, b, left_points, right_points  # global variables

    # ----------------------------------- Game Window
    window = pygame.display.set_mode((800, 600))  # initialise screen
    window.fill((r, g, b))

    left_paddle = pygame.Rect(30, left_x, 20, 100)
    right_paddle = pygame.Rect(750, right_x, 20, 100)

    ball = pygame.Rect(400, 300, 20, 20)
    ball_image = pygame.image.load('assets/ball.png').convert()
    ball_image = pygame.transform.smoothscale(ball_image, (30, 30))

    clock = pygame.time.Clock()

    def draw_paddles():
        if left_paddle.bottom >= 600:
            left_paddle.bottom = 600
        if left_paddle.top <= 0:
            left_paddle.top = 0
        if right_paddle.bottom >= 600:
            right_paddle.bottom = 600
        if right_paddle.top <= 0:
            right_paddle.top = 0

        # ----------------------------------- left paddle
        pygame.draw.rect(window, (255, 255, 255), left_paddle)

        # ----------------------------------- right paddle
        pygame.draw.rect(window, (255, 255, 255), right_paddle)
    draw_paddles()

    def draw_ball():
        global add_x, add_y

        ball.x += add_x
        ball.y += add_y

        if ball.right >= 800:
            add_x *= -1
        if ball.left <= 0:
            add_x *= -1
        if ball.bottom >= 600 or ball.top <= 0:
            add_y *= -1

        window.fill((r, g, b))

        draw_paddles()

        window.blit(ball_image, ball)

    # ----------------------------------- functions
    def check_collision():
        global add_y, add_x

        # -------------------------------------- check right paddle collision
        collide_right = ball.colliderect(right_paddle)
        if collide_right:
            if abs(right_paddle.top - ball.bottom) < 10:
                add_y *= -1
            if abs(right_paddle.bottom - ball.top) < 10:
                add_y *= -1
            if abs(right_paddle.left - ball.right) < 10:
                add_x *= -1
            if abs(right_paddle.right - ball.left) < 10:
                add_x *= -1

        # -------------------------------------- check left paddle collision
        collide_left = ball.colliderect(left_paddle)
        if collide_left:
            if abs(left_paddle.top - ball.bottom) < 10:
                add_y *= -1
            if abs(left_paddle.bottom - ball.top) < 10:
                add_y *= -1
            if abs(left_paddle.left - ball.right) < 10:
                add_x *= -1
            if abs(left_paddle.right - ball.left) < 10:
                add_x *= -1

    add_to_paddle = 3

    # ----------------- move up
    def move_right_paddle_up():
        global right_x  # global variables

        right_paddle.y -= add_to_paddle
        draw_paddles()
        window.fill((r, g, b))

    def move_left_paddle_up():
        global left_x  # global variables

        left_paddle.y -= add_to_paddle
        draw_paddles()
        window.fill((r, g, b))

    # ----------------- move down
    def move_right_paddle_down():
        global right_x  # global variables

        right_paddle.y += add_to_paddle
        draw_paddles()
        window.fill((r, g, b))

    def move_left_paddle_down():
        global left_x  # global variables

        left_paddle.y += add_to_paddle
        draw_paddles()
        window.fill((r, g, b))

    while running:  # main while loop
        for event in pygame.event.get():
            # ---------- Quit Window
            if event.type == pygame.QUIT:  # Quit window if close button pressed
                running = False
            # ---------- Track Buttons
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape Button Quit Window
                    running = False
                if event.key == pygame.K_UP:  # Escape Button Quit Window
                    right_up = True
                if event.key == pygame.K_w:  # Escape Button Quit Window
                    left_up = True
                if event.key == pygame.K_DOWN:  # Escape Button Quit Window
                    right_down = True
                if event.key == pygame.K_s:  # Escape Button Quit Window
                    left_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:  # Escape Button Quit Window
                    right_up = False
                if event.key == pygame.K_DOWN:  # Escape Button Quit Window
                    right_down = False
                if event.key == pygame.K_w:  # Escape Button Quit Window
                    left_up = False
                if event.key == pygame.K_s:  # Escape Button Quit Window
                    left_down = False

        if right_up:
            move_right_paddle_up()
        if right_down:
            move_right_paddle_down()
        if left_up:
            move_left_paddle_up()
        if left_down:
            move_left_paddle_down()

        draw_paddles()
        draw_ball()
        check_collision()

        pygame.display.update()  # update screen

        clock.tick(120)


# ---------------------------------------------- required if statement
if __name__ == "__main__":
    play()
