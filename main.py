import cv2
import pygame
import numpy as np
import math
from hand_tracker import HandTracker
from circuit_components import LogicGate, Wire
from ui_manager import UIManager
from constants import *
from deepseek_brain import CircuitBrain

# ... (simulate_circuit 函数保持不变) ...
def simulate_circuit(gates, wires):
    for g in gates:
        if g.type != "SWITCH":
            g.state = False
            g.output_value = False
    
    for _ in range(3): 
        for g in gates:
            input_values = [False, False]
            connected_wires = [w for w in wires if w.end_gate == g]
            for w in connected_wires:
                source = w.start_gate
                if source.type == "SWITCH": w.is_active = source.state
                else: w.is_active = source.output_value
                if w.end_idx < 2: input_values[w.end_idx] = w.is_active

            if g.type == "AND": g.output_value = input_values[0] and input_values[1]
            elif g.type == "OR": g.output_value = input_values[0] or input_values[1]
            elif g.type == "NOT": g.output_value = not input_values[0]
            elif g.type == "BULB": g.state = input_values[0]

# 增大吸附判定范围
SNAP_THRESHOLD = 40 

def get_distance(pt1, pt2):
    return math.hypot(pt1[0]-pt2[0], pt1[1]-pt2[1])

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("AetherCircuits: Magnetic Snapping")
    
    cap = cv2.VideoCapture(0)
    cap.set(3, SCREEN_WIDTH)
    cap.set(4, SCREEN_HEIGHT)

    tracker = HandTracker()
    ui = UIManager()
    brain = CircuitBrain("YOUR_KEY")

    toolbox_gates = [
        LogicGate("SWITCH", 60, 100, True),
        LogicGate("AND", 60, 200, True),
        LogicGate("OR", 60, 300, True),
        LogicGate("NOT", 60, 400, True),
        LogicGate("BULB", 60, 500, True)
    ]
    active_gates = []
    wires = []
    
    dragging_gate = None
    wire_start_node = None     # (gate, idx, type, abs_pos)
    snap_target_candidate = None # === 新增：当前被吸附的目标 ===
    
    toggle_cooldown = 0 
    clock = pygame.time.Clock()
    running = True

    while running:
        success, img = cap.read()
        if not success: break
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        tracker.find_hands(img)
        pointer_pos, is_pinching = tracker.get_pointer_position(SCREEN_WIDTH, SCREEN_HEIGHT)
        simulate_circuit(active_gates, wires)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                active_gates = []
                wires = []

        # === 实时计算吸附候选点 (Visual Snapping Logic) ===
        snap_target_candidate = None # 每帧重置
        if pointer_pos and wire_start_node: # 只有在拉线的时候才计算吸附
            start_gate = wire_start_node[0]
            
            # 遍历场上所有组件的 INPUT 端口
            for gate in active_gates:
                if gate == start_gate: continue # 不能连自己
                
                inputs = gate.get_abs_input_nodes()
                for idx, (nx, ny, _) in enumerate(inputs):
                    # 如果手指进入了某个端口的磁吸范围
                    if get_distance(pointer_pos, (nx, ny)) < SNAP_THRESHOLD:
                        snap_target_candidate = (gate, idx, (nx, ny))
                        break # 找到一个就停止
                if snap_target_candidate: break

        # === 交互逻辑 ===
        if pointer_pos:
            cx, cy = pointer_pos
            
            # 1. 点击开关
            if is_pinching and toggle_cooldown == 0 and not dragging_gate and not wire_start_node:
                for g in active_gates:
                    if g.type == "SWITCH" and g.rect.collidepoint(cx, cy):
                        g.toggle()
                        toggle_cooldown = 30
                        break
            if toggle_cooldown > 0: toggle_cooldown -= 1

            # 2. 状态机处理
            if is_pinching:
                # --- 开始阶段 ---
                if (dragging_gate is None) and (wire_start_node is None):
                    # 优先检测是不是要从 Output 拉线
                    found_output = False
                    for gate in active_gates:
                        outputs = gate.get_abs_output_nodes()
                        for idx, (nx, ny, _) in enumerate(outputs):
                            if get_distance((cx, cy), (nx, ny)) < SNAP_THRESHOLD:
                                wire_start_node = (gate, idx, "output", (nx, ny))
                                found_output = True
                                break
                        if found_output: break
                    
                    # 如果不是拉线，那就是抓取组件
                    if not found_output:
                        # 先看工具栏
                        if cx < SIDEBAR_WIDTH:
                            for gate in toolbox_gates:
                                if gate.rect.collidepoint(cx, cy):
                                    new_gate = gate.clone(cx, cy)
                                    active_gates.append(new_gate)
                                    dragging_gate = new_gate
                                    break
                        # 再看场上组件
                        else:
                            for gate in active_gates:
                                if gate.rect.collidepoint(cx, cy):
                                    dragging_gate = gate
                                    break
                
                # --- 拖动阶段 ---
                elif dragging_gate:
                    dragging_gate.update_pos(cx, cy)
                
                # elif wire_start_node: 
                # 这里不需要做逻辑，因为吸附计算已经在上面做了

            # 3. 松开处理 (Release)
            elif not is_pinching:
                # 放置组件
                if dragging_gate:
                    if dragging_gate.rect.centerx < SIDEBAR_WIDTH:
                        if dragging_gate in active_gates:
                            active_gates.remove(dragging_gate)
                            wires = [w for w in wires if w.start_gate != dragging_gate and w.end_gate != dragging_gate]
                    dragging_gate = None
                
                # 完成连线
                if wire_start_node:
                    # 如果松手时，有一个有效的吸附候选点
                    if snap_target_candidate:
                        start_gate, start_idx, _, _ = wire_start_node
                        end_gate, end_idx, _ = snap_target_candidate
                        
                        # 创建连线 (去重)
                        already_exists = any(w.end_gate == end_gate and w.end_idx == end_idx for w in wires)
                        if not already_exists:
                            wires.append(Wire(start_gate, start_idx, end_gate, end_idx))
                    
                    wire_start_node = None # 结束连线状态

        # === 渲染层 ===
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_surface = pygame.surfarray.make_surface(np.rot90(img_rgb))
        screen.blit(pygame.transform.flip(img_surface, True, False), (0, 0))

        ui.draw_sidebar(screen, toolbox_gates)
        for w in wires: w.draw(screen)
        for g in active_gates: g.draw(screen)

        # === 绘制交互反馈 (关键视觉升级) ===
        if wire_start_node and pointer_pos:
            # 起点固定
            start_pos = wire_start_node[0].get_abs_output_nodes()[wire_start_node[1]][:2]
            
            # 终点逻辑：如果有吸附对象，线就连到对象上；否则跟随手指
            if snap_target_candidate:
                target_pos = snap_target_candidate[2] # 吸附目标的坐标
                
                # 1. 绘制锁定光环
                pygame.draw.circle(screen, COLOR_WHITE, target_pos, 15, 2) 
                
                # 2. 线直接连到目标上 (磁性效果)
                pygame.draw.line(screen, COLOR_WHITE, start_pos, target_pos, 3)
            else:
                # 正常跟随手指
                pygame.draw.line(screen, (200, 200, 200), start_pos, pointer_pos, 2)
                pygame.draw.circle(screen, COLOR_WHITE, pointer_pos, 5)

        if pointer_pos:
            ui.draw_cursor(screen, pointer_pos, is_pinching)

        pygame.display.flip()
        clock.tick(60)

    cap.release()
    pygame.quit()

if __name__ == "__main__":
    main()