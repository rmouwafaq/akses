# -*- coding: utf-8 -*-
# from odoo import http


# class PortalTest(http.Controller):
#     @http.route('/portal_test/portal_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_test/portal_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_test.listing', {
#             'root': '/portal_test/portal_test',
#             'objects': http.request.env['portal_test.portal_test'].search([]),
#         })

#     @http.route('/portal_test/portal_test/objects/<model("portal_test.portal_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_test.object', {
#             'object': obj
#         })
