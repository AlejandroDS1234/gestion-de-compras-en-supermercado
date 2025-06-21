#Listas
clientes=["Alejandra","Fernando","Natalia"]
productos=["Arrosz","Leche","Huevos"]


#1 añadir carlos
if clientes.count("Natalia")!=0:
    clientes.append("Carlos")


#2 añadir pan
if productos.count("Huevos")!=0:
    productos.append("Pan")

    
#3 eliminar fernando
if clientes.count("Fernando")!=0:
    clientes.remove("Fernando")

    
#4 eliminar el primer elemento de productos
if len(productos)>3:
    productos.remove(productos[0])

    
#5 remplazar alejandra por marcela
if clientes.count("Alejandra")!=0:
    clientes[clientes.index("Alejandra")]="Marcela"

    
#6 lista turno caja
turno_caja=[clientes[0],clientes[1]]


#7 lista canasta basica
canasta_basica=[productos[-1],productos[-2]]


#8 tupla producto oferta
if canasta_basica.count("Pan")!=0:
    producto_oferta=("Pan",2500)

    
#9 añadir preferencial
if turno_caja.count("Marcela")!=0:
    turno_caja.append("Preferencial")

    
#10 crear diccionario venta
if turno_caja.count("Preferencial")!=0:
    vent={"cliente":"Marcela","producto":"Leche","total":3500}

    
#11 comprobar si el diccionario venta existe
try:
    venta["medio_pago"]="Tarjeta debito"
except NameError:
    print("Venta no existe")

    
#12 agregar azucar
if productos.count("Azucar")==0:
    productos.append("Azucar")

    
#13 agregar a fernando
if clientes.count("Fernando")==0:
    clientes.append("Fernando")

    
#14 imprimir
print(f"clientes: {clientes}\nproductos: {productos}\nturno_caja: {turno_caja}\ncanasta_basica: {canasta_basica}\nTUPLA(producto_oferta): {producto_oferta}")
try:
    print(f"venta: {venta}")
except NameError:
    print("El diccionario venta no existe")