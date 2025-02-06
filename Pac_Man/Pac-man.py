import pygame
import sys

pygame.init()

Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("吃豆人")

# 定义颜色
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# 网格设置
TILE_SIZE = 40
ROWS = Height // TILE_SIZE  # 10
COLS = Width // TILE_SIZE   # 15

# 初始化地图，每个格子都有豆子（值为1）
game_map = [[1 for _ in range(COLS)] for _ in range(ROWS)]

# 定义吃豆人的属性
pacman_radius = 20
pacman_x = Width // 2
pacman_y = Height // 2
pacman_speed = 5

clock = pygame.time.Clock()

running  = True


def draw_map():
    # 遍历地图，每个格子绘制豆子
    for row in range(ROWS):
        for col in range(COLS):
            if game_map[row][col] == 1:
                # 计算豆子中心位置（在当前格子的中间）
                center_x = col * TILE_SIZE + TILE_SIZE // 2
                center_y = row * TILE_SIZE + TILE_SIZE // 2
                # 绘制小豆子（半径为4）
                pygame.draw.circle(screen, WHITE, (center_x, center_y), 4)


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # function of QUIT
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
    pacman_x = max(pacman_radius, min(Width - pacman_radius, pacman_x))
    pacman_y = max(pacman_radius, min(Height - pacman_radius, pacman_y))

    # 绘制场景
    screen.fill(BLACK)

    # 绘制吃豆人（一个圆形）
    draw_map()
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    pygame.display.flip()

pygame.quit()
sys.exit()
