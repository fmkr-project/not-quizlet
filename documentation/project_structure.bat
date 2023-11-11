@echo off
SET "scriptPath=%~dp0doc_scripts\project_structure.ps1"
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& '%scriptPath%'"
pause