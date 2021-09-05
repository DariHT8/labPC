function Fecha{
for ($i=1){
Get-Date -DisplayHint Date
exit
}
}
function Hora{
for ($i=2){
Get-Date -DisplayHint Time
exit
}
}

Write-Host "¡Hola! Bienvenido a mi función de PowerShell"
$i= Read-Host -Prompt "¿Qué desea ver? [1] Fecha, [2] Hora"
switch($i){
    1{
    Fecha}2{
    Hora}
    }