# -*- coding: utf-8 -*-
# from odoo import http


# class ModeloCompras(http.Controller):
#     @http.route('/modelo_compras/modelo_compras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modelo_compras/modelo_compras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modelo_compras.listing', {
#             'root': '/modelo_compras/modelo_compras',
#             'objects': http.request.env['modelo_compras.modelo_compras'].search([]),
#         })

#     @http.route('/modelo_compras/modelo_compras/objects/<model("modelo_compras.modelo_compras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modelo_compras.object', {
#             'object': obj
#         })
