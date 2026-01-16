# ODD Frequently Asked Questions

## General

### What is ODD?

**ODD (Output-Driven Development)** is a methodology for AI-native software engineering. It prioritizes **Artifacts** and **Decision Responsibility** over Code.

### How is ODD different from GitHub Copilot?

| Copilot | ODD |
|---------|-----|
| AI assistant that helps you write code | Framework that defines contracts for AI to generate code |
| You still review all code | System verifies code automatically |
| Responsibility is vague | Responsibility is clear via contracts |
| Focus on "how to write" | Focus on "what to produce" |

### Is ODD a tool or a methodology?

ODD is a **methodology** with a reference implementation. You can practice ODD with any tools (Copilot, Cursor, Claude, etc.). This repo is a reference implementation.

---

## Usage

### What LLMs are supported?

Any OpenAI-compatible API:
- OpenAI (GPT-4, GPT-4o)
- NVIDIA (Llama, Mistral)
- Anthropic (via adapter)
- Local models (Ollama, LM Studio)

### Do I need to know how to code?

No. ODD separates **definition** from **execution**:
- **Definition** (contracts) requires domain knowledge, not coding
- **Execution** (code generation) is done by AI

Domain experts can participate directly without programming skills.

### Can I use ODD for [specific use case]?

ODD is designed for:
- ✅ Enterprise applications
- ✅ Finance/Healthcare (compliance requirements)
- ✅ Large teams (standardization needs)
- ✅ High-risk systems (auditability needs)

ODD is NOT designed for:
- ❌ Creative exploration
- ❌ Pure art projects
- ❌ Zero-cost prototyping

---

## Technical

### What is a "contract"?

A contract is a precise agreement defining artifacts:
- **Inputs**: What the artifact receives
- **Outputs**: What the artifact produces
- **Implicit requirements**: Expert knowledge encoded as rules
- **Verification hints**: How to validate the result

### What is "sealing"?

Sealing creates an immutable audit trail:
- Calculates SHA-256 hash of each artifact
- Establishes a complete hash chain
- Enables traceability from final code back to requirements

### What if verification fails?

Two scenarios:
1. **Critical failure** (e.g., missing password hashing) → Block deployment, require human decision
2. **Warning** (e.g., missing exception handling) → Log warning, allow override

This is **Human-in-the-Loop Governance**: AI generates, system screens, humans decide.

---

## Contributing

### How can I contribute?

1. **Add contract templates** to `artifacts/standards/`
2. **Improve verification rules** for existing templates
3. **Share your use cases** in Discussions
4. **Report bugs** via Issues

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

### Can I use ODD commercially?

Yes. ODD is licensed under [MIT License](LICENSE), which permits commercial use.

### Do I need to credit ODD?

No, but it's appreciated if you do.

---

## Contact

**Author**: Yi Fu (ODDFounder)
**Email**: fuyi.it@live.cn
**WeChat**: Fuyi-ODDFounder
**GitHub**: [@oddfounder](https://github.com/oddfounder)

---

<div align="center">

### ⭐ Found this helpful? [Star us on GitHub](https://github.com/oddfounder/odd-starter)

**ODD: Unleash AI Speed. Reduce Engineering Risk.**

</div>
