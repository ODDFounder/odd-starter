@echo off
chcp 65001 >nul
echo ========================================
echo   ODD Demo - Output-Driven Development
echo ========================================
echo.

REM 检查虚拟环境
if not exist "venv" (
    echo [1/3] 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境并安装依赖
echo [2/3] 安装依赖...
call venv\Scripts\activate.bat
pip install -r requirements.txt -q

REM 检查 .env 文件
if not exist ".env" (
    echo.
    echo [警告] 未找到 .env 文件
    echo 请复制 .env.example 为 .env 并填入 OPENAI_API_KEY
    echo.
    copy .env.example .env
    echo 已创建 .env 文件，请编辑后重新运行
    pause
    exit /b 1
)

REM 运行 Demo
echo [3/3] 运行 ODD Demo...
echo.
python main.py generate "创建一个用户登录API，需要用户名和密码"

echo.
echo ========================================
echo   Demo 完成！查看 output 目录获取结果
echo ========================================
pause
