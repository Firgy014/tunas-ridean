from odoo import models, fields, api

class TunasMasterRuangan(models.Model):
    _name = 'tunas.master.ruangan'
    _description = 'Master Ruangan'

    nama = fields.Char(string='Nama Ruangan', required=True)
    tipe = fields.Selection([
        ('meeting_kecil', 'Meeting Room Kecil'),
        ('meeting_besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto = fields.Binary(string='Foto Ruangan', required=True)
    kapasitas = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')

    _sql_constraints = [
        ('nama_unique', 'unique(nama)', 'Nama ruangan sudah ada!')
    ]

    def name_get(self):
        result = []
        for record in self:
            nama = record.nama
            result.append((record.id, nama))
        return result