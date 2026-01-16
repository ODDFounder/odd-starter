# ODD Demo 开发任务清单

## 项目目标
创建一个命令行工具，演示 ODD 流程：需求 -> 契约 -> 代码 -> 验证 -> 封存

---

## 任务列表

### 阶段一：项目初始化
- [x] 创建目录结构 (`odd/`, `artifacts/standards/`, `output/`)
- [ ] 创建 `requirements.txt`
- [ ] 创建 `.env.example`
- [ ] 创建 `main.py` 入口

### 阶段二：产出物标准库
- [x] 设计标准库 YAML 格式规范
- [x] 创建 `standard_library.yaml` (含 auth_login + crud_api)

### 阶段三：核心模块实现
- [ ] `odd/__init__.py` - 包初始化
- [ ] `odd/utils.py` - 工具函数
- [ ] `odd/contract_generator.py` - 契约生成器
      - 加载 standard_library.yaml
      - 关键词匹配产出物类型
      - 提取隐式需求和常识参数
      - 输出结构化契约字典
- [ ] `odd/code_generator.py` - 代码生成器 (GPT-4)
      - 函数: generate_code(contract_dict, api_key)
      - System Prompt: 严格遵循契约的代码生成器
      - User Prompt: 生成完整 Flask API 代码
      - 异常处理: API调用失败、响应解析
- [ ] `odd/contract_verifier.py` - 契约验证器
      - 静态模式检查
      - 检查密码哈希关键字 (bcrypt/pbkdf2/hash)
      - 返回验证结果布尔值
- [ ] `odd/seal_manager.py` - 封存模块
      - 计算各产物 SHA-256 哈希
      - 打包: 原始需求、契约、代码、验证结果
      - 输出: seal.json (含时间戳)

### 阶段四：CLI 实现
- [ ] `odd/cli.py` - 命令行界面 (click)
- [ ] 实现完整 ODD 流程命令

### 阶段五：测试与演示
- [ ] 端到端流程测试

---

## 技术栈
- Python 3.13
- click (CLI)
- openai (GPT-4 API)
- pyyaml (标准库解析)
- rich (终端美化)
- pydantic (数据校验)

---

## 模块详细设计

### contract_generator.py
```
输入: "创建一个用户登录API，需要手机号和密码"
处理:
  1. 加载 standard_library.yaml
  2. 关键词匹配 -> auth_login
  3. 提取隐式需求 + 常识参数
输出:
  {
    "contract_id": "uuid",
    "requirement_original": "原始需求",
    "artifact_type": "auth_login",
    "contract": {
      "implicit_requirements": [...],
      "common_knowledge": {...},
      "inputs": [...],
      "outputs": [...]
    }
  }
```

### code_generator.py
```
System Prompt:
  "你是一个严格的代码生成器，必须完全遵循提供的契约条款..."
User Prompt:
  "请生成一个完整的Python Flask文件，实现以下契约..."
异常处理:
  - API调用失败
  - 响应解析错误
  - 超时处理
```

### contract_verifier.py
```
输入: 生成的代码字符串
处理:
  1. 加载对应产出物的 verification_hints
  2. 执行 must_contain_any 检查
  3. 执行 must_not_contain 检查
输出:
  {
    "passed": bool,
    "checks": [
      {"rule": "密码哈希", "passed": true, "found": "bcrypt"},
      ...
    ]
  }
```

### seal_manager.py
```
输入: requirement, contract, code, verification_result
处理:
  1. 计算各项 SHA-256 哈希
  2. 生成时间戳
  3. 组装封存结构
输出: seal.json
  {
    "seal_id": "uuid",
    "timestamp": "ISO8601",
    "hashes": {
      "requirement": "sha256...",
      "contract": "sha256...",
      "code": "sha256...",
      "verification": "sha256..."
    },
    "artifacts": {...}
  }
```

---

## 当前进度
**状态**: 阶段四完成，全部模块已实现
**下一步**: 测试完整流程

## 已完成文件
- `odd/__init__.py`
- `odd/contract_generator.py`
- `odd/code_generator.py`
- `odd/contract_verifier.py`
- `odd/seal_manager.py`
- `main.py`
- `run_demo.bat`
- `requirements.txt`
- `.env.example`
