# ©  2008-2021 Deltatech
# See README.rst file on addons root folder for license details


from odoo import fields, models


class DeliveryCarrierAddMinAmount(models.Model):
    _inherit = "delivery.carrier"
    
    amount_min = fields.Float()