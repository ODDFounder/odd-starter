"""
契约验证器 (Contract Verifier)
对生成的代码进行静态模式检查
"""

import re
from typing import List


class ContractVerifier:
    """契约验证器：检查生成代码是否符合契约要求"""
    
    def verify(self, code: str, verification_hints: dict) -> dict:
        """执行验证检查"""
        checks = []
        all_passed = True
        critical_failed = False
        
        # must_contain_any 检查
        for rule in verification_hints.get('must_contain_any', []):
            patterns = rule.get('patterns', [])
            reason = rule.get('reason', '')
            severity = rule.get('severity', 'medium')
            found = None
            for pattern in patterns:
                if pattern.lower() in code.lower():
                    found = pattern
                    break
            passed = found is not None
            if not passed and severity == 'critical':
                critical_failed = True
            if not passed:
                all_passed = False
            checks.append({"type": "must_contain_any", "rule": reason, "severity": severity, "passed": passed, "found": found})
        
        # must_not_contain 检查
        for rule in verification_hints.get('must_not_contain', []):
            patterns = rule.get('patterns', [])
            reason = rule.get('reason', '')
            severity = rule.get('severity', 'medium')
            found = None
            for pattern in patterns:
                if pattern in code:
                    found = pattern
                    break
            passed = found is None
            if not passed and severity == 'critical':
                critical_failed = True
            if not passed:
                all_passed = False
            checks.append({"type": "must_not_contain", "rule": reason, "severity": severity, "passed": passed, "found": found})
        
        # should_contain 检查 (不影响整体通过)
        for rule in verification_hints.get('should_contain', []):
            patterns = rule.get('patterns', [])
            reason = rule.get('reason', '')
            found = None
            for pattern in patterns:
                if pattern in code:
                    found = pattern
                    break
            checks.append({"type": "should_contain", "rule": reason, "severity": "low", "passed": found is not None, "found": found})
        
        return {"passed": all_passed and not critical_failed, "critical_failed": critical_failed, "checks": checks}


if __name__ == "__main__":
    test_code = '''
import bcrypt
from flask import Flask
def login(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return {"token": "jwt_token"}
'''
    hints = {
        "must_contain_any": [{"patterns": ["bcrypt", "hashlib"], "reason": "密码哈希", "severity": "critical"}],
        "must_not_contain": [{"patterns": ["password ="], "reason": "明文密码", "severity": "critical"}]
    }
    verifier = ContractVerifier()
    result = verifier.verify(test_code, hints)
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
