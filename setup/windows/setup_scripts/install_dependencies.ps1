# PowerShell script for setting up project dependencies

Write-Host "Starting project setup..."

# Install Python dependencies
if (Test-Path "..\..\backend") {
    Write-Host "Installing Python dependencies..." -ForegroundColor Blue
    pip install -r "..\..\backend\requirements.txt"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install Python dependencies." -ForegroundColor Red
        Pause
        exit 1
    }
    Write-Host "Python dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "Backend directory not found." -ForegroundColor Red
    Pause
    exit 1
}

# Install Node dependencies
if (Test-Path "..\..\frontend") {
    Write-Host "Installing Node.js dependencies..." -ForegroundColor Magenta
    Push-Location "..\..\frontend"
    npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install Node.js dependencies." -ForegroundColor Red
        Pause
        exit 1
    }
    Write-Host "Node.js dependencies installed successfully." -ForegroundColor Green
    Pop-Location
} else {
    Write-Host "Frontend directory not found." -ForegroundColor Red
    Pause
    exit 1
}

Write-Host "Project setup completed successfully." -ForegroundColor Green
Pause
