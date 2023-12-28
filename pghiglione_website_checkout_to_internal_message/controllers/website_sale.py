from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleCheckout(WebsiteSale):
    @http.route(["/shop/confirmation"], type="http", auth="public", website=True, sitemap=False)
    def shop_payment_confirmation(self, **post):
        sale_order_id = request.session.get("sale_last_order_id")
        if sale_order_id:
            order = request.env["sale.order"].sudo().browse(sale_order_id)
            order.action_confirm()
            # Se busca el canal para envíar por mensajería interna
            channel = request.env['mail.channel'].sudo().search([('name', '=', 'eCommerce')], limit=1)
            if not channel:
                channel = request.env['mail.channel'].sudo().create({'name': 'eCommerce'})
            # Crea el mensaje interno
            message = _("Se ha realizado una nueva orden de venta con referencia: %s") % (order.name)
            # Envía el mensaje al canal de chat
            channel.sudo().message_post(body=message, author_id=request.env.user.partner_id.id, message_type='comment', subtype='mail.mt_comment')
        return super(WebsiteSaleCheckout, self).shop_payment_confirmation(**post)