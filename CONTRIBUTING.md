# Contributing to ODD Starter

感谢你对 ODD 项目的关注！

## 如何贡献

### 报告问题

请在 [Issues](https://github.com/oddfounder/odd-starter/issues) 中报告 bug 或提出功能请求。

报告问题时，请包含：
- ODD 版本号
- Python 版本
- 操作系统
- 复现步骤
- 预期行为 vs 实际行为

### 提交代码

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 代码规范

- 使用 PEP 8 风格指南
- 添加必要的注释和文档字符串
- 确保所有测试通过
- 更新相关文档

### 提交契约模板

ODD 的核心价值在于**产出物标准库**。欢迎贡献新的契约模板：

```yaml
# artifacts/standards/your_artifact.yaml
your_artifact:
  name: "你的产出物名称"
  keywords: ["关键词1", "关键词2"]
  implicit_requirements:
    - {id: "IR001", name: "隐式需求", severity: "critical"}
  verification_hints:
    must_contain_any:
      - patterns: ["必要模式"]
        reason: "原因"
```

## 行为准则

- 尊重不同观点
- 建设性反馈
- 关注问题本身而非个人

## 许可证

贡献的代码将采用与项目相同的 [MIT License](LICENSE)。
