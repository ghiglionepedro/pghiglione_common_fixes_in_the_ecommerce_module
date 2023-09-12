# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo.http import request, route

from odoo.addons.website_sale.controllers.main import WebsiteSale as Base


class WebsiteSaleWithMinAmount(Base):
    @route("/shop/carrier_acquirer_check", type="json", auth="public", website=True, sitemap=False)
    def carrier_acquirer_check(self, carrier_id, acquirer_id=None, **kw):
        debajo_minimo = False
        result = {"status": False, "all_acquirer": True}
        carrier = request.env["delivery.carrier"].sudo().browse(int(carrier_id))
        if acquirer_id is None:
            acquirer_id = 0
        if carrier:
            if carrier.amount_min and float(request.website.sale_get_order().amount_total) < carrier.amount_min:
                # El monto total es menor que el mínimo, por lo que no se permiten opciones de pago
                debajo_minimo = True
            else:
                if carrier.acquirer_allowed_ids:
                    result = {
                        "status": False,
                        "acquirer_allowed_ids": carrier.acquirer_allowed_ids.ids,
                        "all_acquirer": False,
                    }
                    if int(acquirer_id) in carrier.acquirer_allowed_ids.ids:
                        result["status"] = True
                else:
                    result = {"status": True, "all_acquirer": True}

        if acquirer_id:

            context = dict(request.context)
            context.setdefault("acquirer_id", acquirer_id)
            request.context = context

            order = request.website.sale_get_order()

            acquirer = request.env["payment.acquirer"].sudo().browse(int(acquirer_id))
            # if acquirer and order.acquirer_id != acquirer:
            #     order.write({"acquirer_id": acquirer.id})

            if acquirer.value_limit and order.amount_total > acquirer.value_limit:
                result["status"] = False
            label_ids = list(set(order.partner_id.category_id.ids) & set(acquirer.restrict_label_ids.ids))
            if label_ids:
                result["status"] = False
        if debajo_minimo:
            result["status"] = False
            
        return result