#sk-18da037f0d4e44388c36806465c0a11b

import speech_recognition as sr
import requests
import json
import sys

# ================= 配置区域 =================
DEEPSEEK_API_KEY = "sk-18da037f0d4e44388c36806465c0a11b" # ⚠️ 填入你的 Key
OUTPUT_FILENAME = "voice_circuit_v10.circ"
# ===========================================

def get_xml_template(components_xml):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="3.8.0" version="1.0">
  This file is intended to be loaded by Logisim-evolution v3.8.0(https://github.com/logisim-evolution/).
  <lib desc="#Wiring" name="0">
    <tool name="Pin"><a name="appearance" val="classic"/></tool>
    <tool name="Tunnel"><a name="facing" val="east"/></tool>
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
    <tool lib="1" name="NAND Gate"/>
    <tool lib="1" name="NOR Gate"/>
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
    print("   💎 Logisim 最终完美版 v10.0")
    print("   (精准区分 OR / NOR 的几何差异)")
    print("="*50)
    print("1. ⌨️  文本输入")
    print("2. 🎤 语音输入")
    c = input("选择: ").strip()
    if c == '2': return listen_command()
    return input("\n📝 请输入电路描述 (试一下: Multiplexer 2 to 1): ")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 正在听...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            print(f"✅ 收到: {text}")
            return text
        except: return None

def query_deepseek(prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    
    system_prompt = """
    You are a Circuit Topological Architect.
    Task: Convert description into a JSON list of components categorized by 'stage'.
    
    Rules:
    1. 'stage': 0 (Inputs), 1 (Logic Layer 1), 2 (Logic Layer 2), 3 (Outputs).
    2. 'inputs': List of net names.
    3. 'output': Result net name.
    
    Example for Mux 2-1:
    {
      "items": [
        {"type": "Pin", "stage": 0, "net": "A", "dir": "out"}, 
        {"type": "Pin", "stage": 0, "net": "B", "dir": "out"},
        {"type": "Pin", "stage": 0, "net": "S", "dir": "out"},
        {"type": "NOT Gate", "stage": 1, "inputs": ["S"], "output": "nS"},
        {"type": "AND Gate", "stage": 1, "inputs": ["A", "nS"], "output": "top"},
        {"type": "AND Gate", "stage": 1, "inputs": ["B", "S"], "output": "bot"},
        {"type": "OR Gate", "stage": 2, "inputs": ["top", "bot"], "output": "Y"},
        {"type": "Pin", "stage": 3, "net": "Y", "dir": "in"}
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
            
            if name == "Pin":
                net_name = item.get('net', 'unknown')
                is_input_pin = (item.get('dir') == 'out')
                if is_input_pin:
                    xml_body += generate_comp(0, "Pin", x, y, f'<a name="appearance" val="classic"/><a name="label" val="{net_name}"/>')
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="label" val="{net_name}"/>')
                else:
                    xml_body += generate_comp(0, "Pin", x, y, f'<a name="appearance" val="classic"/><a name="facing" val="west"/><a name="output" val="true"/><a name="label" val="{net_name}"/>')
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="facing" val="east"/><a name="label" val="{net_name}"/>')

            elif "Gate" in name:
                xml_body += generate_comp(1, name, x, y, "")
                
                inputs = item.get("inputs", [])
                
                # === v10.0 精确修正逻辑 ===
                # 默认偏移 (AND, OR, XOR)
                input_x_offset = -50 
                
                if name == "NOT Gate":
                    input_x_offset = -30
                # 检测“带圈”的门 (NAND, NOR, XNOR) -> 它们的身体更长，需要退更多
                elif name in ["NAND Gate", "NOR Gate", "XNOR Gate"]:
                    input_x_offset = -60
                # 普通门 (AND, OR, XOR) 保持 -50
                
                for idx, net in enumerate(inputs):
                    y_offset = -20 if idx == 0 else 20
                    if len(inputs) == 1: y_offset = 0
                    
                    xml_body += generate_comp(0, "Tunnel", x + input_x_offset, y + y_offset, f'<a name="facing" val="east"/><a name="label" val="{net}"/>')

                out_net = item.get("output")
                if out_net:
                    xml_body += generate_comp(0, "Tunnel", x, y, f'<a name="label" val="{out_net}"/>')

        full_content = get_xml_template(xml_body)
        with open(OUTPUT_FILENAME, "w") as f:
            f.write(full_content)
        print(f"\n🎉 v10.0 已生成！\n逻辑修正：OR Gate = -50, NOR Gate = -60。")
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