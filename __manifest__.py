# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Dynamic Family Pricing',
    'version' : '1.0',
    'summary': 'Dynamic product\'s Family Pricing',
    'sequence': 10,
    'description': '"Tarification Dynamique par Famille de Produits"',
    'category': 'Productivity',
    'website': 'https://www.proosoftcloud.com/',
    'depends' : ['mail',
                 'sale',
    ],
    'data': ['views/inherit_product_view.xml',
             'views/inherit_product_category.xml',
             'views/inherit_res_config_settings_view.xml',
             'views/inherit_sale_order_view.xml',
             'views/menu.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
}