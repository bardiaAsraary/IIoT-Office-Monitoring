# Start WAMP router
Start-Process -FilePath "python" -ArgumentList "wamp_router/router.py" -WindowStyle Minimized

# Generate certificates if missing
if (-not (Test-Path "certs/ca-cert.pem")) {
    Write-Host "Generating certificates..."
    Set-Location certs
    .\generate_certs.ps1
    Set-Location ..
}

# Start Node-RED
Start-Process -FilePath "node-red" -ArgumentList "-s node-red/settings.js" -WindowStyle Minimized

# Start Renode
Start-Process -FilePath "renode" -ArgumentList "renode/hifive1.resc"

Write-Host "All systems started!"
Write-Host "Access dashboard at: http://localhost:1880/ui"