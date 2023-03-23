@echo off
cd /d "%~dp0"

:Isolation
SET CONDA_SHLVL=
SET PYTHONNOUSERSITE=1
SET PYTHONPATH=

Reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v "LongPathsEnabled" /t REG_DWORD /d "1" /f 2>nul
IF EXIST _conda GOTO APP

micromamba create --no-shortcuts -r _conda -c conda-forge -n msp python=3.10 -y
micromamba run -r _conda -n msp python -s -m pip install -r requirements.txt

:APP
TITLE Meal System Printer Server
micromamba run -r _conda -n msp python main.py