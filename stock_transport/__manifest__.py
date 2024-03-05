{
    'name': "stock_transport",
    'depends': [
        'base',
        'fleet',
        'stock_picking_batch'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/inherited_stock_picking_batch_views.xml',
        'views/inherited_view_picking_form_views.xml',
        'views/inventory_batch_transfers_graph_view.xml',
        'views/inherited_fleet_vehicle_model_category_views.xml',
    ],
     
    'installable': True,
    'autoinstall':False,
    'application': True,
}