@echo off
chcp 65001 >nul
echo ========================================
echo AI Daily Report - 一键安装依赖
echo ========================================
echo.

REM 切换到项目目录
cd /d "d:\桌面\项目\ai-daily-report"
echo 当前目录: %CD%
echo.

REM 尝试多个Python路径
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo 正在安装依赖...
    pip install -r requirements.txt
    goto test
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    echo 正在安装依赖...
    python3 -m pip install -r requirements.txt
    goto test
)

if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    echo 使用Windows应用商店Python...
    "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" -m pip install -r requirements.txt
    goto test
)

echo ❌ 未找到Python!
echo.
echo 请先安装Python:
echo 1. 访问 https://www.python.org/downloads/
echo 2. 下载并安装Python 3.7或更高版本
echo 3. 安装时勾选 "Add Python to PATH"
echo.
pause
exit

:test
echo.
echo ========================================
echo 安装完成! 现在测试飞书推送...
echo ========================================
echo.

if exist "quick_test.py" (
    python quick_test.py
) else (
    python main.py --now
)

echo.
echo ========================================
echo 如果测试成功,按任意键启动定时任务
echo 如果测试失败,请检查错误信息
echo ========================================
pause

REM 启动定时任务
echo.
echo 正在启动定时任务...
echo ⚠️ 重要: 不要关闭这个窗口!
echo.
python main.py

pause
