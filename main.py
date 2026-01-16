"""
ODD Demo 主程序入口
命令行界面实现
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
load_dotenv()

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

# Windows 控制台编码修复
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from odd.contract_generator import ContractGenerator
from odd.code_generator import CodeGenerator
from odd.contract_verifier import ContractVerifier
from odd.seal_manager import SealManager

console = Console()


def run_odd_demo(requirement: str, save_code: bool = True) -> dict:
    """执行完整 ODD 流程"""
    results = {"requirement": requirement, "timestamp": datetime.now().isoformat()}
    
    # Step 1: 契约生成
    console.print(Panel("[bold cyan]Step 1: 契约生成[/bold cyan]"))
    contract_gen = ContractGenerator()
    contract = contract_gen.generate_contract(requirement)
    
    if contract.get('error'):
        console.print(f"[red]错误: {contract.get('message')}[/red]")
        return {"error": True, "message": contract.get('message')}
    
    console.print(f"[green]✓[/green] 匹配到产出物类型: [bold]{contract['artifact_type']}[/bold]")
    console.print(f"[green]✓[/green] 契约ID: {contract['contract_id'][:8]}...")
    results["contract"] = contract
    
    # Step 2: 代码生成
    console.print(Panel("[bold cyan]Step 2: 代码生成 (GPT-4)[/bold cyan]"))
    try:
        code_gen = CodeGenerator()
        code_result = code_gen.generate_code(contract)
        
        if code_result.get('error'):
            console.print(f"[red]错误: {code_result.get('message')}[/red]")
            return {"error": True, "message": code_result.get('message')}
        
        code = code_result['code']
        console.print(f"[green]✓[/green] 代码生成完成 (tokens: {code_result.get('tokens_used', 'N/A')})")
        results["code"] = code
    except ValueError as e:
        console.print(f"[yellow]跳过代码生成: {e}[/yellow]")
        code = "# 代码生成跳过 (未配置 API Key)"
        results["code"] = code
    
    # Step 3: 契约验证
    console.print(Panel("[bold cyan]Step 3: 契约验证[/bold cyan]"))
    verifier = ContractVerifier()
    verification = verifier.verify(code, contract['contract'].get('verification_hints', {}))
    
    table = Table(title="验证结果")
    table.add_column("规则", style="cyan")
    table.add_column("状态", style="green")
    table.add_column("详情")
    
    for check in verification['checks']:
        status = "[green]✓ PASS[/green]" if check['passed'] else "[red]✗ FAIL[/red]"
        table.add_row(check['rule'], status, str(check.get('found', '-')))
    
    console.print(table)
    overall = "[green]通过[/green]" if verification['passed'] else "[red]未通过[/red]"
    console.print(f"整体验证: {overall}")
    results["verification"] = verification
    
    # Step 4: 封存
    console.print(Panel("[bold cyan]Step 4: 封存[/bold cyan]"))
    sealer = SealManager()
    seal_result = sealer.seal(requirement, contract, code, verification)
    console.print(f"[green]✓[/green] 封存完成: {seal_result['file_path']}")
    console.print(f"[green]✓[/green] 完整性哈希: {seal_result['integrity'][:16]}...")
    results["seal"] = seal_result
    
    # 保存生成的代码
    if save_code:
        output_dir = Path(__file__).parent / "output"
        code_file = output_dir / f"generated_{contract['artifact_type']}.py"
        with open(code_file, 'w', encoding='utf-8') as f:
            f.write(code)
        console.print(f"[green]✓[/green] 代码已保存: {code_file}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description="ODD Demo - Output-Driven Development 概念验证")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # generate 命令
    gen_parser = subparsers.add_parser("generate", help="执行完整 ODD 流程")
    gen_parser.add_argument("requirement", type=str, help="自然语言需求")
    gen_parser.add_argument("--no-save", action="store_true", help="不保存生成的代码")
    
    # contract 命令 (仅生成契约)
    contract_parser = subparsers.add_parser("contract", help="仅生成契约")
    contract_parser.add_argument("requirement", type=str, help="自然语言需求")
    
    args = parser.parse_args()
    
    if args.command == "generate":
        console.print(Panel(f"[bold]ODD Demo[/bold]\n需求: {args.requirement}", title="Output-Driven Development"))
        run_odd_demo(args.requirement, save_code=not args.no_save)
    elif args.command == "contract":
        gen = ContractGenerator()
        contract = gen.generate_contract(args.requirement)
        console.print_json(json.dumps(contract, ensure_ascii=False))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
