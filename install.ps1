# Author: Guillermo Robles
#
# Installs all the TTF fonts in the current computer (except the original)

# Some definition
$FONTS=0x14

# Get Fonts directory
$objShell = New-Object -ComObject Shell.Application #Create a new Shell
$fontFolder = $objShell.Namespace($FONTS)

# Get all Codified fonts in directory
Get-ChildItem -recurse . |
  Where-Object {($_.name -match "Codified*") -and ($_.extension -eq ".ttf")} |
  ForEach-Object {
      # For each font, copy it to the Fonts directory
      $fontFolder.CopyHere($_.fullname)
      Write-Output "Installed $_.name"
  }
