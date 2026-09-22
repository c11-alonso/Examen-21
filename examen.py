# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido: Catalina Alonso
# Curso:2° 1°
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
nombrep = input("ingresar el nombre del piloto")
print ("bienvenido/a", nombrep, "el combustible disponible inicial es 100")
cantidadv = 0
print ("cantidad de viajes realizados es cero", cantidadv)
cantidadvl = 0
print ("cantidad de viajes realizados a la lunaes cero", cantidadvl)
cantidadvm = 0
print ("cantidad de viajes realizados a marte es cero", cantidadvm)
cantidadvs = 0
print ("cantidad de viajes realizados a saturno es cero", cantidadvs)
destinos = ["luna", "marte", "saturno"]
costos = [20, 35, 50]



# =========================

# Crear las variables necesarias.
# Crear las listas de destinos y costos.
# Pedir el nombre del piloto.


# =========================
# ETAPA 2 - NAVEGACIÓN
print ("las opciones de viajes son luna, marte y saturno")
destino = input("elegi un destino")
if destino == "luna":
    print ("el combustible necesario es 20")
    print ("el viaje se realizó correctamente, el combustible restante es 80")
else:
    print ("el combustible es insuficiente")
if destino == "marte":
    print ("el combustible necesario es 35")
    print ("el viaje se realizo correctamente sobro 65")
else:
    print ("el combustible es insuficiente")
if destino == "saturno":
    print ("el combustible necesario es 50 ")
    print ("el viaje se realizo correctamente sobro 50")
else:
    print ("el combustible es insuficiente")
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.
