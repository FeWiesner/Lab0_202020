import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=sep)
        for row in spamreader: 
            lst.append(row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Cantidad de peliculas por titulo")
    print("4- Cantidad de peliculas con calificaciones positivas (>=6) de un director")
    print("0- Salir")

def countMoviesByName(movieMame, lst):
    #Contar la cantidad de peliculas con titulo que inclue movieName
    if len(lista)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        moviesCount=0
        for mov in lst:
            if movieMame.lower() in mov[5].lower(): #comparar con el titulo (columna 5)
                moviesCount+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return moviesCount

def countGoodMoviesByDirector(lastName, lst):
    #Contar la cantidad de peliculas con calificación promedio >= 6
    #Donde el director tiene el apellido=lastName
    return 0


if __name__ == "__main__":
    lista = [] #instanciar una lista vacia
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv", lista) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0:
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                movieName =input('Ingrese parte del titulo de la pelicula\n')
                moviesCount=countMoviesByName(movieName,lista)
                print("Peliculas que contienen '", movieName ,"' en el titulo: ",moviesCount)
            elif int(inputs[0])==4: #opcion 4
                lastName =input('Ingrese el apellido del director\n')
                moviesCount=countGoodMoviesByDirector(lastName,lista)
                print("Peliculas con calificación positiva de '", lastName ,"':",moviesCount," en construcción ...")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
