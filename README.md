# Módulo de gestión de viviendas


El objetivo de este módulo es gestionar la venta y el alquiler de viviendas a distintos clientes.

Consta de cuatro modelos: casas, pisos, clientes y categorías.

## Modelo categeorias.

En este modelo se utiliza para añadir distintas categorías a las que pueden pertenecer cada una de las viviendas almacenadas. Lo que se pretende no es definir tipos genéricos como casas, pisos... Que es lo que ya reflejan las clases; sino crear agrupaciones personalizadas como podría ser: vivienda familiar, estudio personal...


## Modelo casas.

En este modelo se pretende gestionar cada una de las casas que pueden ser alquiladas o vendidas, es decir, las que se encuentran disponibles, gestionar su cambio de estado y almacenar sus datos. Cada casa añadida puede tener distintos campos:

- _name: identifica al identificador global interno del modelo.
- _descricion: es un nombre más descriptivo del modelo.
- cod: es la clave primaria de cada casa, aquel código único para ella por el que se define de las demás. Este campo es obligatorio.
- address: este campo se utiliza para indicar la dirección de la casa. Este campo es obligatorio.
- date_rent: fecha en la que comienza el alquiler o en la que se vende el inmueble.
- numMeses: número total de meses por los que va estar alquilada.
- category_id: identificador de la categoría.
- pricePMonth: indica el precio del alquiler o de la venta por mes.
- totalPrice: aquí nos encontramos con un campo calculado que se corresponde con el precio total 
que va a costar el alquiler o venta. Este campo se calcula en el método _total, que realizando la multiplicación entre el número de meses y el precio por cada uno de ellos obtiene el precio total.
- state: en esta lista de selección se almacenan los distintos estados por los que puede pasar una casa, alquilada --> si se encuentra alquilada a un cliente, vendida --> si la vivienda se vende o disponible --> quiere decir que la casa se puede alquilar o comprar ya que no se encuentra en ninguno de esos estados.
A continuación en este modelo se definen las restricciones y validaciones en el cambio de estado de la vivienda, es decir, se definen los cambios posibles; en este caso una casa que está disponible puede alquilarse o venderse en cualquier momento, si la casa está alquilada puede terminar el período de alquiler por lo que pasará a estar disponible otra vez, o puede venderse. En el caso de que la casa se encuentre vendida, no podrá volver a estar disponible ni se podrá alquilar.
Para constar de los cambios de estado se declaran unas funciones de mismo nombre que el estado para establecerlo.
Por último consta de dos restricciones:
- la primera de ellas comprueba que al guardar una casa en la base de datos no exista otra con la misma clave primaria, que sea única, es decir, que no puede crearse dos casas que tengan el mismo código.
- la segunda es una restricción en la fecha. Comprueba que la fecha introducida para el comienzo del alquiler o de la venta no sea anterior a la fecha del día en el que se realiza el registro.

Este modelo cuenta con las vistas tree y form.


## Modelo pisos.
Es similar al modelo de casas, este almacena cada uno de los pisos que pueden ser alquilados o vendidos, es decir, los que se encuentran disponibles, gestionar su cambio de estado y almacenar sus datos. Cada piso añadido puede tener distintos campos:
- en primer lugar tienen los mismos campos que casas:
- _name: identifica al identificador global interno del modelo.
- _descricion: es un nombre más descriptivo del modelo.
- cod: es la clave primaria de cada casa, aquel código único para ella por el que se define de las demás. Este campo es obligatorio.
- address: este campo se utiliza para indicar la dirección de la casa. Este campo es obligatorio.
- date_rent: fecha en la que comienza el alquiler o en la que se vende el inmueble.
- numMeses: número total de meses por los que va estar alquilada.
- category_id: identificador de la categoría.
- pricePMonth: indica el precio del alquiler o de la venta por mes.
- totalPrice: aquí nos encontramos con un campo calculado que se corresponde con el precio total 
que va a costar el alquiler o venta. Este campo se calcula en el método _total, que realizando la multiplicación entre el número de meses y el precio por cada uno de ellos obtiene el precio total.
- state: en esta lista de selección se almacenan los distintos estados por los que puede pasar una casa, alquilada --> si se encuentra alquilada a un cliente, vendida --> si la vivienda se vende o disponible --> quiere decir que la casa se puede alquilar o comprar ya que no se encuentra en ninguno de esos estados.
- A diferencia de casas cuenta con dos boolean, parking y garaje en el que se le puede indicar si cuentan con estas características.

Este modelo cuenta con las vistas tree y form.

## Modelo Cliente
En este modelo se definen los datos de cada uno de los clientes, pueden ser definidos antes de alquilar o comprar una vivienda pero que tengán preintención de ello, sino sería irrelevante guardarlos. Cada Cliente puede tener diferentes campos:
- _name: identifica al identificador global interno del modelo.
- _descricion: es un nombre más descriptivo del modelo.
- casas: es un campo relacional que relaciona cada cliente con el número de casas que posee.
- dni: es el campo por el que se identifica a cada cliente ya que es único. Es obligatorio.
- name: define el nombre y apellidos. Es obligatorio.
- address: aquí se almacena la dirección de cada cliente.
- tlf: para guardar el teléfono de cada cliente.
- pisos: es un campo relacional que relaciona cada cliente con los pisos que tiene en posesión.

Este modelo tiene una restricción sql que comprueba que no existan clientes con el mismo dni.

Este modelo cuenta con las vistas tree y form.



**Este módulo está creado para la versión 12 de Odoo.**

**El enlace: https://github.com/a17saralb/trabajo**



