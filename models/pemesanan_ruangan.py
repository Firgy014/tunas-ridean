from odoo import models, fields, api

class TunasPemesananRuangan(models.Model):
    _name = 'tunas.pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True, readonly=True, copy=False, default='New')
    ruangan_id = fields.Many2one('tunas.master.ruangan', string='Ruangan', required=True)
    nama_pemesan = fields.Char(string='Nama Pemesan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done'),
    ], string='Status', default='draft', track_visibility='onchange')
    catatan = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('nama_pemesan_unique', 'unique(nama_pemesan)', 'Nama pemesan sudah ada!'),
        ('ruangan_tanggal_unique', 'unique(ruangan_id, tanggal_pemesanan)', 'Ruangan dan tanggal pemesanan sudah dipakai!')
    ]

    @api.model
    def create(self, vals):
        if vals.get('nomor_pemesanan', 'New') == 'New':
            sequence = self.env['ir.sequence'].next_by_code('pemesanan.ruangan') or '/'
            vals['nomor_pemesanan'] = f"{vals.get('ruangan_id')}/{vals.get('tanggal_pemesanan')}/{sequence}"
        return super(TunasPemesananRuangan, self).create(vals)
    
    def action_proses(self):
        for record in self:
            record.state = 'on_going'
    
    def action_done(self):
        for record in self:
            record.state = 'done'

    def name_get(self):
        result = []
        for record in self:
            nomor_pemesanan = record.nomor_pemesanan
            result.append((record.id, nomor_pemesanan))
        return result
    