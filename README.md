# Módulo de gestión de viviendas


El objetivo de este módulo es gestionar la venta y el alquiler de viviendas a distintos clientes.

Consta de cuatro modelos: casas, pisos, clientes y categorías.

## Modelo categeorias.

En este modelo se utiliza para añadir distintas categorías a las que pueden pertenecer los 


Los cursos se pueden ver listados(con la vista tree) o agrupados por nivel(con la vista kanban)

---El modelo courses.student que maneja la gestión de los alumnos se utiliza de una forma un poco 
---diferente a los cursos, puesto que tiene herencia por delegación del modelo "res.partner". Los 
---datos que podemos manejar son los siguientes:

---partner_id: Cuando queremos crear un estudiante nos muestra una lista con los nombres que ya 
---están declarados en el modelo padre.


Para este modelo únicamente tenemos las vistas tree y form.



Para que la fecha en la que termina la impartición no sea anterior a la de comienzo, pues no tendría sentido.

Para que un estudiante únicamente pueda estar asignado a un solo curso que se esté impartiendo en ese momento. Si el curso al que estaba asignado ya ha terminado, podrá ser asignado a otro distinto.

Para este modelo además de las vistas tree y form tenemos la vista calendar.

Para cada modelo hay un elemento en el menú superior del módulo, mediante los cuales podremos acceder a sus vistas para gestionar cada uno de ellos. Podremos crear cursos y alumnos independientemente, o hacerlo a la vez que creamos también una impartición.

Este módulo está creado para la versión 12 de Odoo.


class FruteriaSocio(models.Model):
    _name = 'fruteria.socio'
    _description = 'Socio fruteria'
    _inherits = {'res.partner': 'partner_id'}

    imagen_socio = fields.Binary('Imagen', related='partner_id.image')
    id_socio = fields.Integer('Id_Socio',require=True)
    partner_id = fields.Many2one('res.partner',ondelete='cascade',require=True)
    ids_peticion = fields.One2many('fruteria.peticion',inverse_name='id_socio')
