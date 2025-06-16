# INSTALL WITHOUT CHOCOLATEY

# 1. Install Python dependencies
pip install autobahn[twisted] service_identity pyopenssl

# 2. Install Node-RED
npm install -g node-red
npm install node-red-dashboard node-red-contrib-wamp

# 3. Install Renode (Windows)
Write-Host "Downloading Renode..."
$renodeUrl = "https://dl.antmicro.com/projects/renode/builds/renode-latest.windows-portable.zip"
Invoke-WebRequest -Uri $renodeUrl -OutFile "renode.zip"
Expand-Archive -Path "renode.zip" -DestinationPath "renode-install"
Move-Item -Path "renode-install\*" -Destination "C:\renode" -Force
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\renode", "Machine")
Remove-Item "renode.zip"
Remove-Item "renode-install" -Recurse

# 4. Install RISC-V Toolchain
Write-Host "Downloading RISC-V Toolchain..."
$toolchainUrl = "https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v12.2.0-1/xpack-riscv-none-elf-gcc-12.2.0-1-win32-x64.zip"
Invoke-WebRequest -Uri $toolchainUrl -OutFile "riscv-toolchain.zip"
Expand-Archive -Path "riscv-toolchain.zip" -DestinationPath "C:\riscv-toolchain"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\riscv-toolchain\bin", "Machine")
Remove-Item "riscv-toolchain.zip"

Write-Host "Installation complete! Please restart your terminal."