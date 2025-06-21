desicion1=input("Desea iniciar el programa? (si/no)").lower()
if desicion1=="si":
    #Listas
    clientes=["Alejandra","Fernando","Natalia"]
    productos=["Arrosz","Leche","Huevos"]
    print(f"Listas creadas:\nclientes: {clientes}\nproductos: {productos}")
    

    desicion2=input("Desea comprovar si Natalia esta entre los clientes y añadir a carlos? (si/no)").lower()
    if desicion2=="si":
        #1 añadir carlos
        if clientes.count("Natalia")!=0:
            clientes.append("Carlos")

    
    desicion3=input("Desea comprovar si Huevos esta entre los productos y añadir a pan? (si/no)").lower()
    if desicion3=="si":
        #2 añadir pan
        if productos.count("Huevos")!=0:
            productos.append("Pan")


    desicion4=input("Desea comprovar si Fernando esta entre los clientes y eliminarlo? (si/no)").lower()
    if desicion4=="si":
        #3 eliminar fernando
        if clientes.count("Fernando")!=0:
            clientes.remove("Fernando")


    desicion5=input("Desea comprovar si hay mas de 3 productos y eliminar el primero? (si/no)").lower()
    if desicion5=="si":
        #4 eliminar el primer elemento de productos
        if len(productos)>3:             
            productos.remove(productos[0])


    desicion6=input("Desea comprovar si Alejandra esta entre clientes y reemplazarla por Marcela? (si/no)").lower()
    if desicion6=="si":
        #5 remplazar alejandra por marcela
        if clientes.count("Alejandra")!=0:
            clientes[clientes.index("Alejandra")]="Marcela"
    

    desicion7=input("Desea crear las listas turno_caja y canasta_basica? (si/no)").lower()
    if desicion7=="si":
        #6 lista turno caja
        turno_caja=[clientes[0],clientes[1]]
        #7 lista canasta basica
        canasta_basica=[productos[-1],productos[-2]]


        desicion8=input("Desea comprobar si pan esta en la canasta basica y crear la tupla producto en oferta? (si/no)").lower()
        if desicion8=="si":
            #8 tupla producto oferta
            if canasta_basica.count("Pan")!=0:
                producto_oferta=("Pan",2500)


        desicion9=input("Desea comprobar si Marcela esta en el turno caja y añadir preferencial? (si/no)").lower()
        if desicion9=="si":
            #9 añadir preferencial
            if turno_caja.count("Marcela")!=0:
                turno_caja.append("Preferencial")


        desicion10=input("Desea comprobar si preferencial esta en el turno caja y crar el diccionario ventas? (si/no)").lower()
        if desicion10=="si":
            #10 crear diccionario venta
            if turno_caja.count("Preferencial")!=0:
                    venta={"cliente":"Marcela","producto":"Leche","total":3500}


        desicion11=input("Desea comprobar si existe el diccionario venta y añadir el medio de pago? (si/no)").lower()
        if desicion11=="si":
            #11 comprobar si el diccionario venta existe
            try:
                venta["medio_pago"]="Tarjeta debito"
            except NameError:
                print("Venta no existe")


        desicion12=input("Desea comprobar si el azucar esta entre en los productos y si no agregarla? (si/no)").lower()
        if desicion12=="si":
            #12 agregar azucar
            if productos.count("Azucar")==0:
                productos.append("Azucar")


        desicion13=input("Desea comprobar si Fernando esta entre clientes y si no volver a agregarlo? (si/no)").lower()
        if desicion13=="si":
            #13 agregar a fernando
            if clientes.count("Fernando")==0:
                clientes.append("Fernando")
        

        desicion14=input("Desea ver el resumen de lo que se hizo en el programa? (si/no)").lower()
        if desicion14=="si":
            #14 imprimir
            print(f"clientes: {clientes}\nproductos: {productos}\nturno_caja: {turno_caja}\ncanasta_basica: {canasta_basica}\nTUPLA(producto_oferta): {producto_oferta}")
            try:
                print(f"venta: {venta}")
            except NameError:
                print("El diccionario venta no existe")


    else:
        print(f"Sin estas listas no puede continuar el programa")
        desicion7_1=input("desea ver el resumen de lo echo por el programa? (si/no)").lower()
        if desicion7_1=="si":
            print(f"Listas:\nclientes: {clientes}\nproductos: {productos}")
        else:
            print("Programa finalizado")


else:
    print("ok, hasta luego\nPrograma finalizado")
    

    

    

    
