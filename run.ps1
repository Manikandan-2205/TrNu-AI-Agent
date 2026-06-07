# run.ps1
# Script to install dependencies and run both the Frontend and Backend servers simultaneously

Write-Host "=======================================================" -ForegroundColor Green
Write-Host "  Starting TrNu Tech Solutions AI Service Desk Setup   " -ForegroundColor Green
Write-Host "=======================================================" -ForegroundColor Green

# -------------------------------------------------------------
# 1. SETUP AND RUN BACKEND
# -------------------------------------------------------------
Write-Host "`n[1/4] Checking Backend Dependencies..." -ForegroundColor Cyan
Set-Location -Path "backend"

# Ensure uv is installed
if (-Not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Error: 'uv' package manager is not installed. Please run 'pip install uv'." -ForegroundColor Red
    exit 1
}

# Create venv if it doesn't exist
if (-Not (Test-Path ".venv")) {
    Write-Host "Creating python virtual environment using uv..." -ForegroundColor Yellow
    uv venv
}

Write-Host "Installing backend packages from requirements.txt..." -ForegroundColor Yellow
uv pip install -r requirements.txt

# Start Backend in a new terminal window
Write-Host "`n[2/4] Starting FastAPI Backend Server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '$PWD'; Write-Host 'Starting FastAPI Backend...'; uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload`""

Set-Location -Path ".."

# -------------------------------------------------------------
# 2. SETUP AND RUN FRONTEND
# -------------------------------------------------------------
Write-Host "`n[3/4] Checking Frontend Dependencies..." -ForegroundColor Cyan
Set-Location -Path "frontend"

Write-Host "Installing Node.js packages..." -ForegroundColor Yellow
npm install

# Start Frontend in a new terminal window
Write-Host "`n[4/4] Starting Next.js Frontend Server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '$PWD'; Write-Host 'Starting Next.js Frontend...'; npm run dev`""

Set-Location -Path ".."

# -------------------------------------------------------------
# FINISHED
# -------------------------------------------------------------
Write-Host "`n=======================================================" -ForegroundColor Green
Write-Host "  All services have been started in separate windows!  " -ForegroundColor Green
Write-Host "=======================================================" -ForegroundColor Green
Write-Host "Backend API Docs:  http://localhost:8000/api/docs" -ForegroundColor Yellow
Write-Host "Frontend UI:       http://localhost:3000" -ForegroundColor Yellow
Write-Host "`nYou can close this terminal window. Close the new windows to stop the servers."
