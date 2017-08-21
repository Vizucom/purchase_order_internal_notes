# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _


class purchase_order(osv.Model):
    
    _inherit = 'purchase.order'

    _columns = {
        'internal_notes': fields.text('Internal Notes'),
    }
