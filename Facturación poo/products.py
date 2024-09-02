from clsjson import save,read
class Product:
    next = 0
    def __init__(self,descrip='ninguno', preci=0.00, stock=0):
        id_product=read('file/id.json')
        Product.next=id_product['id_product']
        Product.next += 1
        self.id =('P0'if id_product['id_product'] <10 else 'P')+str(Product.next)
        self.descrip = descrip
        self.preci = preci
        self.__stock = stock  
        id_product['id_product']=Product.next
        save(id_product,'file/id.json')           
    @property
    def stock(self):
        
        return self.__stock
    
    def __repr__(self):
        
        return f'Producto:{self.id} {self.descrip} {self.preci} {self.stock}'  
    
    def __str__(self):
        
        return f'Producto:{self.id} {self.descrip} {self.preci} {self.stock}'  
    
    def getJson(self):
       
        return {"id":self.id,"descripcion":self.descrip,"precio":self.preci,"stock": self.stock}
      
    def show(self):
        
       
        print(f'{self.id}  {self.descrip}           {self.preci}  {self.stock}')  