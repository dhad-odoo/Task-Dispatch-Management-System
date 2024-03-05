from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking'

    volume=fields.Float(compute='_compute_total_volume', store=True)


    @api.depends('move_ids.product_id.volume', 'move_ids.product_qty')
    def _compute_total_volume(self):
        for picking in self:
        #     total_volume = sum(
        #         move.product_id.volume * move.product_qty
        #         for move in picking.move_ids
        #         if move.product_id and move.product_id.volume
        #     )
        #     picking.volume = total_volume

            total_volume = 0
            for move in picking.move_ids:
                if move.product_id and move.product_id.volume:
                    total_volume += move.product_id.volume * move.product_qty
            picking.volume = total_volume
            
