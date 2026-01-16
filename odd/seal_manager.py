"""
封存管理器 (Seal Manager)
将所有产物进行哈希封存
"""

import uuid
import json
import hashlib
from datetime import datetime
from pathlib import Path


class SealManager:
    """封存管理器：计算哈希并生成封存记录"""
    
    def __init__(self, output_dir: str = None):
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / "output"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def _compute_hash(self, content: str) -> str:
        """计算 SHA-256 哈希"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def seal(self, requirement: str, contract: dict, code: str, verification: dict) -> dict:
        """封存所有产物"""
        seal_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        contract_str = json.dumps(contract, ensure_ascii=False, sort_keys=True)
        verification_str = json.dumps(verification, ensure_ascii=False, sort_keys=True)
        
        seal_record = {
            "seal_id": seal_id,
            "timestamp": timestamp,
            "odd_version": "0.1.0",
            "hashes": {
                "requirement": self._compute_hash(requirement),
                "contract": self._compute_hash(contract_str),
                "code": self._compute_hash(code),
                "verification": self._compute_hash(verification_str)
            },
            "artifacts": {
                "requirement": requirement,
                "contract": contract,
                "code": code,
                "verification": verification
            },
            "integrity": None
        }
        
        # 计算整体完整性哈希
        integrity_content = f"{seal_record['hashes']['requirement']}:{seal_record['hashes']['contract']}:{seal_record['hashes']['code']}:{seal_record['hashes']['verification']}"
        seal_record["integrity"] = self._compute_hash(integrity_content)
        
        # 保存到文件
        seal_file = self.output_dir / f"seal_{seal_id[:8]}.json"
        with open(seal_file, 'w', encoding='utf-8') as f:
            json.dump(seal_record, f, indent=2, ensure_ascii=False)
        
        return {"seal_id": seal_id, "file_path": str(seal_file), "integrity": seal_record["integrity"]}


if __name__ == "__main__":
    sealer = SealManager()
    result = sealer.seal(
        requirement="测试需求",
        contract={"test": "contract"},
        code="print('hello')",
        verification={"passed": True}
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
