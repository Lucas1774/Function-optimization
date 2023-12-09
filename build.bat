@echo off
pyinstaller --onefile src\functionOptimizer.py
move dist\functionOptimizer.exe .
rmdir /s /q dist
rmdir /s /q build
del functionOptimizer.spec
