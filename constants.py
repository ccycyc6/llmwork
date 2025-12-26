import pygame

# === 修改这里：加大窗口尺寸 ===
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SIDEBAR_WIDTH = 250 # 侧边栏也宽一点

# 配色方案
COLOR_BG_DARK = (10, 20, 30, 200)
COLOR_CYAN = (0, 255, 255)       # 正常状态
COLOR_NEON_GREEN = (57, 255, 20) # 高电平/通电
COLOR_ALERT_RED = (255, 50, 50)  # 低电平/断电
COLOR_WHITE = (255, 255, 255)
COLOR_CHIP_BODY = (40, 40, 50)
COLOR_WIRE_OFF = (100, 100, 100) # 没通电的线是灰色的