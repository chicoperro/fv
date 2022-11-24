# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import _datetime
from dateutil.relativedelta import relativedelta

class Contratos(models.Model):
    id_contrat = models.AutoField(primary_key=True)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')
    rut_person = models.CharField(max_length=20)
    phone_contrat = models.IntegerField()
    emision_contrat = models.DateField(default=_datetime.date.today(),blank=True)
    fin_contrat = models.DateField(default=_datetime.date.today() + relativedelta(years = 1), blank = True)
    estado = models.BooleanField(default = False)

    class Meta:
        verbose_name="Contrato"
        verbose_name_plural="Contratos"
        db_table = 'CONTRATOS'

class DetallCompra(models.Model):
    id_detall = models.IntegerField(primary_key=True)
    proces_venta_id_proc_venta = models.ForeignKey('ProcesVenta', models.DO_NOTHING, db_column='proces_venta_id_proc_venta')
    fecha_detall = models.DateField()
    nom_producto = models.CharField(max_length=15)
    cost_producto = models.IntegerField()
    iva_producto = models.IntegerField()
    total_compra = models.IntegerField()

    class Meta:
        verbose_name="Detalle Compra"
        verbose_name_plural="Detalle Compras"
        db_table = 'DETALLE_COMPRA'

class DirecExtran(models.Model):
    vent_extran_id_vent_ex = models.ForeignKey('VentExtran', models.DO_NOTHING, db_column='vent_extran_id_vent_ex')
    id_direc = models.CharField(primary_key=True, max_length=20)
    pais = models.CharField(max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    localidad = models.CharField(max_length=20)

    class Meta:
        verbose_name="Direccion Cli_Extrajero"
        verbose_name_plural="Direccion Cli_Extrajeros"
        db_table = 'DIRECCION_EXTRANJERO'

class DirecLocal(models.Model):
    id_direc = models.CharField(primary_key=True, max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=20)
    comuna = models.CharField(max_length=20)
    vent_local_id_vent_loc = models.ForeignKey('VentLocal', models.DO_NOTHING, db_column='vent_local_id_vent_loc')

    class Meta:
        verbose_name="Direccion Cli_Local"
        verbose_name_plural="Direccion Cli_Locales"
        db_table = 'DIRECCION_LOCAL'

class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)
    fecha = models.DateField()
    descrip = models.CharField(max_length=200)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')
    productos_id_prod = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_id_prod', blank=True, null=True)
    estado_admin = models.BooleanField(default = False)
    estado_productor = models.BooleanField(default = False)

    class Meta:
        verbose_name="Pedido"
        verbose_name_plural="Pedidos"
        db_table = 'PEDIDO'

class ProcesPedido(models.Model):
    id_proc_pedido = models.AutoField(primary_key=True)
    transporte_id_trans = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='transporte_id_trans')
    pedido_id_ped = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido_id_ped')
    estado_proceso = models.BooleanField(default = False)

    class Meta:
        verbose_name="Procesar Pedido"
        verbose_name_plural="Procesar Pedidos"
        db_table = 'PROCESAR_PEDIDO'

class ProcesVenta(models.Model):
    id_proc_venta = models.IntegerField(primary_key=True)
    proces_pedido_id_proc_pedido = models.ForeignKey(ProcesPedido, models.DO_NOTHING, db_column='proces_pedido_id_proc_pedido')

    class Meta:
        verbose_name="Procesar Venta"
        verbose_name_plural="Procesar Ventas"
        db_table = 'PROCESO_VENTA'

class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=20)
    precio_prod = models.IntegerField()
    desc_prod = models.CharField(max_length=200)
    imagen = models.ImageField()
    stock_prod = models.IntegerField()
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        db_table = 'PRODUCTOS'

    def __str__(self):
        return self.nom_prod

class ReportMerma(models.Model):
    id_merma = models.IntegerField(primary_key=True)
    fecha_merma = models.DateField()
    descrip_merma = models.CharField(max_length=40)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        verbose_name="Reportar Merma"
        verbose_name_plural="Reportar Mermas"
        db_table = 'REPORTE_MERMA'

class ReportVenta(models.Model):
    id_report_vent = models.IntegerField(primary_key=True)
    prod_venta = models.CharField(max_length=20)
    cant_venta = models.IntegerField()
    total_venta = models.IntegerField()
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta_id_proc_venta')

    class Meta:
        verbose_name="Reportar Venta"
        verbose_name_plural="Reportar Ventas"
        db_table = 'REPORTE_VENTA'

class Reportes(models.Model):
    id_report = models.IntegerField(primary_key=True)
    fecha_report = models.DateField()
    tip_report = models.CharField(max_length=15)
    user_report = models.CharField(max_length=15)
    descrip_report = models.CharField(max_length=30)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        verbose_name="Reporte"
        verbose_name_plural="Reportes"
        db_table = 'REPORTES'

class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    estados = (('preparando','preparando productos'),('despacho','productos despachados'),
        ('recepcionados','recepcionados por el transportista'),('viaje','en camino'),('completado','seguimiento finalizado'))
    est_seguimiento = models.CharField(max_length=50,choices=estados,default='preparando')
    pedido_id_ped = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido_id_ped')
    proces_pedido_id_proc_pedido = models.ForeignKey(ProcesPedido, models.DO_NOTHING, db_column='proces_pedido_id_proc_pedido')

    class Meta:
        verbose_name="Seguimiento"
        verbose_name_plural="Seguimiento"
        db_table = 'SEGUIMIENTO'

class Transporte(models.Model):
    id_trans = models.AutoField(primary_key=True)
    tip_transporte = models.CharField(max_length=15)
    tamano_trans = models.IntegerField()
    capacidad_trans = models.IntegerField()
    refrigeracion_trans = models.CharField(max_length=10)
    fecha_trans = models.DateField()
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        verbose_name="Transporte"
        verbose_name_plural="Transportes"
        db_table = 'TRANSPORTE'

class UsuariosUsuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    tipo_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_usuarios'

class VentExtran(models.Model):
    id_vent_ex = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta_id_proc_venta')
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        verbose_name="Venta Extranjera"
        verbose_name_plural="Ventas Extranjeras"
        db_table = 'VENTA_EXTRANJERO'


class VentLocal(models.Model):
    id_vent_loc = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_proc_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta_id_proc_venta')
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        verbose_name="Venta Local"
        verbose_name_plural="Ventas Locales"
        db_table = 'VENTA_LOCAL'
        
