from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id=fields.Many2one('stock.transport.dock', string="Dock")
    vehicle_id=fields.Many2one('fleet.vehicle', string="Vehicle")
    category_id = fields.Many2one('fleet.vehicle.model.category')
    weight_capacity=fields.Float(compute='_compute_weight_capacity', store=True)
    volume_capacity=fields.Float(compute='_compute_volume_capacity', store=True)


    @api.depends('category_id.max_weight','picking_ids')
    def _compute_weight_capacity(self):
        for batch in self:
            transfers=batch.picking_ids

            curr_weight=0
            for transfer in transfers:
                for picking in transfer:
                    for product in picking.move_ids:
                        curr_weight=curr_weight+(product.product_id.weight*product.product_qty)
            # print(curr_weight)
            
            if batch.category_id.max_weight:
                batch.weight_capacity=(curr_weight/batch.category_id.max_weight)*100
            else:
                batch.weight_capacity=0

        # for batch in self:
        #     transfers=batch.picking_ids
        #     curr_weight=0
        #     for transfer in transfers:
        #         curr_weight=curr_weight+transfer.weight
        #     if batch.category_id.max_weight:
        #         batch.weight_capacity=curr_weight/batch.category_id.max_weight
        #     else:
        #         batch.weight_capacity=0

           


    
    @api.depends('category_id.max_volume','picking_ids')
    def _compute_volume_capacity(self):
        for batch in self:
            transfers=batch.picking_ids

            curr_volume=0
            for transfer in transfers:
                for picking in transfer:
                    for product in picking.move_ids:
                        curr_volume=curr_volume+(product.product_id.volume*product.product_qty)
            # print(curr_volume)
            
            if batch.category_id.max_volume:
                batch.volume_capacity=(curr_volume/batch.category_id.max_volume)*100
            else:
                batch.volume_capacity=0