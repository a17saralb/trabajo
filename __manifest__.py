# -*- coding: utf-8 -*-
{
    'name': "Alquiler de casas",  # Module title
    'summary': "Gestión de alquiler de casas",  # Module subtitle phrase
    'description': """Aplicación de gestión de alquiler de una o varias casas a un cliente""",  # You can also rst format
    'author': "Sara M. Lago Bouzas",
    'website': "http://www.fotocasa.com",
    'category': 'Servicios',
    'version': '2.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/casas.xml',
        'views/categorias.xml',
        'views/clientes.xml',
        'views/pisos.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
