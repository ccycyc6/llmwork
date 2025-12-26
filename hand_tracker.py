import cv2
import mediapipe as mp
import math

# === 保持之前的 import 修复 ===
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing

class HandTracker:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp_drawing
        self.is_pinching = False # 记录上一帧状态

    def find_hands(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        return self.results

    def get_pointer_position(self, img_width, img_height):
        if self.results.multi_hand_landmarks:
            hand_lms = self.results.multi_hand_landmarks[0]
            index_finger = hand_lms.landmark[8]
            thumb = hand_lms.landmark[4]
            
            cx, cy = int(index_finger.x * img_width), int(index_finger.y * img_height)
            t_x, t_y = int(thumb.x * img_width), int(thumb.y * img_height)
            
            distance = math.hypot(t_x - cx, t_y - cy)
            
            # === 优化重点：迟滞阈值 (Hysteresis) ===
            # 如果之前没捏，距离 < 30 才算捏
            # 如果之前捏了，距离 > 50 才算松开
            # 这样创造了一个 20px 的“稳定区”
            if not self.is_pinching and distance < 30:
                self.is_pinching = True
            elif self.is_pinching and distance > 50:
                self.is_pinching = False
                
            return (cx, cy), self.is_pinching
            
        return None, False