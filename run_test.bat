@echo off
chcp 65001 >nul
echo ========================================
echo AI Daily Report - 飞书测试
echo ========================================
echo.

REM 尝试多个Python路径
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo 找到Python,正在测试...
    python quick_test.py
    goto end
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    echo 找到Python3,正在测试...
    python3 quick_test.py
    goto end
)

REM 尝试Windows Store Python
if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    echo 使用Windows应用商店Python...
    "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" quick_test.py
    goto end
)

echo ❌ 未找到Python!
echo.
echo 请先安装Python:
echo 1. 访问 https://www.python.org/downloads/
echo 2. 下载并安装Python 3.7或更高版本
echo 3. 安装时勾选 "Add Python to PATH"
echo 4. 重新运行此脚本
echo.

:end
pause
