from odoo import models, fields, api


class stockTransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "These are dock vechile"


    name=fields.Char()
    