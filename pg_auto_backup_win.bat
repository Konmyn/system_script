@echo off
@setlocal enableextensions
@cd /d "%~dp0"

:: 设置路径
set PGHOME="C:\Program Files\PostgreSQL\9.6\bin"
set PGDATA=D:\pgdatabase
set BACKUP_DIR=D:\pgbackup

set day=%date%
:: 提取日期
for /f "tokens=1-3 delims=-/. " %%i in ("%day%") do (
    set /a sy=%%i, sm=100%%j %% 100, sd=100%%k %% 100
)
set DATE_1=%sy%-%sm:~-2%-%sd:~-2%
::echo %DATE_1%
::pause>nul

:: 7天前
set /a sd-=7
if %sd% leq 0 call :count

set DATE_2=%sy%-%sm:~-2%-%sd:~-2%

if exist %BACKUP_DIR%\db_back_%DATE_2% (del /f %BACKUP_DIR%\db_back_%DATE_2%)

if not exist %BACKUP_DIR%\db_back_%DATE_1% (%PGHOME%\pg_dump.exe -h localhost -p 5432 -U postgres -W admin odoo10en>%BACKUP_DIR%\db_back_%DATE_1%)

:count
set /a sm-=1
if !sm! equ 0 set /a sm=12, sy-=1
call :days
set /a sd+=days
if %sd% leq 0 goto count
goto :eof

:days
:: 获取指定月份的总天数
set /a leap="^!(sy %% 4) & ^!(^!(sy %% 100)) | ^!(sy %% 400)"
set /a max=28+leap
for /f "tokens=%sm%" %%i in ("31 %max% 31 30 31 30 31 31 30 31 30 31") do set days=%%i
goto :eof

echo Backup Taken Complete
pause
