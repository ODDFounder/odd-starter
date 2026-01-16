---
marp: true
theme: gaia
class: lead
backgroundColor: #1a1a1a
color: #f0f0f0
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 30px;
  }
  h1 {
    color: #4da6ff;
    font-size: 60px;
  }
  h2 {
    color: #99ccff;
    font-size: 40px;
  }
  strong {
    color: #ffad33;
  }
  blockquote {
    background: #333;
    border-left: 10px solid #4da6ff;
    color: #fff;
    padding-top: 20px;
    padding-bottom: 20px;
  }
  ul {
    text-align: left;
  }
  table {
    font-size: 24px;
    margin-left: auto;
    margin-right: auto;
  }
  th {
    color: #4da6ff;
  }
---

# Output-Driven Development
## The Responsibility Framework for AI-Native Software Production

**Yi Fu (ODDFounder)**
January 2026

---

## Executive Summary
### What Has Changed?

*   **Scarcity Shift**: Code generation cost has collapsed to near zero.
*   **The Bottleneck**: Traditional methods (Agile/TDD) fail when AI generates 1,000 lines/sec. Human review is now a security vulnerability.
*   **The Solution**: ODD is a **structural response**.

> **Core Judgment**:
> When code generation is no longer scarce, **Responsibility**, **Auditability**, and **Decision Structure** become the new scarce resources.

---

## The Problem is Not "Efficiency"
### It Is "Responsibility Collapse"

We reject the narrative that "AI makes programming faster."

**The Defining Questions of Our Era:**
*   **Who** is responsible for a logical error?
*   **Who** can explain a stochastic decision?
*   **Who** is audited when code is ephemeral?

> **Efficiency is optional.**
> **Responsibility is unavoidable.**

---

## Hidden Assumptions Have Failed

We do not need a "better Agile." We need a new social contract.

| Implicit Assumption | Reality in AI Era | Consequence |
| :--- | :--- | :--- |
| **Human Authorship** | AI generates bulk code | Attribution Failure |
| **Human Readability** | Code is discarded daily | Cognitive Overload |
| **Process = Trust** | Dev is a stochastic matrix | Trust Collapse |

---

## What Is ODD?

**Output-Driven Development (ODD)** is a methodology that prioritizes **Artifacts** and **Decision Responsibility** over Code.

**What ODD Is NOT:**
❌ A code generation tool (like Copilot)
❌ An automation script
❌ A replacement for domain expertise

**What ODD IS:**
✅ A **Responsibility-First** perspective
✅ An **Artifact-Centric** structure
✅ A way to **exit execution without exiting responsibility**

---

## The Core Shift: Code → Output

**The Traditional View**
`Requirements → [Write Code] → [Review Code] → Value`
*Focus: "Is the code elegant?"*

**The ODD View**
`Intent → [Define Contract] → [AI Generates] → [Verify] → Value`
*Focus: "Does the output satisfy the contract?"*

> In the AI era, **"Why this result was permitted"** is infinitely more important than **"How the code was written."**

---

<!-- _class: lead -->
<style scoped>section { font-size: 20px; } h2 { font-size: 32px; } blockquote { padding: 10px 20px; }</style>

## The Utility Structure

ODD is designed to **increase utility**, not just enforce accountability.

> **Utility = Output Value / Input Cost**

**How does ODD affect this equation?**

1.  **Numerator: Output Value ↑**
    *   Contracts precisely define "what is valuable output"
    *   Reduce "looks correct but useless" waste code
    *   Artifacts map directly to business requirements

2.  **Denominator: Input Cost ↓**
    *   Humans focus on definition & acceptance
    *   Execution & verification delegated to AI and systems
    *   Cognitive load shifts from "full participation" to "key checkpoint participation"

> *This is a structural possibility, not a guarantee. Actual utility depends on implementation quality.*

---

<!-- _class: lead -->
<style scoped>section { font-size: 20px; } h2 { font-size: 32px; } blockquote { padding: 10px 20px; }</style>

## Scaling Potential

ODD's architecture is designed to exhibit the following **theoretical properties**:

1.  **Concurrency limited by compute, not headcount**
    *   Traditional: Add people → Add communication overhead
    *   ODD: Add compute → Diminishing marginal cost

2.  **Contracts as reusable assets**
    *   Code may need rewriting as models upgrade
    *   Contracts define "what is needed", independent of implementation

3.  **Domain experts can participate directly**
    *   Contract definition requires no programming skills
    *   Lower technical barrier, broader participation

4.  **Clear, traceable responsibility**
    *   Every artifact has a contract signer
    *   Complete audit trail

> *These are architectural design properties. Actual performance requires empirical validation.*

---

<!-- _class: lead -->
<style scoped>section { font-size: 20px; } h2 { font-size: 32px; } blockquote { padding: 10px 20px; }</style>

## The Structural Dividend
### Why would enterprises WANT to use ODD?

1.  **Infinite Concurrency**
    *   *Unlock*: Speed is no longer limited by human reading speed, but by compute.
    *   *Result*: **Linear Headcount → Exponential Compute**.

2.  **Asset Accumulation**
    *   *Unlock*: Code is a liability (maintenance); **Contracts are assets** (reusable, tradeable).
    *   *Result*: As models get better, your contracts gain value.

3.  **Cognitive Decoupling**
    *   *Unlock*: Domain experts can build software without mastering syntax.
    *   *Result*: **Domain Experts** become direct producers.

4.  **Organizational Empowerment**
    *   *Unlock*: Shift from "Human Wave" to "Elite Squad + AI Legion".
    *   *Result*: **One-Person Army** leveraging systemic power.

---

## The Human Role
### Exiting the Execution Loop

ODD does **not** remove humans. It **elevates** them.

1.  **Execution Loop** (Typing, Syntax) → **Delegate to AI**
2.  **Decision Loop** (Intent, Constraints) → **Retain for Humans**
3.  **Audit Loop** (Traceability) → **Enforce by System**

> Stop being a **Bricklayer**.
> Become a **Building Inspector**.

---

## ODD vs. "Runaway AI"

ODD explicitly opposes "Black Box" automation.

**The ODD Bottom Line:**
Any critical AI-generated artifact must be able to answer:

> **"Who, under what conditions, authorized my existence?"**

If a system cannot answer this, it is not an ODD system.
It is a **rogue system**.

---

## Why Now?
### The Window of Opportunity

1.  **Capability**: Models are finally reliable enough.
2.  **Vacuum**: No standard exists for AI governance.
3.  **Pre-Crisis**: The "Chernobyl of AI Software" hasn't happened yet.

> **We are building the fire escape before the fire.**
> We provide the structural option before trust collapses.

---

## Boundaries & Limitations

To be credible, we must be honest.

**ODD is NOT suitable for:**
*   **Creative Exploration** (Use Vibe Coding)
*   **Purely Subjective Domains** (Art/Aesthetics)
*   **Zero-Cost Prototyping**

> ODD is **not** designed to maximize innovation speed.
> It is designed to **prevent structural collapse** in scaled AI production.

---

# Conclusion

ODD is a beginning, not an end.

Whether ODD evolves or is replaced, the questions it raises will remain:

*   **Responsibility**
*   **Auditability**
*   **Artifact-Centricity**

> We invite you to join us in defining this new reality, rather than being defined by it.

---

## Get Involved

*   **Read the full whitepaper**: Deep dive into ODD theory
*   **View Zenodo preprint**: The formally registered document
*   **Join early discussions**: Explore AI-native software engineering with us

> **Zenodo Paper**: https://zenodo.org/records/18207648

---

# Thank You

**Output-Driven Development**
*Unleash AI Speed. Reduce Engineering Risk.*

Yi Fu . (ODDFounder)
Email: fuyi.it@live.cn
WeChat: Fuyi-ODDFounder
