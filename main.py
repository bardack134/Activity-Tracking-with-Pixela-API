import requests
from constants import *



#TODO:usaremos el metodo post para crear una cuenta
pixela_api="https://pixe.la/v1/users"


#parameters que recibe nuestra API
parameters={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes", 
    "notMinor":"yes",
    
}


#solicitud post a nuestra api, para crear la account
# response=requests.post(pixela_api, json=parameters)


# miramos la respuesta del servidor, para saber si fue exitosa o no nuestra peticion
# print(response.text)


#vamos a crear un nuevo graph para nuestro usuario
graph_headers={
    'X-USER-TOKEN':TOKEN 
}


#informacion encontrada en la documentacion de la api
graph_parameters={
    "id":"graph134",
    "name":"Japanese Graph",
    "unit":"Hours",
    "type":"float",
    "color":"momiji",
    "timezone":"Asia/Tokyo",
}


graph_end_point=f'https://pixe.la/v1/users/{USERNAME}/graphs'


#post request para crear nuestra grafica
response=requests.post(graph_end_point, json=graph_parameters, headers=graph_headers)


# miramos la respuesta del servidor, para saber si fue exitosa o no nuestra peticion
print(response.text)


#NOTE: https://docs.pixe.la/entry/post-graph
#to check our graph, see api documentaqtion


#Enviando informacion a nuestra grafica


