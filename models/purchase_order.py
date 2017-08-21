# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class PurchaseOrder(models.Model):
    
    _inherit = 'purchase.order'

    internal_notes = fields.Text('Internal Notes')
