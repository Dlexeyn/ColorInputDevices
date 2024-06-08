@echo off

for /f "tokens=*" %%i in ('powershell -command "Get-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name Wallpaper | Select-Object -ExpandProperty Wallpaper"') do (
    set "wallpaper_path=%%i"
)

python main.py %wallpaper_path%
pause
