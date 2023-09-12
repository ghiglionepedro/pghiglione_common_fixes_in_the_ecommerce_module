# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "Delivery and Payment",
    "category": "Website",
    "summary": "eCommerce Delivery and Payment constrains",
    "version": "15.0.2.1.0",
    "author": "Terrabit, Dorin Hongu",
    "license": "OPL-1",
    "website": "https://www.terrabit.ro",
    "depends": ["website_sale", "website_sale_delivery", "deltatech_website_delivery_and_payment"],
    "data": [
        "views/delivery_view.xml",
    ],
    "installable": True,
    "development_status": "Mature",
    "maintainers": ["dhongu"],
    "assets": {
        "web.assets_frontend": ["deltatech_website_delivery_and_payment/static/src/js/website_sale_delivery.js"],
    },
}
