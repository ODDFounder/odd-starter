"""
代码生成器 (Code Generator)
调用 OpenAI GPT-4 API 根据契约生成代码
"""

import os
import json
from typing import Optional
from openai import OpenAI


class CodeGenerator:
    """代码生成器：根据契约调用 LLM API 生成代码"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("未设置 OPENAI_API_KEY")
        
        # 支持 NVIDIA API 或 OpenAI API
        base_url = os.getenv("OPENAI_BASE_URL", None)
        if base_url:
            self.client = OpenAI(api_key=self.api_key, base_url=base_url)
        else:
            self.client = OpenAI(api_key=self.api_key)
        
        self.model = os.getenv("OPENAI_MODEL", "gpt-4")
    
    def _build_system_prompt(self) -> str:
        return """你是一个严格的代码生成器，遵循 ODD (Output-Driven Development) 范式。

核心原则：
1. 你必须完全遵循提供的契约条款，不得遗漏任何隐式需求
2. 生成的代码必须包含所有必要的导入语句
3. 必须包含适当的错误处理
4. 代码必须可直接运行

输出格式：
- 只输出纯 Python 代码
- 不要添加 ```python 标记
- 不要添加任何解释性文字"""

    def _build_user_prompt(self, contract: dict) -> str:
        implicit_reqs = contract.get('contract', {}).get('implicit_requirements', [])
        implicit_text = "\n".join([f"  - [{r['id']}] {r['name']}: {r['description']}" for r in implicit_reqs])
        
        common_knowledge = contract.get('contract', {}).get('common_knowledge', {})
        inputs = contract.get('contract', {}).get('inputs', [])
        outputs = contract.get('contract', {}).get('outputs', [])
        hints = contract.get('contract', {}).get('generation_hints', [])
        
        return f"""请生成一个完整的 Python Flask API 文件，实现以下契约。

## 原始需求
{contract.get('requirement_original', '')}

## 产出物类型
{contract.get('artifact_type', '')} - {contract.get('artifact_name', '')}

## 隐式需求（必须全部满足）
{implicit_text}

## 常识参数
{json.dumps(common_knowledge, indent=2, ensure_ascii=False)}

## 输入参数
{json.dumps(inputs, indent=2, ensure_ascii=False)}

## 输出参数
{json.dumps(outputs, indent=2, ensure_ascii=False)}

## 生成提示
{chr(10).join(['- ' + h for h in hints])}

请生成完整的 Flask API 代码，包含：
1. 所有必要的 import 语句
2. Flask app 初始化
3. API 路由实现
4. 输入验证
5. 错误处理
6. if __name__ == '__main__' 启动代码"""

    def generate_code(self, contract: dict) -> dict:
        """根据契约生成代码"""
        if contract.get('error'):
            return {"error": True, "message": contract.get('message'), "code": None}
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._build_system_prompt()},
                    {"role": "user", "content": self._build_user_prompt(contract)}
                ],
                temperature=0.2,
                max_tokens=4000
            )
            code = response.choices[0].message.content.strip()
            if code.startswith("```"):
                code = code.split("\n", 1)[1].rsplit("```", 1)[0]
            return {"error": False, "code": code, "model": self.model, "tokens_used": response.usage.total_tokens}
        except Exception as e:
            return {"error": True, "message": f"API 调用失败: {str(e)}", "code": None}


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    from contract_generator import ContractGenerator
    
    cg = ContractGenerator()
    contract = cg.generate_contract("创建用户登录API")
    
    gen = CodeGenerator()
    result = gen.generate_code(contract)
    print(result.get('code', result.get('message')))
