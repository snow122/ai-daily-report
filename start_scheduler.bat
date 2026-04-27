@echo off
chcp 65001 >nul
echo ========================================
echo AI Daily Report - 启动定时任务
echo 每天下午4点(16:00)自动推送
echo ========================================
echo.

REM 尝试多个Python路径
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo 启动定时任务...
    echo ⚠️ 重要: 不要关闭这个窗口!
    echo.
    python main.py
    goto end
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    echo 启动定时任务...
    echo ⚠️ 重要: 不要关闭这个窗口!
    echo.
    python3 main.py
    goto end
)

if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    echo 启动定时任务...
    echo ⚠️ 重要: 不要关闭这个窗口!
    echo.
    "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" main.py
    goto end
)

echo ❌ 未找到Python!
echo 请先安装Python后再运行。

:end
pause
