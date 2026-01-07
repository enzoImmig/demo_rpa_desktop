$exclude = @("venv", "desktopBotDemo.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desktopBotDemo.zip" -Force