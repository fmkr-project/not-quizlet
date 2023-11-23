@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo Starting project setup...

REM Install Python dependencies
if exist "..\..\backend" (
    echo Installing Python dependencies...
    pip install -r ..\..\backend\requirements.txt
    if !errorlevel! neq 0 (
        echo Failed to install Python dependencies.
        pause
        exit /b 1
    )
    echo Python dependencies installed successfully.
) else (
    echo Backend directory not found.
    pause
    exit /b 1
)

REM Install Node dependencies
if exist "..\..\frontend" (
    echo Installing Node.js dependencies...
    cd ..\..\frontend
    npm install
    if !errorlevel! neq 0 (
        echo Failed to install Node.js dependencies.
        pause
        exit /b 1
    )
    cd ..\..\setup\windows
    echo Node.js dependencies installed successfully.
) else (
    echo Frontend directory not found.
    pause
    exit /b 1
)

echo Project setup completed successfully.
pause