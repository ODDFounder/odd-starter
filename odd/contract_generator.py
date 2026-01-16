"""
契约生成器 (Contract Generator)
将自然语言需求匹配到标准库，生成结构化契约
"""

import uuid
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional


class ContractGenerator:
    """契约生成器：根据用户需求和标准库生成结构化契约"""
    
    def __init__(self, standards_path: str = None):
        if standards_path is None:
            standards_path = Path(__file__).parent.parent / "artifacts" / "standards" / "standard_library.yaml"
        self.standards_path = Path(standards_path)
        self.standards = self._load_standards()
    
    def _load_standards(self) -> dict:
        """加载产出物标准库"""
        if not self.standards_path.exists():
            raise FileNotFoundError(f"标准库文件不存在: {self.standards_path}")
        with open(self.standards_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def match_artifact_type(self, requirement: str) -> Optional[str]:
        """通过关键词匹配需求到产出物类型"""
        requirement_lower = requirement.lower()
        artifacts = self.standards.get('artifacts', {})
        
        best_match = None
        best_score = 0
        
        for artifact_id, artifact_config in artifacts.items():
            keywords = artifact_config.get('keywords', [])
            score = sum(1 for kw in keywords if kw.lower() in requirement_lower)
            if score > best_score:
                best_score = score
                best_match = artifact_id
        
        return best_match if best_score > 0 else None
    
    def generate_contract(self, requirement: str) -> dict:
        """生成完整契约"""
        artifact_type = self.match_artifact_type(requirement)
        
        if artifact_type is None:
            return {
                "error": True,
                "message": f"无法匹配需求到已知产出物类型: {requirement}",
                "requirement_original": requirement
            }
        
        artifact_config = self.standards['artifacts'][artifact_type]
        
        contract = {
            "contract_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "requirement_original": requirement,
            "artifact_type": artifact_type,
            "artifact_name": artifact_config.get('name', artifact_type),
            "contract": {
                "implicit_requirements": artifact_config.get('implicit_requirements', []),
                "common_knowledge": artifact_config.get('common_knowledge', {}),
                "inputs": artifact_config.get('contract_template', {}).get('inputs', []),
                "outputs": artifact_config.get('contract_template', {}).get('outputs', []),
                "generation_hints": artifact_config.get('generation_hints', []),
                "verification_hints": artifact_config.get('verification_hints', {})
            }
        }
        
        return contract


if __name__ == "__main__":
    # 测试示例
    generator = ContractGenerator()
    result = generator.generate_contract("创建一个用户登录API，需要手机号和密码")
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
