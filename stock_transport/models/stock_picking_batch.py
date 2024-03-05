from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'
    dock_id=fields.Many2one('stock.transport.dock', string="Dock")
    vehicle_id=fields.Many2one('fleet.vehicle', string="Vehicle")
    category_id = fields.Many2one('fleet.vehicle.model.category')
    weight_capacity=fields.Float(compute='_compute_weight_capacity', store=True)
    volume_capacity=fields.Float(compute='_compute_volume_capacity', store=True)
    total_transfers=fields.Integer(compute='_compute_total_transfers', string='Transfers', store=True)
    total_lines=fields.Integer(compute='_compute_total_lines', string="Lines", store=True)


    @api.depends('name','weight_capacity','volume_capacity')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            flag=0
            if record.weight_capacity and record.volume_capacity:
                name = name +" :"+f"{record.weight_capacity}"+" Kg"+", "+f"{record.volume_capacity}"+" m\u00b3"
            elif record.weight_capacity :
                name = name +" :"+f"{record.weight_capacity}"+" Kg"
            elif record.volume_capacity :
                name = name +" :"+f"{record.volume_capacity}"+" m\u00b3"
            record.display_name = name




    @api.depends('category_id.max_weight','picking_ids.move_ids.product_qty','picking_ids.move_ids.product_id.weight')
    def _compute_weight_capacity(self):
        for batch in self:
            transfers=batch.picking_ids

            curr_weight=0
            for transfer in transfers:
                # print("Transfer",transfer)
                    # print("Picking",picking)
                for product in transfer.move_ids:
                    curr_weight=curr_weight+(product.product_id.weight*product.product_qty)
            # print("wt ")
            # print(curr_weight)
            
            if batch.category_id.max_weight:
                batch.weight_capacity=(curr_weight/batch.category_id.max_weight)*100
            else:
                batch.weight_capacity=0
            # print(batch.weight_capacity)
            # print("nx ")

        # for batch in self:
        #     transfers=batch.picking_ids
        #     curr_weight=0
        #     for transfer in transfers:
        #         curr_weight=curr_weight+transfer.weight
        #     if batch.category_id.max_weight:
        #         batch.weight_capacity=curr_weight/batch.category_id.max_weight
        #     else:
        #         batch.weight_capacity=0

           


    
    @api.depends('category_id.max_volume','picking_ids.move_ids.product_qty','picking_ids.move_ids.product_id.volume')
    def _compute_volume_capacity(self):
        for batch in self:
            transfers=batch.picking_ids

            curr_volume=0
            for transfer in transfers:
                for product in transfer.move_ids:
                    curr_volume=curr_volume+(product.product_id.volume*product.product_qty)
            # print("vol ")
            # print(curr_volume)
            
            if batch.category_id.max_volume:
                batch.volume_capacity=(curr_volume/batch.category_id.max_volume)*100
            else:
                batch.volume_capacity=0
            # print(batch.volume_capacity)
            # print("nx ")



    @api.depends('picking_ids')
    def _compute_total_transfers(self):
        for batch in self:
            batch.total_transfers=len(batch.picking_ids)
            # print("transfers")
            # print(batch.total_transfers)  





    @api.depends('move_line_ids')
    def _compute_total_lines(self):
        for batch in self:
            batch.total_lines=len(batch.move_line_ids)
            # print("lines")
            # print(batch.total_lines)  


