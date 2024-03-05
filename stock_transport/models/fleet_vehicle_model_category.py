from odoo import models, fields, api

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string ='Max Weight (Kg)')
    max_volume = fields.Float(string ='Max Volume (m\u00b3)')


    @api.depends('name')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            flag=0
            if record.max_weight and record.max_volume:
                name = name +" ("+f"{record.max_weight}"+" Kg"+", "+f"{record.max_volume}"+" m\u00b3)"
            elif record.max_weight :
                name = name +" ("+f"{record.max_weight}"+" Kg)"
            elif record.max_volume :
                name = name +" ("+f"{record.max_volume}"+" m\u00b3)"
            record.display_name = name

