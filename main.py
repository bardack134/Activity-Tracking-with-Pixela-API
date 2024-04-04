import requests
from constants import *
from datetime import date


#TODO:USAREMOS EL METODO POST PARA CREAR UNA CUENTA
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


#TODO:VAMOS A CREAR UN NUEVO GRAPH PARA NUESTRO USUARIO
# graph_headers={
#     'X-USER-TOKEN':TOKEN 
# }


#informacion encontrada en la documentacion de la api
# graph_parameters={
#     "id":GRAPH_ID,
#     "name":"Japanese Graph",
#     "unit":"Hours",
#     "type":"float",
#     "color":"momiji",
#     "timezone":"Asia/Tokyo",
# }


# graph_end_point=f'https://pixe.la/v1/users/{USERNAME}/graphs'


#post request para crear nuestra grafica
# response=requests.post(graph_end_point, json=graph_parameters, headers=graph_headers)


# miramos la respuesta del servidor, para saber si fue exitosa o no nuestra peticion
# print(response.text)


#NOTE: https://docs.pixe.la/entry/post-graph (https://pixe.la/v1/users/bardack134/graphs/graph134.html)
#to check our graph, more information in api documentaqtion


#TODO: ENVIANDO INFORMACION A NUESTRA GRAFICA
graph_creation_point=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'


graph_headers={
    'X-USER-TOKEN':TOKEN 
}


# Obtenemos la fecha de hoy y la convertimos a una cadena
today = str(date.today())


# Reemplazamos los guiones en la fecha con nada (los eliminamos)
today = today.replace('-', '')


graph_parameters={
    "date":today,
    # "date":'20240320',
    "quantity":input('How many hours did you study today: '),
    # "optionalData":"{\"key\":\"value\"}"
    }


#post request para crear nuestra grafica
# response=requests.post(graph_creation_point, json=graph_parameters, headers=graph_headers)


# miramos la respuesta del servidor, para saber si fue exitosa o no nuestra peticion
# print(response.text)


#TODO: ACTUALIZANDO UN DATO DE MI GRAFICA
# new_end_point=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}'


new_parameters={
    "quantity":"0.5",
    
    }

#post request para actrualizar un dato de la grafica
# response=requests.put(new_end_point, json=new_parameters, headers=graph_headers)


# miramos la respuesta del servidor, para saber si fue exitosa o no nuestra peticion
# print(response.text)


#TODO:BORRANDO UN DATO EN ESPECIFICO
delete_end_point=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20240401'


response=requests.delete(delete_end_point, headers=graph_headers)
print(response.text)