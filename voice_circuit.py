#sk-18da037f0d4e44388c36806465c0a11b

import speech_recognition as sr
import requests
import json
import sys
import os
import subprocess
import re


DEEPSEEK_API_KEY = "sk-18da037f0d4e44388c36806465c0a11b" 
OUTPUT_FILENAME = "voice_circuit_v24_perfect.circ"
OUTPUT_VERILOG_FILENAME = "voice_circuit_output.v"
OUTPUT_CPP_FILENAME = "sim_main.cpp" 



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

# ==========================================
# 🚀 新增功能区：Verilator 自动化仿真逻辑
# ==========================================

def extract_module_name(verilog_code):
    """从 Verilog 代码中提取模块名"""
    match = re.search(r"module\s+(\w+)", verilog_code)
    if match:
        return match.group(1)
    return "top"

def run_verilator_sim(verilog_filename, cpp_filename, module_name):
    """调用 Verilator 进行编译和仿真"""
    print(f"\n🚀 开始 Verilator 自动化仿真流程...")
    
    # 1. 清理旧文件
    if os.path.exists("obj_dir"):
        subprocess.run(["rm", "-rf", "obj_dir"])
    if os.path.exists("wave.fst"):
        os.remove("wave.fst")

    # 2. 构造 Verilator 编译命令
    # ⚡️ 关键修正：添加 --top-module 确保 .h 文件名正确
    cmd_build = [
        "verilator",
        "--top-module", module_name, 
        "--cc",
        "--exe",
        "--trace-fst",  # 生成 FST 波形
        "--build",      # 自动调用 make
        "-o", "sim_main",
        "-Wno-fatal",
        verilog_filename,
        cpp_filename
    ]
    
    print(f"🔧 编译中: {' '.join(cmd_build)}")
    try:
        # 执行编译
        result = subprocess.run(cmd_build, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print("❌ Verilator 编译失败:")
            print(result.stderr)
            return

        print("✅ 编译成功！")

        # 3. 运行仿真
        sim_executable = os.path.join("obj_dir", "sim_main")
        print(f"▶️  运行仿真: {sim_executable}")
        
        sim_result = subprocess.run([sim_executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if sim_result.returncode != 0:
            print("❌ 仿真运行错误:")
            print(sim_result.stderr)
        else:
            print("✅ 仿真完成！")
            if os.path.exists("wave.fst"):
                print(f"📉 波形文件已生成: {os.path.abspath('wave.fst')}")
                print("💡 提示: 使用 'gtkwave wave.fst' 查看波形")
            else:
                print("⚠️ 警告: 未找到 wave.fst，请检查 C++ 代码是否正确调用了 dump")

    except FileNotFoundError:
        print("❌ 错误: 未找到 'verilator' 命令，请确保已安装 Verilator。")
    except Exception as e:
        print(f"❌ 未知错误: {e}")

def save_verilog_and_sim(json_str):
    """保存 Verilog，生成 Testbench 并运行仿真"""
    try:
        data = json.loads(json_str)
        verilog_code = data.get("verilog_code", "")
        
        if not verilog_code:
            print("❌ 生成失败：AI 未返回有效的 Verilog 代码")
            return

        # 1. 保存 Verilog
        with open(OUTPUT_VERILOG_FILENAME, "w", encoding="utf-8") as f:
            f.write(verilog_code)
        print(f"\n📄 Verilog 代码已保存: {OUTPUT_VERILOG_FILENAME}")
        
        # 2. 提取模块名
        module_name = extract_module_name(verilog_code)
        print(f"🔍 识别模块名: {module_name}")

        # 3. 请求 AI 生成对应的 C++ Testbench
        print("🤖 正在生成 C++ Testbench (main.cpp) ...")
        # 调用 deepseek 生成 testbench
        cpp_code = query_deepseek(verilog_code, mode="cpp_tb", extra_context=module_name)
        
        if cpp_code:
            cpp_json = json.loads(cpp_code)
            actual_cpp = cpp_json.get("cpp_code", "")
            
            with open(OUTPUT_CPP_FILENAME, "w", encoding="utf-8") as f:
                f.write(actual_cpp)
            print(f"📄 C++ 仿真驱动已保存: {OUTPUT_CPP_FILENAME}")
            
            # 4. 执行 Verilator 仿真
            run_verilator_sim(OUTPUT_VERILOG_FILENAME, OUTPUT_CPP_FILENAME, module_name)
        
    except Exception as e:
        print(f"❌ 流程错误: {e}")
        print("原始数据:", json_str)

# ==========================================
# 修改后的交互与 API 逻辑
# ==========================================

def get_user_input_method():
    print("\n" + "="*50)
    print("   1. ⌨️  文本输入")
    print("   2. 🎤 语音输入 (中文)")
    c = input("   选择输入方式: ").strip()
    if c == '2': return listen_command()
    return input("\n📝 请输入电路描述 (例如: 做一个四位计数器): ")

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

def query_deepseek(prompt, mode="circuit", extra_context=""):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    
    # 📌 模式 1: Logisim 专用 Prompt
    system_prompt_circuit = """
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
        {"type": "D Flip-Flop", "stage": 3, "inputs": ["D0", "CLK", "RST"], "output": "Q0"},
        {"type": "Pin", "stage": 4, "net": "Q0", "dir": "in"}
      ]
    }
    """

    # 📌 模式 2: Verilog 专用 Prompt
    system_prompt_verilog = """
    You are an FPGA Engineer.
    Task: Convert the user's description into a synthesizable Verilog module.
    Rules:
    1. Use IEEE 1364 standard (Verilog-2001).
    2. Output ONLY a JSON object containing the code string.
    JSON Output Structure:
    {
      "verilog_code": "module name (...); ... endmodule"
    }
    """

    # 📌 模式 3: C++ Testbench (新增 - 适配 Verilator FST)
    system_prompt_cpp = f"""
        You are a Verilator Verification Engineer.
        Task: Write a C++ testbench (`main.cpp`) for a Verilog module named "{extra_context}".
        
        CONTEXT:
        The Verilog code is provided below. You MUST analyze it to determine the input ports.
        
        CRITICAL RULES:
        1. **NO HALLUCINATIONS**: Do NOT access `top->clk`, `top->rst`, or `top->clock` unless they are explicitly defined as `input` in the provided Verilog code.
        2. **Combinational Logic**: If no clock input exists, do NOT generate a clock toggle loop. Just change data inputs (A, B, etc.) and call `top->eval()` repeatedly.
        3. **Sequential Logic**: If a clock input IS present, drive it properly (0->1->0).
        
        Structure:
        - Include "V{extra_context}.h" and "verilated_fst_c.h".
        - Setup FST tracing ("wave.fst").
        - Loop for 20-50 steps changing inputs.
        - Output ONLY JSON: {{"cpp_code": "..."}}
        """

    # 根据模式选择提示词
    if mode == "circuit":
        sys_p = system_prompt_circuit
        user_p = f"Design: {prompt}"
    elif mode == "verilog":
        sys_p = system_prompt_verilog
        user_p = f"Design: {prompt}"
    elif mode == "cpp_tb":
        sys_p = system_prompt_cpp
        user_p = f"The Verilog code is:\n{prompt}"
    else:
        sys_p = system_prompt_circuit
        user_p = prompt

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": sys_p},
            {"role": "user", "content": user_p}
        ],
        "stream": False,
        "response_format": {"type": "json_object"}
    }
    
    try:
        # print(f"🤖 请求 AI ({mode})...")
        r = requests.post(url, headers=headers, json=data)
        return r.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {e}")
        return None

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   🔀 双模生成器 (Logisim v24.0 Core) + 自动仿真")
    print("="*50)
    print("请选择要生成的目标:")
    print("1. 📐 Logisim 电路图 (.circ)")
    print("2. 💻 Verilog 代码 + 🌊 自动仿真 (.v + .fst)")
    
    mode_input = input("   你的选择 (1/2): ").strip()
    
    # 确定模式
    target_mode = "circuit"
    if mode_input == '2':
        target_mode = "verilog"
    
    # 获取用户描述
    cmd = get_user_input_method()
    
    if cmd:
        # 调用 API
        res = query_deepseek(cmd, mode=target_mode)
        
        if res:
            # 根据模式分发处理
            if target_mode == "circuit":
                generate_circuit_file(res)
            else:
                save_verilog_and_sim(res)