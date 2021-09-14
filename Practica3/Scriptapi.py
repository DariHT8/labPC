import requests
var = input ("Bienvenido a mi Práctica 3, ¿deseas ver mi perfil? s/n ")
if var == 's' :
  usuario = "DariHT8"
  url = 'https://api.github.com/users/'
  res = requests.get(url+usuario)
  print ("Esta es la información de mi perfil:")
  print (res.text)
  var2 = input("¿Deseas ver la información de mis seguidores? s/n ")
  if var2 == 's' :
    followers = 'https://api.github.com/users/DariHT8/followers'
    res2 = requests.get(followers)
    print ("Esta es la información de mis seguidores:")
    print(res2.text)
    var3 = input("¿Deseas ver la información de mis eventos? s/n ")
    if var3 == 's' :
      events = 'https://api.github.com/users/DariHT8/events'
      res3 = requests.get(events)
      print ("Esta es la información de mis eventos:")
      print(res3.text)
      var4 = input("¿Deseas ver la información de mis eventos recibidos? s/n ")
      if var4 == 's' :
        received_events = 'https://api.github.com/users/DariHT8/received_events'
        res4 = requests.get(received_events)
        print ("Esta es la información de mis eventos recbidos:")
        print(res4.text)
        var5 = input("¿Deseas ver la información de mis repositorios? s/n ")
        if var5 == 's' :
          repos = 'https://api.github.com/users/DariHT8/repos'
          res5 = requests.get(repos)
          print ("Esta es la información de mis repositorios:")
          print(res5.text) 
        else :
          print ("Hasta luego:)")
      else :
        print ("Hasta luego:)")
    else :
      print ("Hasta luego:)")
  else :
    print ("Hasta luego:)") 
else :
  print ("Hasta luego:)")
