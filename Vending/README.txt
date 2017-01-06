#############################################
# Base de datos para el control del Vending #
#############################################

############
# Maquinas #
############
Tabla para el control de las maquinas, tiene los siguientes campos:
- Numero de Serie, debe ser unico y llave primaria
- Modelo, no puede estar vacio
- Ubicacion (Cotton, Fedex, Comude, Progreso, Toshiba)

#############
# Productos #
#############
Tabla para el control de los productos, tiene los siguientes campos:
- Producto ID, debe ser unico y llave primaria
- Nombre del producto, no puede estar vacio
- Categoria (Fritura, Bebida, Botana, Chocolate, Barras, Dulces, Galletas)
- Descripcion
