import json
def save(data,filename):
        with open(filename, 'w') as file:
            json.dump(data, file)# dump:graba datos a un archivo json
def read(filename):
    try:
        with open(filename,'r') as file:
            data = json.load(file)# load:carga datos desde un archivo json
    except FileNotFoundError:
        data = []
    return data
     
def find(filename,atributo,buscado):
    try:
        with open(filename,'r') as file:
            datas = json.load(file)
            data = [item for item in datas if item[atributo] == buscado ]
    except FileNotFoundError:
        data = []
    return data

