import pygame
import sys
from pygame.locals import *

import time
   
pygame.init()

# 캐릭터 속도와 점프 변수 설정
xs = -50
ys = 0
jup = 0
f = 10
sec = 1

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# 패들(캐릭터) 설정
paddle = pygame.Rect(930, 900, 30, 70)
paddle_dy = 60
paddle_dx = 0

# 벽돌 설정
bricks = [pygame.Rect(60 + 200 * i, 999 + 200 * j, 200, 19) for i in range(10) for j in range(1)]

def game_over():
    draw_text("GAME OVER", 48, screen.get_width() / 2, screen.get_height() / 2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xs -= 2
    if keys[pygame.K_RIGHT]:
        xs += 2
    if keys[pygame.K_UP] and hit_index != -1:
        jup = 15

    # 점프 처리
    if jup > 0:
        ys = -25
        jup = jup - 1

    # 캐릭터 위치 업데이트
    paddle.top += paddle_dy
    paddle_dy = ys

    # 중력 적용: 캐릭터가 공중에 있을 때 중력 추가
    if ys < 30:
        ys += 1

    # 벽돌과 충돌 처리
    hit_index = paddle.collidelist(bricks)  # 패들이 벽돌과 충돌하는지 확인
    if hit_index != -1:  # 벽돌에 충돌했을 때
        # 벽돌과 충돌했을 때 캐릭터를 벽돌 위에 고정
        paddle.bottom = bricks[hit_index].top
        ys = 0  # Y축 속도를 0으로 설정하여 멈추게 함
        jup = 0  # 점프 중단

        # 마찰력 적용 (벽돌에 닿았을 때 X축 속도를 점점 줄임)
        xs *= 0.8  # 마찰력에 의해 X축 속도를 감소시킴
    
    # 벽과 충돌 처리: 패들이 화면 좌우 벽에 닿으면 반사되도록 함
    if paddle.left <= 0:  # 화면의 왼쪽 벽에 닿을 때
        paddle.left = 0  # 화면 밖으로 나가지 않게 고정
        xs = -xs  # 반사 효과 (속도 방향 반전)
    elif paddle.right >= screen_width:  # 화면의 오른쪽 벽에 닿을 때
        paddle.right = screen_width  # 화면 밖으로 나가지 않게 고정
        xs = -xs  # 반사 효과 (속도 방향 반전)

    # 캐릭터의 X축 이동 처리
    paddle.left += xs

    # 화면 그리기
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (50, 255, 255), paddle)
    for brick in bricks:
        pygame.draw.rect(screen, (250, 250, 250), brick)

    pygame.display.flip()

    # 공중에서는 X축 속도 감소 (마찰과 비슷하게 구현)
    if hit_index == -1:  # 벽돌과 충돌하지 않았을 때도 X축 속도가 감소하도록 마찰력 비슷한 효과
        xs *= 0.99  # 공중에서 마찰에 의해 조금씩 속도가 줄어듦

    pygame.time.delay(10)
