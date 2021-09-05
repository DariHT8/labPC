#!/bin/bash
function prueba (){
  for i in {1..10};
  do
    echo  $i 'x' $ola '=' $((i*ola))
  done
}

echo "¡Hola! Bienvenido a mi script en Bash"
read -p "Ingresa un numero diferente de 0: " ola
if [[ $ola != 0 ]];
  then
    echo "Puedes apreciar la tabla del " $ola
    prueba
  else
    echo "No escribiste un cáracter válido:("
  fi
