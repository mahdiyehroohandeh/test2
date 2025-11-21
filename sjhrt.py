import pygame
import sys

# راه اندازی pygame
pygame.init()

# تنظیمات صفحه
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ماشین در حال حرکت")

# رنگ‌ها
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# تنظیمات ماشین
car_width = 50
car_height = 30
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# حلقه اصلی بازی
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    
    # رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # حرکت ماشین
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    
    # محدود کردن حرکت ماشین در صفحه
    if car_x < 0:
        car_x = 0
    elif car_x > width - car_width:
        car_x = width - car_width
    
    # رسم ماشین
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    
    # بروزرسانی صفحه
    pygame.display.update()
    
    # تنظیم فریم ریت
    clock.tick(60)
