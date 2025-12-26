import pygame
from constants import *

class LogicGate:
    def __init__(self, gate_type, x, y, is_in_toolbox=False):
        self.type = gate_type
        self.rect = pygame.Rect(x, y, 100, 60)
        self.is_in_toolbox = is_in_toolbox
        self.id = f"{gate_type}_{id(self)}"
        
        # === 新增：组件状态 ===
        self.state = False # False=0/Off, True=1/On
        self.output_value = False # 输出电平

        # 端口布局
        self.input_nodes = []
        self.output_nodes = []
        
        if gate_type in ["AND", "OR", "XOR"]:
            self.input_nodes = [(0, 15), (0, 45)]
            self.output_nodes = [(100, 30)]
        elif gate_type == "NOT":
            self.input_nodes = [(0, 30)]
            self.output_nodes = [(100, 30)]
        elif gate_type == "SWITCH": # 输入设备
            self.output_nodes = [(100, 30)]
            self.color_on = COLOR_NEON_GREEN
            self.color_off = COLOR_ALERT_RED
        elif gate_type == "BULB":   # 输出设备
            self.input_nodes = [(0, 30)]

    def toggle(self):
        """点击开关时切换状态"""
        if self.type == "SWITCH":
            self.state = not self.state

    def draw(self, screen):
        # 1. 动态决定颜色
        border_color = COLOR_CYAN
        fill_color = COLOR_CHIP_BODY

        if self.is_in_toolbox:
            border_color = (100, 100, 100)
        else:
            # 如果是开关，根据状态变色
            if self.type == "SWITCH":
                fill_color = self.color_on if self.state else self.color_off
            # 如果是灯泡，根据输入通电变亮
            elif self.type == "BULB":
                fill_color = COLOR_NEON_GREEN if self.state else (30, 30, 30)

        # 2. 绘制主体
        pygame.draw.rect(screen, fill_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, border_color, self.rect, 2, border_radius=10)

        # 3. 绘制文字
        font = pygame.font.SysFont('Arial', 20, bold=True)
        label = self.type
        if self.type == "SWITCH": label = "ON" if self.state else "OFF"
        
        text_color = COLOR_WHITE
        if self.type == "BULB" and self.state: text_color = (0, 0, 0) # 灯亮了字变黑
        
        text = font.render(label, True, text_color)
        screen.blit(text, text.get_rect(center=self.rect.center))

        # 4. 绘制端口
        for ix, iy in self.input_nodes:
            # 输入口：白色
            pygame.draw.circle(screen, COLOR_WHITE, (self.rect.x + ix, self.rect.y + iy), 8)
            
        for ox, oy in self.output_nodes:
            # 输出口：如果组件输出高电平，或者是开启的开关，显示绿色
            node_color = COLOR_NEON_GREEN 
            pygame.draw.circle(screen, node_color, (self.rect.x + ox, self.rect.y + oy), 8)

    def update_pos(self, x, y):
        self.rect.center = (x, y)

    def clone(self, x, y):
        return LogicGate(self.type, x, y, is_in_toolbox=False)

    def get_abs_input_nodes(self):
        return [(self.rect.x + x, self.rect.y + y, i) for i, (x, y) in enumerate(self.input_nodes)]

    def get_abs_output_nodes(self):
        return [(self.rect.x + x, self.rect.y + y, i) for i, (x, y) in enumerate(self.output_nodes)]

class Wire:
    def __init__(self, start_gate, start_idx, end_gate, end_idx):
        self.start_gate = start_gate
        self.start_idx = start_idx
        self.end_gate = end_gate
        self.end_idx = end_idx
        self.is_active = False # 是否通电

    def draw(self, screen):
        try:
            start_pos = self.start_gate.get_abs_output_nodes()[self.start_idx][:2]
            end_pos = self.end_gate.get_abs_input_nodes()[self.end_idx][:2]
            
            # 如果通电了，线变亮，变粗
            color = COLOR_NEON_GREEN if self.is_active else COLOR_WIRE_OFF
            width = 4 if self.is_active else 2
            
            pygame.draw.line(screen, color, start_pos, end_pos, width)
            pygame.draw.circle(screen, color, start_pos, 5)
            pygame.draw.circle(screen, color, end_pos, 5)
        except:
            pass