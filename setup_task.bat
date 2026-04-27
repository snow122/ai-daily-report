@echo off
chcp 65001 >nul
echo ========================================
echo AI Daily Report - 设置Windows定时任务
echo 每天下午4点自动执行(无需保持窗口开启)
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 需要管理员权限!
    echo.
    echo 请右键点击此文件,选择"以管理员身份运行"
    echo.
    pause
    exit /b 1
)

echo 正在创建Windows定时任务...
echo.

REM 删除已存在的任务(如果有)
schtasks /delete /tn "AI_Daily_Report" /f >nul 2>&1

REM 获取Python路径
where python >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_PATH=python
    goto create_task
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_PATH=python3
    goto create_task
)

if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    set PYTHON_PATH="%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe"
    goto create_task
)

echo ❌ 未找到Python路径!
pause
exit /b 1

:create_task
echo Python路径: %PYTHON_PATH%
echo 工作目录: d:\桌面\项目\ai-daily-report
echo.

REM 创建定时任务
schtasks /create ^
    /tn "AI_Daily_Report" ^
    /tr "%PYTHON_PATH% main.py --now" ^
    /sc daily ^
    /st 16:00 ^
    /ru %USERNAME% ^
    /rl HIGHEST ^
    /sd %date:~0,4%/%date:~5,2%/%date:~8,2% ^
    /f

if %errorlevel% equ 0 (
    echo.
    echo ✅ 定时任务创建成功!
    echo.
    echo 任务名称: AI_Daily_Report
    echo 执行时间: 每天下午 16:00
    echo 执行命令: python main.py --now
    echo.
    echo 你可以在以下位置查看和管理任务:
    echo   控制面板 → 管理工具 → 任务计划程序
    echo   或运行: taskschd.msc
    echo.
    echo 测试任务(立即执行一次):
    echo   schtasks /run /tn "AI_Daily_Report"
    echo.
    echo 查看任务状态:
    echo   schtasks /query /tn "AI_Daily_Report"
    echo.
    echo 删除任务:
    echo   schtasks /delete /tn "AI_Daily_Report" /f
    echo.
) else (
    echo.
    echo ❌ 任务创建失败!
    echo.
)

pause
