# -*- coding:utf-8 -*-
import sys  # 导入sys模块
import pygame  # 导入pygame模块

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色

ball = pygame.image.load("ball.png")  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed = [5, 5]  # 设置移动的X轴、Y轴距离

# 执行死循环，确保窗口一直显示
while True:

    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果点击关闭窗口，则退出
            sys.exit()

    ballrect = ballrect.move(speed)  # 移动小球

    screen.fill(color)  # 填充颜色
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame
