#!/usr/bin/python
# -*- coding: utf-8 -*-


from odoo_rpc_client import Client
from timeit import default_timer


host = 'localhost'
username = 'admin'
password = 'ksarels2017'
dbname = 'kalisign'

client = Client(host, dbname, username, password)
products = client['product.product'].search_records([])

start_time = default_timer()
print 'Starting...'

for counter, product in enumerate(products):
    print "processing No.", counter
    product.write({'sticker_sign_file': product.sticker_sign,
                   'vectorize_file_file':product.vectorize_file,
                   # 'rendering_3d_file':product.rendering_3d,
                   'production_file_file':product.production_file,
                   'wir_diag_file':product.wir_diag,
                   'addition_draw1_file':product.addition_draw1,
                   'addition_draw2_file':product.addition_draw2,
                    })
    # if product.rende_filename:
    #     base_name = product.rende_filename.split('.')[-1].upper()
    #     if base_name not in ["JPG", "PNG"]:
    #         pass
    #     else:
    #         pass

print "Done!"
end_time = default_timer()
print "Time used(s): {}".format(end_time-start_time)