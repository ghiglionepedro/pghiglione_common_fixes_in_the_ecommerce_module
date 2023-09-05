# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo15/odoo/repositorios/adrian-pet/sellerInProductTemplate(http.Controller):
#     @http.route('//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template.listing', {
#             'root': '//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template',
#             'objects': http.request.env['/opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template./opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template'].search([]),
#         })

#     @http.route('//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template//opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template/objects/<model("/opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template./opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo15/odoo/repositorios/adrian-pet/seller_in_product_template.object', {
#             'object': obj
#         })
