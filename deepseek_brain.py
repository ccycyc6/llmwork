import requests
import json

class CircuitBrain:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "sk-045bccc976d94c948a50bed9b70281fa" # 请核对具体的DeepSeek API Endpoint

    def verify_circuit(self, components, wires, objective):
        """
        components: 组件列表
        wires: 连线列表
        objective: 当前关卡目标 (例如: "构建一个半加器")
        """
        
        # 1. 将电路转化为 DeepSeek 能读懂的 Netlist (网表)
        netlist_desc = "Current Circuit Configuration:\n"
        for wire in wires:
            netlist_desc += f"- Output of [{wire.start_gate.id}] is connected to Input of [{wire.end_gate.id}]\n"
        
        for comp in components:
            netlist_desc += f"- Component: {comp.id} (Type: {comp.type})\n"

        # 2. 构建 Prompt
        system_prompt = """
        You are an expert Digital Logic Professor. 
        Analyze the user's circuit netlist. 
        Verify if it matches the 'Objective'. 
        If it's correct, say 'PASS'. 
        If it's wrong, explain why briefly and give a hint.
        """
        
        user_prompt = f"Objective: {objective}\n\n{netlist_desc}"

        # 3. 发送请求
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek-chat", # 或 deepseek-coder
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error connecting to Logic Core: {e}"