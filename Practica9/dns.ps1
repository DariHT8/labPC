$dns =  ipconfig /displaydns 
$Path = "C:\Users\Hurtado\Documents\labPC\Practica9\dnsResultados.txt"
$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($dns))
Set-Content -Value "$codificado" -Path $Path