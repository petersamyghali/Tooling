@echo off
setlocal EnableDelayedExpansion
IF NOT EXIST TXTFiles (
MKDIR TXTFiles
)

IF NOT EXIST SFiles (
MKDIR SFiles
)

IF NOT EXIST HFiles (
MKDIR HFiles
)
for /f "tokens=1-4" %%a in (Input.txt) do (

if not exist %%a (
mkdir %%a
)
cd %%a
if not exist %%b (
echo 0 >%%b
) else (
set /p count=<%%b
set /a count+=1
echo !count!>%%b
)

if not exist %%c (
echo 0 >%%c
) else (
set /p count=<%%c
set /a count+=1
echo !count!>%%c
)

if not exist %%d (
echo 0 >%%d
) else (
set /p count=<%%d
set /a count+=1
echo !count!>%%d
)
cd ..
COPY /Y %%a\*.txt TXTFiles>nul
COPY /Y %%a\*.c SFiles>nul
COPY /Y %%a\*.h HFiles>nul
)


