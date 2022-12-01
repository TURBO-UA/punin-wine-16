{
    'name': 'POS extensions',
    'summary': 'POS Receipt - PUNIN WINE',
    'author': 'Oleksandr Komarov',
    'maintainer': 'info@modool.pro',
    'website': 'https://modool.pro',
    'license': 'Other proprietary',
    'category': 'Sales/Point of Sale',
    'version': '16.0.1.0.1',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'report/report_z_report_views.xml',
        'report/report_z_report_templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pw_pos/static/src/xml/ReceiptScreen/OrderReceipt.xml',
        ],
    },
}
