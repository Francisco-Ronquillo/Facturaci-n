from Crud import ICrud
import time
import datetime
from saleDetail import SaleDetail
from sales import Sale
from products import Product
from employee import Cashier,Manager
from clsjson import save,read,find
from client import RegularClient,VipClient
from validaciones import Validar
from components import Menu,limpiarPantalla,dibujarCabez,gotoxy,RED,GREEN,BLUE,RESET

class menuClientes(ICrud):
   def create():
      type_client=''
      limpiarPantalla()
      dibujarCabez('Registro de cliente')
      print('''Seleccione tipo de cliente
            1)Regular
            2)Vip''')
      type_client=input('Escoja una opcion 1..2: ')
      if type_client not in {'1','2'}:
         print('Opcion invalida')
         return
      nombre=Validar.letras('Ingrese el nombre del cliente:  ',1,9)
      apellido=Validar.letras('Ingrese el apellido del cliente: ',1,10)
      dni=Validar.Dni('Ingrese su cedula: ',1,11)
      if type_client=='1':
         option=''
         while True:
            gotoxy(1,12);option=input('¿El cliente quiere una tarjeta de descuento?(s/n): ')
            if option.lower()=='s':
               card =True
               break
            if option.lower()=='n':
               card=False
               break
            else:
               gotoxy(50,12);print(' '*20)
               gotoxy(50,12);print('Opcion no valida')
               time.sleep(2)
               gotoxy(50,12);print(' '*20)
         cliente=RegularClient(nombre,apellido,dni,card)
      else:
         cliente=VipClient(nombre,apellido,dni,)
      clients=read('file/clients.json')
      clients.append(cliente.getJson())
      save(clients,'file/clients.json')
      gotoxy(1,14);print('Cliente registrado con exito')
      input('Presione una tecla para continuar...')
   def update():
      limpiarPantalla()
      dibujarCabez('Actualizacion de datos cliente')
      dni=Validar.Dni('Ingrese la cedula del cliente: ',1,4)
      clients=read('file/clients.json')
      update_clients=[]
      found=False
      for client in clients:
         
         if client['dni'] ==dni:
            found=True
            print('Cliente encontrado')
            nombre=Validar.letras('Ingrese el nuevo nombre del cliente: ',1,8)
            apellido=Validar.letras('Ingrese el nuevo apellido del cliente: ',1,9)
            if nombre:
               client['nombre']=nombre
            if apellido:
               client['apellido']=apellido
         update_clients.append(client)
      if found:
         gotoxy(1,10);print('Actualizado con exito')
         save(update_clients,'file/clients.json')
         input('Presione una tecla para continuar..')
      else:
         gotoxy(1,10);print('Cliente no encontrado')
         time.sleep(2)
   def delete():
      limpiarPantalla()
      dibujarCabez('Eliminar cliente')
      dni=Validar.Dni('Ingrese la cedula del cliente: ',1,4)
      clients=read('file/clients.json')
      update_clients=[]
      found=False
      for client in clients:
         if client['dni'] ==dni:
            found=True
            gotoxy(1,5);print(('Cliente encontrado'))
         
         
      if found:
         while True:
               gotoxy(1,6);decision=input('Esta seguro de eliminar los datos?(s/n): ')
               if decision.lower()=='s':
                  for client in clients:
                     if client['dni']!=dni:
                        update_clients.append(client)
                  print('Datos eliminados con exito')
                  save(update_clients,'file/clients.json')
                  break
               elif decision.lower()=='n':
                  print('Operacion cancelada')
                  break
               else:
                  gotoxy(40,6);print(' '*20)
                  gotoxy(40,6);print('Opcion no valida')
                  gotoxy(40,6);print(' '*20)
                  time.sleep(2)
      else:
         gotoxy(1,5);print('Cliente no encontrado')
         time.sleep(2)
      input('Presiona una tecla para continuar')
   def consult():
      limpiarPantalla()
      dibujarCabez('Buscar cliente')
      dni=Validar.Dni('Ingrese la cedula del cliente: ',1,4)
      cliente_buscados=find("file/clients.json","dni",dni)
      if cliente_buscados:
         cliente_buscado=cliente_buscados[0]
         print('Estos son los datos encontrados')
         print(GREEN+'Nombre: '+BLUE+f"{cliente_buscado['nombre']}")
         print(GREEN+'Apellido: '+BLUE+f"{cliente_buscado['apellido']}")
         print(GREEN+'DNI: '+BLUE+f"{cliente_buscado['dni']}")
         
      else:
         print('Cliente no encontrado')
      input(BLUE+ "Presione una tecla para continuar...")
class menuProducto(ICrud):
   def create():
      limpiarPantalla()
      dibujarCabez('Registro de producto')
      nombre=Validar.letras('Ingrese el nombre del producto: ',1,4)
      valor=Validar.numerosDecimales('Ingrese el precio del producto: ',1,5)
      stock=Validar.numerosEnteros('Ingrese el stock del producto: ',1,6)
      while True:
         gotoxy(1,7);option=input('¿Desea registrar el producto?: ')
         if option.lower()=='s':
            producto=Product(nombre,valor,stock)
            productos=read('file/producto.json')
            productos.append(producto.getJson())
            save(productos,'file/producto.json')
            gotoxy(1,8);print('Producto registrado con exito')
            time.sleep(2)
            break
         elif option.lower()=='n':
            gotoxy(1,8);print('Opereacion cancelada')
            break
         else:
            gotoxy(32,7);print(' '*20)
            gotoxy(32,7);print('Opcion no valida')
            time.sleep(2)
            gotoxy(32,7);print(' '*20)
      input('Presiona una tecla para continuar...')
   def update():
      limpiarPantalla()
      dibujarCabez('Actualizacion de producto')
      products=read('file/producto.json')
      id=input('Ingrese el id del producto: ')
      update_productos=[]
      found=False
      for product in products:
         if product['id'] == id:
            found=True
            print('Producto encontrado')
            precio=Validar.numerosDecimales('Ingrese el precio del producto: ',1,6)
            stock=Validar.numerosEnteros('Ingrese el stock del producto: ',1,7)
            if precio:
               product['precio']=precio
            if stock:
               product['stock']=stock
         update_productos.append(product)
      if found:
         print('Actualizado con exito')
         save(update_productos,'file/producto.json')

      else:

         print('Producto no encontrado')
         time.sleep(2)
   def delete():
      limpiarPantalla()
      dibujarCabez('Eliminar producto')
      id=input('Ingrese el id del producto: ')
      products=read('file/producto.json')
      update_products=[]
      found=False
      for product in products:
         if product['id']==id:
            found=True 
            print('Producto encontrado')
         
         
      if found:
         while True:
               gotoxy(1,6);decision=input('Esta seguro de eliminar los datos del producto?(s/n): ')
               if decision.lower()=='s':
                  for product in products:
                     if product['id']!=id:
                        update_products.append(product)
                  print('Datos eliminados con exito')
                  save(update_products,'file/producto.json')
                  break
               elif decision.lower()=='n':
                  print('Operacion cancelada')
                  break
               else:
                  gotoxy(55,6);print(' '*20)
                  gotoxy(55,6);print('Opcion no valida')
                  time.sleep(2)
                  gotoxy(55,6);print(' '*20)
      else:
         print('Producto no encontrado')
         time.sleep(2)
      input('Preciona una tecla para continuar...')
   def consult():
      limpiarPantalla()
      dibujarCabez('Buscar producto')
      id=input('Ingrese el codigo del producto: ')
      productos_buscados=find("file/producto.json","id",id)
      if productos_buscados:
         producto_buscado=productos_buscados[0]
         print('Estos son los datos encontrados')
         print(GREEN+'Descripcion: '+BLUE+f"{producto_buscado['descripcion']}")
         print(GREEN+'Valor: '+BLUE+f"{producto_buscado['precio']}")
         print(GREEN+'Stock: '+BLUE+f"{producto_buscado['stock']}"+RESET)
         
      else:
         print('Producto no encontrado')
      input(BLUE+ "Presione una tecla para continuar...")
class menuEmpleado(ICrud):
   def create():
      limpiarPantalla()
      type_emplooye=''
      limpiarPantalla()
      dibujarCabez('Registro de empleados')
      print('''Seleccione tipo de empleado
            1)Cajero
            2)Gerente''')
      type_emplooye=input('Escoja una opcion 1..2: ')
      if type_emplooye not in {'1','2'}:
         print('Opcion invalida')
         return
      nombre=Validar.letras('Ingrese el nombre del empleado: ',1,9)
      apellido=Validar.letras('Ingrese el apellido del empleado: ',1,10)
      dni=Validar.Dni('Ingrese su cedula: ',1,11)
      if type_emplooye=='1':
         option=''
         emplooye=Cashier(nombre,apellido,dni)
      else:
         option=''
         emplooye=Manager(nombre,apellido,dni,)
      emplooyes=read('file/emplooye.json')
      emplooyes.append(emplooye.getJson())
      save(emplooyes,'file/emplooye.json')
      print('Empleado creado con exito')
      time.sleep(2)
   def update():
      limpiarPantalla()
      dibujarCabez('Actualizacion de datos empleado')
      dni=Validar.Dni('Ingrese la cedula del empleado: ',1,4)
      emplooyes=read('file/emplooye.json')
      update_emplooye=[]
      found=False
      for emplooye in emplooyes:
         if emplooye['dni'] ==dni:
            found=True
            print('Empleado encontrado')
            nombre=Validar.letras('Ingrese el nuevo nombre del empleado: ',1,6)
            apellido=Validar.letras('Ingrese el nuevo apellido del empleado: ',1,7)
            if nombre:
               emplooye['nombre']=nombre
            if apellido:
               emplooye['apellido']=apellido
         update_emplooye.append(emplooye)
      if found:
         gotoxy(1,8);print('Actualizado con exito')
         save(update_emplooye,'file/emplooye.json')
      else:
         print('Empleado no encontrado')
         time.sleep(2)
      input('Presione una tecla para continuar...')
   def delete():
      limpiarPantalla()
      dibujarCabez('Eliminar cliente')
      dni=Validar.Dni('Ingrese la cedula del cliente: ',1,4)
      emplooyes=read('file/emplooye.json')
      update_emplooyes=[]
      found=False
      for emplooye in emplooyes:
         if emplooye['dni'] ==dni:
            found=True
            print('Empleado encontrado')
         
         
      if found:
         
         while True:
               gotoxy(1,6);decision=input('Esta seguro de eliminar los datos?(s/n): ')
               if decision.lower()=='s':
                  for emplooye in emplooyes:
                     if emplooye['dni']!=dni:
                        update_emplooyes.append(emplooye)
                  print('Datos eliminados con exito')
                  save(update_emplooyes,'file/emplooye.json')
                  break
               elif decision.lower()=='n':
                  print('Operacion cancelada')
                  break
               else:
                  gotoxy(44,6);print(' '*20)
                  print('Opcion no valida')
                  time.sleep(2)
                  gotoxy(44,6);print(' '*20)
      else:
         print('Empleado no encontrado')
         time.sleep(2)
      input('Presiona una tecla para continuar...')
   def consult():
      limpiarPantalla()
      dibujarCabez('Buscar cliente')
      dni=Validar.Dni('Ingrese la cedula del empleado: ',1,4)
      empleados_buscados=find("file/emplooye.json","dni",dni)
      if empleados_buscados:
         empleado_buscado=empleados_buscados[0]
         print('Estos son los datos encontrados')
         print(GREEN+'Nombre: '+BLUE+f"{empleado_buscado['nombre']}")
         print(GREEN+'Apellido: '+BLUE+f"{empleado_buscado['apellido']}")
         print(GREEN+'DNI: '+BLUE+f"{empleado_buscado['dni']}")
         
      else:
         print('Empleado no encontrado')
      input(BLUE+ "Presione una tecla para continuar...")
class menuVenta(ICrud):
   def create():
      limpiarPantalla()
      #CABEZA DE VENTA
      dibujarCabez('Registro de venta')
      gotoxy(35,4);print('Empresa:El rosado'+' '*3+'Ruc:1825445154')
      gotoxy(5,5);print(f"Factura#:F0999999 {' '*3} Fecha:{(datetime.datetime.now()).strftime('%d/%m/%Y %H:%M:%S')}")
      gotoxy(66,5);print("Subtotal:")
      gotoxy(66,6);print("Decuento:")
      gotoxy(66,7);print("Iva     :")
      gotoxy(66,8);print("Total   :")
      gotoxy(3,7);print("Codigo cajero:")
      gotoxy(18,7);id=input()
      emplooyes=find('file/emplooye.json','codigo_empleado',id)
      if not emplooyes:
         gotoxy(18,7);print(' '*20)
         gotoxy(18,7);print('Empleado no existe')
         time.sleep(2)
         return
      emplooye=emplooyes[0]
      emplo=Cashier(emplooye['nombre'],emplooye['apellido'],emplooye['dni'],0)
      gotoxy(18,7);print(' '*20)
      gotoxy(18,7);print(emplo.fullName())
      gotoxy(15,8);print("Cedula:")
      gotoxy(22,8);dni=Validar.Dni(' ',22,8)
      clients=find('file/clients.json','dni',dni)
      if not clients:
         gotoxy(22,9);print(' '*20)
         gotoxy(22,9);print('Cliente no existe')
         time.sleep(2)
         return
      client=clients[0]
      if client['valor']==0.1:
         
         cli=RegularClient(client['nombre'],client['apellido'],client['dni'],client['valor'])
      else:
         cli=VipClient(client['nombre'],client['apellido'],client['dni'],0)
      sale=Sale(cli)
      gotoxy(22,8);print(' '*20)
      gotoxy(30,8);print(cli.fullName())
      gotoxy(2,9);print(GREEN+"*"*90+RESET) 
      gotoxy(5,10);print(RED+"Linea") 
      gotoxy(12,10);print("Id_Articulo") 
      gotoxy(24,10);print("Descripcion") 
      gotoxy(38,10);print("Precio") 
      gotoxy(48,10);print("Cantidad") 
      gotoxy(58,10);print("Subtotal") 
      gotoxy(70,10);print("n->Terminar Venta)"+RESET)
      #Detalle de venta
      line=1
      follow='s'
      while follow.lower()=='s':
         gotoxy(6,10+line);print(line)
         gotoxy(16,10+line);
         id=input()
         prods=find('file/producto.json','id',id)
         if not prods:
            gotoxy(16,10+line);print('Producto no existe')
            time.sleep(1)
            gotoxy(16,10+line);print(' '*20)
         else:
            prod=prods[0]
            product=Product(prod['descripcion'],prod['precio'],prod['stock'],)
            gotoxy(24,10+line);print(product.descrip)
            gotoxy(38,10+line);print(product.preci)
            gotoxy(49,10+line);qyt=Validar.numerosEnteros('',49,10+line)
            gotoxy(59,10+line);print(round(product.preci*qyt,2))
            sale.add_detail(product,qyt)
            gotoxy(76,5);print(round(sale.subtotal,2))
            gotoxy(76,6);print(round(sale.discount,2))
            gotoxy(76,7);print(round(sale.iva,2))
            gotoxy(76,8);print(round(sale.total,2))
            gotoxy(74,10+line);follow=input().lower() or 's'
            gotoxy(76,10+line);print(GREEN+"✔"+RESET)  
            line += 1
      while True:
         gotoxy(15,10+line);print(RED+'Esta seguro de grabar la venta?(s/n)')
         gotoxy(54,10+line);procesar=input().lower()
         if procesar=='s':
            gotoxy(15,11+line);print("Venta Grabada satisfactoriamente"+RESET)
            facturas=read('file/factura.json')
            data=sale.getJson()
            facturas.append(data)
            save(facturas,'file/factura.json')
            time.sleep(2)
         elif procesar=='n':
            gotoxy(20,11+line);print("Venta Cancelada"+RESET)    
            time.sleep(2) 
         else:
            gotoxy(54,10+line);print(' '*20)
            gotoxy(54,10+line);print('Opcion no valida')
            time.sleep(2)
            gotoxy(54,10+line);print(' '*20)
      input('Presiona una tecla para continuar....')
   def delete():
      limpiarPantalla()
      dibujarCabez('Eliminar cliente')
      nFactura=input('Ingrese el numero de la factura: ')
      facturas=read('file/factura.json')
      update_facturas=[]
      found=False
      for factura in facturas:
         if factura['factura'] ==nFactura:
            found=True
            print('Factura encontrado')
         
         
      if found:
         
         while True:
               gotoxy(1,6);decision=input('Esta seguro de eliminar los datos?(s/n): ')
               if decision.lower()=='s':
                  for factura in facturas:
                     if factura['factura']!=nFactura:
                        update_facturas.append(factura)
                  print('Datos eliminados con exito')
                  save(update_facturas,'file/factura.json')
                  break
               elif decision.lower()=='n':
                  print('Operacion cancelada')
                  break
               else:
                  gotoxy(44,6);print(' '*20)
                  print('Opcion no valida')
                  time.sleep(2)
                  gotoxy(44,6);print(' '*20)
      else:
         print('Factura no encontrado')
         time.sleep(2)
      input('Presiona una tecla para continuar...')
   def consult():
      limpiarPantalla()
      dibujarCabez('Buscar factura')
      nFactura=input('Ingrese el numero de factura: ')
      facturas=find("file/factura.json","factura",nFactura)
      linea=1
      if facturas:
         factura=facturas[0]
         print('Estos son los datos encontrados')
         print(GREEN+'Fecha: '+BLUE+f"{factura['Fecha']}")
         print(GREEN+'Cliente: '+BLUE+f"{factura['cliente']}")
         gotoxy(3,9);print('Producto')
         gotoxy(15,9);print('Cantidad')
         gotoxy(25,9);print('Precio')
         for detalle in  factura['detalle']:
            gotoxy(3,9+linea);print(detalle['producto'])
            gotoxy(15,9+linea);print(detalle['cantidad'])
            gotoxy(25,9+linea);print(detalle['precio'])
            linea+=1
      else:
         print('Cliente no encontrado')
      gotoxy(3,9+linea);input(BLUE+ "Presione una tecla para continuar...")
option=''
while option!='5':
   limpiarPantalla()
   menuMain=Menu('Menu Facturacion',['Cliente','Producto','Empleado','Venta','Salir'])
   option=menuMain.menu()

   if option=='1':
      option=''
      while option!='5':
         limpiarPantalla()
         menuCliente=Menu('Menu Cliente',['Insertar','Actualizar','Eliminar','Consultar','Salir'])
         option=menuCliente.menu()
         if option=='1':
            menuClientes.create()
         if option=='2':
            menuClientes.update()
         if option=='3':
            menuClientes.delete()
         if option=='4':
            menuClientes.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='2':
      option=''
      while option!='5':
         limpiarPantalla()
         menuCliente=Menu('Menu Producto',['Insertar','Actualizar','Eliminar','Consultar','Salir'])
         option=menuCliente.menu()
         if option=='1':
            menuProducto.create()
         if option=='2':
            menuProducto.update()
         if option=='3':
            menuProducto.delete()
         if option=='4':
            menuProducto.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='3':
      option=''
      while option!='5':
         limpiarPantalla()
         menuCliente=Menu('Menu Empleado',['Insertar','Actuazilar','Eliminar','Consultar','Salir'])
         option=menuCliente.menu()
         if option=='1':
            menuEmpleado.create()
         if option=='2':
            menuEmpleado.update()
         if option=='3':
            menuEmpleado.delete()
         if option=='4':
            menuEmpleado.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='4':
      option=''
      while option!='5':
         limpiarPantalla()
         menuCliente=Menu('Menu Venta',['Registrar','Eliminar','Consultar','Salir'])
         option=menuCliente.menu()
         if option=='1':
            menuVenta.create()
         if option=='2':
            menuVenta.delete()
         if option=='3':
            menuVenta.consult()
         if option=='4':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='5':
      limpiarPantalla()
      print('Saliendo del programa')
      time.sleep(2)