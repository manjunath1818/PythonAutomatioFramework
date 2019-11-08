echo off
tasklist /fi "imagename eq IEDriverServer64.exe" |find ":" > nul
if errorlevel 1 taskkill /f /im "IEDriverServer.exe"

tasklist /fi "imagename eq IEDriverServer.exe" |find ":" > nul
if errorlevel 1 taskkill /f /im "IEDriverServer.exe"

tasklist /fi "imagename eq chromedriver.exe" |find ":" > nul
if errorlevel 1 taskkill /f /im "chromedriver.exe"

cd /D %temp%
for /d %%D in (*) do rd /s /q "%%D"
del /f /q *

rd /s /q %systemdrive%\$RECYCLE.BIN

exit