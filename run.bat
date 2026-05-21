@echo off
REM File Organizer - Windows Launcher
REM This batch file sets up and runs the File Organizer on Windows

echo.
echo ========================================
echo   FILE ORGANIZER - Windows Launcher
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo Checking dependencies...
pip list | find "schedule" >nul
if errorlevel 1 (
    echo Installing schedule library...
    pip install schedule
)

REM Create logs directory if it doesn't exist
if not exist "logs" (
    mkdir logs
    echo Created logs directory
)

REM Run setup verification
echo.
echo Running setup verification...
python setup.py

REM Run main application
if errorlevel 1 (
    echo.
    echo Setup verification failed. Please fix the issues above.
    pause
    exit /b 1
)

echo.
echo Starting File Organizer...
echo.
python main.py

pause
