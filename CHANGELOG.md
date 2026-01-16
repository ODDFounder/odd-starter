# Changelog

All notable changes to ODD Starter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-01-16

### Added
- Initial release of ODD Starter
- Contract Generator - 自动匹配需求到契约模板
- Code Generator - 支持 OpenAI/NVIDIA API
- Contract Verifier - 静态模式检查
- Seal Manager - SHA-256 哈希链封存
- CLI Interface - `generate` 和 `contract` 命令
- Artifact Standard Library - `auth_login` 和 `crud_api` 模板
- Complete documentation (CN + EN)
  - Developer Guide
  - Manager Guide
  - Executive Guide

### Demo Results
- Input: "创建一个用户登录API"
- Output: 87 lines of Flask API code
- Generation time: 3 seconds
- Verification: 5/6 checks passed
- Seal ID: `961afd7e-fe9d-4961-9ddc-ebef7abfd806`

[Unreleased]: https://github.com/oddfounder/odd-starter/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/oddfounder/odd-starter/releases/tag/v0.1.0
