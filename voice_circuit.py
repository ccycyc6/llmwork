#sk-18da037f0d4e44388c36806465c0a11b

import speech_recognition as sr
import requests
import json
import sys

# ================= 配置区域 =================
DEEPSEEK_API_KEY = "sk-18da037f0d4e44388c36806465c0a11b" # ⚠️ 你的 Key
OUTPUT_FILENAME = "voice_circuit_v24_perfect.circ"
# ===========================================

def get_xml_template(components_xml):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="3.8.0" version="1.0">
  This file is intended to be loaded by Logisim-evolution v3.8.0(https://github.com/logisim-evolution/).

  <lib desc="#Wiring" name="0">
    <tool name="Pin">
      <a name="appearance" val="classic"/>
    </tool>
    <tool name="Tunnel">
      <a name="facing" val="east"/>
    </tool>
  </lib>
  <lib desc="#Gates" name="1"/>
  <lib desc="#Plexers" name="2"/>
  <lib desc="#Arithmetic" name="3"/>
  <lib desc="#Memory" name="4"/>
  <lib desc="#I/O" name="5"/>
  <lib desc="#Base" name="6"/>
  <main name="main"/>
  <options>
    <a name="gateUndefined" val="ignore"/>
    <a name="simlimit" val="1000"/>
    <a name="simrand" val="0"/>
  </options>
  <mappings>
    <tool lib="6" map="Button2" name="Poke Tool"/>
    <tool lib="6" map="Button3" name="Menu Tool"/>
    <tool lib="6" map="Ctrl Button1" name="Menu Tool"/>
  </mappings>
  <toolbar>
    <tool lib="6" name="Poke Tool"/>
    <tool lib="6" name="Edit Tool"/>
    <tool lib="6" name="Wiring Tool"/>
    <tool lib="6" name="Text Tool"/>
    <sep/>
    <tool lib="0" name="Pin"/>
    <tool lib="1" name="NOT Gate"/>
    <tool lib="1" name="AND Gate"/>
    <tool lib="1" name="OR Gate"/>
    <tool lib="1" name="XOR Gate"/>
    <tool lib="1" name="NAND Gate"/>
    <tool lib="1" name="NOR Gate"/>
    <sep/>
    <tool lib="2" name="Multiplexer"/>
    <sep/>
    <tool lib="4" name="D Flip-Flop"/>
  </toolbar>
  <circuit name="main">
    <a name="appearance" val="logisim_evolution"/>
    <a name="circuit" val="main"/>
    <a name="circuitnamedboxfixedsize" val="true"/>
    <a name="simulationFrequency" val="1.0"/>
    
{components_xml}
  </circuit>
</project>
"""

def get_user_input():
    print("\n" + "="*50)
    print("   👂 Logisim 从容对话版 v24.0")
    print("   (修复：二输入门引脚完美对齐)")
    print("="*50)
    print("1. ⌨️  文本输入")
    print("2. 🎤 语音输入 (中文)")
    c = input("选择: ").strip()
    if c == '2': return listen_command()
    return input("\n📝 请输入电路描述 (试一下: 做一个四位计数器): ")

def listen_command():
    r = sr.Recognizer()
    r.pause_threshold = 2.5 
    r.non_speaking_duration = 1.0 
    
    with sr.Microphone() as source:
        print("\n🎤 正在调整环境噪音... (请稍等)")
        r.adjust_for_ambient_noise(source, duration=0.8)
        print("🎤 请用中文说话 (你有充足的时间思考，说完后保持安静 2-3 秒)...")
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=15)
            print("⏳ 正在识别...")
            text = r.recognize_google(audio, language="zh-CN")
            print(f"✅ 识别结果: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ 没听清，请再说一遍")
            return None
        except sr.WaitTimeoutError:
            print("❌ 超时了，你好像没说话")
            return None
        except Exception as e:
            print(f"❌ 错误: {e}")
            return None

def query_deepseek(prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    
    system_prompt = """
    You are a Digital Logic Architect.
    Task: Convert description into a JSON list of components.
    
    Key Concepts:
    1. Combinational Logic (Gates): lib=1.
    2. Sequential Logic (Memory): lib=4. Use "D Flip-Flop".
    3. Stages: 0 (Inputs), 1-2 (Next State Logic), 3 (Flip-Flops), 4 (Outputs).
    
    IMPORTANT for Counters:
    - You MUST include a "D Flip-Flop" for each bit.
    - Flip-Flop Inputs: ["D_i", "CLK", "RST"]
    - Flip-Flop Output: "Q_i"
    - The Logic calculates D_i based on current Q_i.
    
    JSON Example (2-bit Counter):
    {
      "items": [
        {"type": "Pin", "stage": 0, "net": "CLK", "dir": "out"},
        {"type": "Pin", "stage": 0, "net": "RST", "dir": "out"},
        
        {"type": "XOR Gate", "stage": 1, "inputs": ["Q0", "EN"], "output": "D0"},
        {"type": "XOR Gate", "stage": 1, "inputs": ["Q1", "D0"], "output": "D1"},
        
        {"type": "D Flip-Flop", "stage": 3, "inputs": ["D0", "CLK", "RST"], "output": "Q0"},
        {"type": "D Flip-Flop", "stage": 3, "inputs": ["D1", "CLK", "RST"], "output": "Q1"},
        
        {"type": "Pin", "stage": 4, "net": "Q0", "dir": "in"},
        {"type": "Pin", "stage": 4, "net": "Q1", "dir": "in"}
      ]
    }
    """

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Design: {prompt}"}
        ],
        "stream": False,
        "response_format": {"type": "json_object"}
    }
    
    try:
        r = requests.post(url, headers=headers, json=data)
        return r.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {e}")
        return None

def generate_comp(lib, name, x, y, attrs=""):
    return f'    <comp lib="{lib}" loc="({x},{y})" name="{name}">{attrs}</comp>\n'

def generate_circuit_file(json_str):
    try:
        data = json.loads(json_str)
        xml_body = ""
        stage_counts = {} 
        
        for item in data.get('items', []):
            stage = item.get('stage', 0)
            x = 100 + (stage * 300)
            count = stage_counts.get(stage, 0)
            y = 100 + (count * 120)
            stage_counts[stage] = count + 1
            
            name = item['type']
            
            # 1. Pin
            if name == "Pin":
                net_name = item.get('net', 'unknown')
                is_input_pin = (item.get('dir') == 'out')
                if is_input_pin:
                    xml_body += generate_comp(0, "Pin", x, y, f'<a name="appearance" val="classic"/><a name="label" val="{net_name}"/>')
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="label" val="{net_name}"/>')
                else:
                    xml_body += generate_comp(0, "Pin", x, y, f'<a name="appearance" val="classic"/><a name="facing" val="west"/><a name="output" val="true"/><a name="label" val="{net_name}"/>')
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="facing" val="east"/><a name="label" val="{net_name}"/>')

            # 2. Gates
            elif "Gate" in name:
                inputs = item.get("inputs", [])
                num_inputs = len(inputs)
                
                gate_attrs = ""
                input_x_offset = -50
                
                if name == "NOT Gate": 
                    input_x_offset = -30
                    num_inputs = 1
                else:
                    # Size 70 宽门
                    gate_attrs += '<a name="size" val="70"/>'
                    input_x_offset = -70
                    
                    # 几何修正
                    if name in ["NAND Gate", "NOR Gate", "XOR Gate", "XNOR Gate"]: 
                        input_x_offset = -80
                    
                    if num_inputs > 2:
                        gate_attrs += f'<a name="inputs" val="{num_inputs}"/>'
                
                xml_body += generate_comp(1, name, x, y, gate_attrs)
                
                # 输入隧道排列
                for idx, net in enumerate(inputs):
                    if name == "NOT Gate":
                        y_offset = 0
                    
                    # === ⚡️ 核心修复区域 ⚡️ ===
                    # 对于 Size=70 的门，2输入其实是 -20 和 +20
                    # 之前设置的 -30/+30 会导致引脚悬空
                    elif num_inputs == 2:
                        y_offset = -20 if idx == 0 else 20 
                    
                    # 多输入门
                    else:
                        y_offset = (idx * 20) - ((num_inputs - 1) * 10)
                    
                    xml_body += generate_comp(0, "Tunnel", x + input_x_offset, y + y_offset, f'<a name="facing" val="east"/><a name="label" val="{net}"/>')
                
                if item.get("output"):
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="label" val="{item["output"]}"/>')

            # 3. Flip-Flop
            elif "Flip-Flop" in name:
                xml_body += generate_comp(4, name, x, y, '<a name="appearance" val="logisim_evolution"/>')
                inputs = item.get("inputs", [])
                
                if len(inputs) > 0: xml_body += generate_comp(0, "Tunnel", x - 10, y + 10, f'<a name="facing" val="east"/><a name="label" val="{inputs[0]}"/>')
                if len(inputs) > 1: xml_body += generate_comp(0, "Tunnel", x - 10, y + 50, f'<a name="facing" val="east"/><a name="label" val="{inputs[1]}"/>')
                if len(inputs) > 2: xml_body += generate_comp(0, "Tunnel", x + 20, y + 60, f'<a name="facing" val="north"/><a name="label" val="{inputs[2]}"/>')
                
                out_net = item.get("output")
                if out_net:
                    xml_body += generate_comp(0, "Tunnel", x + 50, y + 10, f'<a name="label" val="{out_net}"/>')

        full_content = get_xml_template(xml_body)
        with open(OUTPUT_FILENAME, "w") as f:
            f.write(full_content)
        print(f"\n🎉 v24.0 生成完毕！")
        print(f"🔧 修复：2输入门引脚偏移已恢复为标准的 -20 和 +20，现在应该能完美对齐了。")
        print(f"📁 文件: {OUTPUT_FILENAME}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        print(json_str)

if __name__ == "__main__":
    cmd = get_user_input()
    if cmd:
        print(f"🤖 设计中: '{cmd}' ...")
        res = query_deepseek(cmd)
        if res: generate_circuit_file(res)