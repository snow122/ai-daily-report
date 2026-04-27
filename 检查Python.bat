@echo off
chcp 65001 >nul
echo ========================================
echo Python环境检查和安装指南
echo ========================================
echo.

REM 检查Python是否安装
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python已安装
    python --version
    goto install_deps
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python3已安装
    python3 --version
    goto install_deps_python3
)

REM 检查Windows应用商店Python
if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    echo ⚠ 检测到Windows应用商店Python(可能不完整)
    echo.
    echo 建议安装完整版Python:
    echo 1. 访问 https://www.python.org/downloads/
    echo 2. 下载Python 3.11或更高版本
    echo 3. 运行安装程序
    echo 4. **重要**: 勾选 "Add Python to PATH"
    echo 5. 点击 "Install Now"
    echo.
    pause
    exit
)

echo ❌ 未检测到Python!
echo.
echo ╔════════════════════════════════════════╗
echo ║  需要安装Python才能运行此程序          ║
echo ╚════════════════════════════════════════╝
echo.
echo 请按以下步骤安装Python:
echo.
echo 步骤1: 打开浏览器,访问:
echo   https://www.python.org/downloads/
echo.
echo 步骤2: 下载最新的Python 3.x版本(推荐3.11或3.12)
echo.
echo 步骤3: 运行下载的安装程序
echo.
echo 步骤4: 【非常重要】在安装界面底部勾选:
echo   ☑ Add Python to PATH
echo.
echo 步骤5: 点击 "Install Now" 开始安装
echo.
echo 步骤6: 安装完成后,关闭这个窗口,重新打开CMD
echo.
echo 步骤7: 再次双击运行 "一键安装依赖.bat"
echo.
echo ----------------------------------------
echo 或者,你可以直接点击下方链接下载Python:
echo https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
echo ----------------------------------------
echo.

choice /C YN /M "是否现在打开Python下载页面"
if errorlevel 2 goto end
if errorlevel 1 start https://www.python.org/downloads/

:end
pause
exit

:install_deps
echo.
echo 正在安装依赖包...
echo.
cd /d "d:\桌面\项目\ai-daily-report"
pip install -r requirements.txt
goto test

:install_deps_python3
echo.
echo 正在安装依赖包...
echo.
cd /d "d:\桌面\项目\ai-daily-report"
python3 -m pip install -r requirements.txt
goto test

:test
echo.
echo ========================================
echo 依赖安装完成!
echo ========================================
echo.
echo 现在测试飞书推送...
python quick_test.py
echo.
pause
