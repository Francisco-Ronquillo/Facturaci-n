from clsjson import save,read
class employee:
    def __init__(self,first_name,last_name,dni):
        self.first_name=first_name
        self.last_name=last_name
        self.__dni=dni
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, value):
        if len(value) in (10, 13):
            self.__dni = value
        else:
            self.__dni ="9999999999"  
    def __str__(self):
        return f'Empleado: {self.first_name} {self.last_name}'  
    
    def fullName(self):
        return self.first_name + ' ' + self.last_name
    
    def show(self):
        print('   Nombres    Dni')
        print(f'{self.fullName()}  {self.dni}')  
class Cashier(employee):
    next=0
    def __init__(self,first_name,last_name,dni,cashier_code=0):
        super().__init__(first_name,last_name,dni)
        id_cashier=read('file/id.json')
        Cashier.next=id_cashier['id_cashier']
        Cashier.next+=1
        self.__cashier_code=('C0'if id_cashier['id_cashier']<10 else 'C')+str(Cashier.next)
        id_cashier['id_cashier']=Cashier.next
        save(id_cashier,'file/id.json')
    @property
    def cashier_code(self):
        return self.__cashier_code
    def show(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        print(f'Cliente Minorista: DNI:{self.dni} Nombre:{self.first_name} {self.last_name} Casher_Code:{self.cashier_code}')     

    def getJson(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"codigo_empleado": self.cashier_code}
class Manager(employee):
    next = 0  
    def __init__(self, first_name, last_name, dni):
        super().__init__(first_name, last_name, dni)
        id_manager=read('file/id.json')
        Manager.next=id_manager['id_manager']
        Manager.next += 1
        self.__manager_code = ('M0'if id_manager['id_manager']<10 else 'M') + str(Manager.next)
        id_manager['id_manager']=Manager.next
        save(id_manager,'file/id.json')

    @property
    def manager_code(self):
        return self.__manager_code
    def show(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        print(f'Cliente Minorista: DNI:{self.dni} Nombre:{self.first_name} {self.last_name}  Manager_code: {self.manager_code}')     

    def getJson(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"codigo_empleado": self.manager_code}