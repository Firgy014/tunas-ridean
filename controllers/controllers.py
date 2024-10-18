from odoo import http
from odoo.http import request
import json

class PemesananRuanganAPIController(http.Controller):

    @http.route('/api/pemesanan/status', type='json', auth='public', methods=['POST'], csrf=False)
    def get_status_pemesanan(self, **kwargs):
        
        try:
            data = json.loads(http.request.httprequest.data)
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error reading request data: {str(e)}'
            }
        
        pemesan = data.get('nama_pemesan', None)
        ruangan_id = data.get('ruangan_id', None)
        tanggal_pemesanan = data.get('tanggal_pemesanan', None)

        if not pemesan or not ruangan_id or not tanggal_pemesanan:
            return {
                'status': 'error',
                'message': 'Nama pemesan, ID ruangan, dan tanggal pemesanan harus diberikan.'
            }

        pemesanan = request.env['tunas.pemesanan.ruangan'].sudo().search([
            ('nama_pemesan', '=', pemesan),
            ('ruangan_id', '=', ruangan_id),
            ('tanggal_pemesanan', '=', tanggal_pemesanan)
        ], limit=1)

        if not pemesanan:
            return {
                'status': 'error',
                'message': 'Pemesanan tidak ditemukan.'
            }

        return {
            'status': 'success',
            'data': {
                'nama_pemesan': pemesanan.nama_pemesan,
                'ruangan': pemesanan.ruangan_id.nama,
                'tanggal_pemesanan': pemesanan.tanggal_pemesanan,
                'state': pemesanan.state
            }
        }
