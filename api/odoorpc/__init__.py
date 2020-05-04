import odoorpc
from api.config import ODOO_RPC

odoo = odoorpc.ODOO(ODOO_RPC['host'], port=ODOO_RPC['port'])

try:
    odoo.login(ODOO_RPC['database'], ODOO_RPC['login'], ODOO_RPC['password'])
except:
    print("Error en la conexion con el host")
    
"""
if 'agro.farm' in odoo.env:
    Farm = odoo.env['agro.farm']
    farm_ids = Farm.search([])
    for farm in Farm.browse(farm_ids):
        print(farm.name)
        for parcel in farm.parcel_ids:
            print("     ", parcel.name)"""