from odoo import models, fields, api


class MyModel(models.Model):
    _name = 'portal_test.my_model'
    _description = 'my_model'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()


class ResPartner(models.Model):
    _inherit = 'res.partner'

    b2b = fields.Boolean(default=False)

