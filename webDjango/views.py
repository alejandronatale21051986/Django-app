from django.http import HttpResponse
from django.shortcuts import render #

def saludo(request ):
    #return HttpResponse('Hola te saludo desde mi funcion django')
    # 3 argumentos.!) reques =peticion , 2 nombre de archivo html 3, diccionario de clave y valor
    return render(request,'index.html',{
        'mensaje':'ingreso',
        'titulo':'personas',
        'personas':[
            {'titulo':'Campera','precio':15,'stock':False},
            {'titulo':'Pantalon','precio':24,'stock':True},
            {'titulo':'Remera','precio':11,'stock':False},
            {'titulo':'Gorra','precio':44,'stock':True},
        ]

    })
    
    