import pygame
from constants import *

class UIManager:
    def __init__(self):
        # 侧边栏背景 (带透明度)
        self.sidebar_surf = pygame.Surface((SIDEBAR_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.sidebar_surf.fill(COLOR_BG_DARK)
        
        # 底部栏背景
        self.bottom_surf = pygame.Surface((SCREEN_WIDTH - SIDEBAR_WIDTH, 60), pygame.SRCALPHA)
        self.bottom_surf.fill((0, 0, 0, 180)) # 深黑底色

    def draw_sidebar(self, screen, toolbox_gates):
        screen.blit(self.sidebar_surf, (0, 0))
        
        # 绘制标题
        font = pygame.font.SysFont('Arial', 24, bold=True)
        title = font.render("COMPONENTS", True, COLOR_CYAN)
        screen.blit(title, (20, 20))
        
        pygame.draw.line(screen, COLOR_CYAN, (20, 50), (180, 50), 2)

        # 绘制工具栏里的组件
        for gate in toolbox_gates:
            gate.draw(screen)

    def draw_feedback(self, screen, message):
        # 绘制底部栏
        screen.blit(self.bottom_surf, (SIDEBAR_WIDTH, SCREEN_HEIGHT - 60))
        
        # 绘制文字
        font = pygame.font.SysFont('Consolas', 20) # 编程字体
        text = font.render(f"> SYSTEM: {message}", True, COLOR_NEON_GREEN)
        screen.blit(text, (SIDEBAR_WIDTH + 20, SCREEN_HEIGHT - 40))

    def draw_cursor(self, screen, pos, is_pinching):
        # 绘制科幻风格的光标
        color = COLOR_NEON_GREEN if is_pinching else COLOR_CYAN
        x, y = pos
        
        # 十字准星
        pygame.draw.line(screen, color, (x - 15, y), (x + 15, y), 2)
        pygame.draw.line(screen, color, (x, y - 15), (x, y + 15), 2)
        
        if is_pinching:
            pygame.draw.circle(screen, color, (x, y), 20, 2)