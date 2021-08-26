#!powershell

# Copyright: (c) 2015, Henrik Wallström <henrik@wallstroms.nu>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#Requires -Module Ansible.ModuleUtils.Legacy

$ErrorActionPreference = "Stop"

$params = Parse-Args $args
$name = Get-AnsibleParam -obj $params -name "name" -type "str" -failifempty $true
$site = Get-AnsibleParam -obj $params -name "site" -type "str" -failifempty $true
$application = Get-AnsibleParam -obj $params -name "application" -type "str" -failifempty $true

# Ensure WebAdministration module is loaded
if ($null -eq (Get-Module "WebAdministration" -ErrorAction SilentlyContinue)) {
  Import-Module WebAdministration
}

$result = @{
  directory = @{}
  changed = $true
};
# Construct path
$directory_path = "IIS:\Sites\$($site)\$($application)\$($name)"

try {
  If (Test-Path -LiteralPath $directory_path){
    Remove-Item -LiteralPath $directory_path -Recurse -Force
  }

} catch {
  Fail-Json $result $_.Exception.Message
}

# Result
$directory = Get-WebVirtualDirectory -Site $site -Name $name
$result.directory = @{
  PhysicalPath = $directory.PhysicalPath
}

Exit-Json -obj $result
