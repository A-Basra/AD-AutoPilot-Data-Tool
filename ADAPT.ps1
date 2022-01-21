
$Creds = Get-Credential
$OUPath = $args[0]
$Share = $args[1]

$GatherHH = {
    
    $checknuget = Get-PackageProvider -Name Nuget
    $checkapinfo = Test-Path -Path "C:\Program Files\WindowsPowerShell\Scripts\Get-WindowsAutoPilotInfo.ps1" -PathType Leaf 
    $testmap = Test-Path P:\

    Set-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value '1' -Type DWord

    Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value '1' -Type DWord

    [Net.ServicePointManager]::SecurityProtocol


    if($testmap -eq "True"){Write-Host("Drive Mounted")}
    else{New-PSDrive -Name P -PSProvider Filesystem -Root $Share -Credential $Username -Persist}



    if($checknuget){Write-Host("Nuget Installed")}
    else{Write-Host("Installing NuGet")
         Install-PackageProvider -Name NuGet -Force}


    if($checkapinfo -eq "True"){Write-Host("Get-WindowsAutoPilotInfo Already Installed")
    }else{Write-Host("Installing Get-WindowsAutoPilotInfo")
          Install-Script -Name Get-WindowsAutoPilotInfo -Force 
    }

    Set-Location -Path "P:\"
    if(Test-Path P:\AutoPilot){Write-Host("AutoPilot Folder Found")}else{mkdir AutoPilot}
    Set-Location -Path "P:\AutoPilot"
    Get-WindowsAutoPilotInfo.ps1 -OutputFile AutoPilSWID.csv -Append
    Set-ExecutionPolicy Restricted -Force 

}

$PCName = $OUPath | Foreach {
    Get-ADComputer -Filter * -Properties * -SearchBase $_ |
        Select-Object -ExpandProperty Name
}


Invoke-Command -ComputerName $PCName -ScriptBlock $GatherHH -Credential $Creds