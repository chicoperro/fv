from django.urls import re_path as url, include
from apps.sistema.views import index,listar_usuarios,User_edit,registrarproductos,listar_productos,Contrato,VerContrato,registrartransportes
from apps.sistema.views import solicitarpedido,listar_pedidos,AdministrarPedido,OfertaProducto,lista_ofrecer,lista_procesopedidos,ResponderOfertas
from apps.sistema.views import lista_sin_transporte,OfertarTransporte,lista_en_proceso,ResponderTransportes,Eliminar_ofert_transport,SolicitarSeguimientos
from apps.sistema.views import lista_en_seguimiento,seguimiento_admin,AdministrarSeguimientos, listaContratos
from django.urls import include, path

app_name = "sistema";

urlpatterns = [
    url(r'^$', index,name='index'), #Administrador, #Productor, #Interno, #Externo, #Consultor, #Transportista
    url(r'^usuarios/', listar_usuarios,name='usuarios'), #Administrador
    url(r'^editar/(?P<id_user>\d*)$', User_edit, name='editar_usuario'),
    url(r'^registrarprod/', registrarproductos,name='regprod'), #Productor
    url(r'^listaprod/', listar_productos, name='listaprod'), #Administrador, #Interno, #Externo
    url(r'^mi-contrato/',VerContrato,name='mi-contrato'), #Productor, #Interno, #Externo, #Consultor, #Transportista
    url(r'^contrato/', Contrato, name='regcontr'), #Visible para quien requiera contrato nuevo
    url(r'^registrartrans/', registrartransportes,name='regptrans'), #Transportista
    url(r'^solicitar-pedido/', solicitarpedido,name='solped'), #Externo
    url(r'^listapedid/', listar_pedidos, name='listaped'), #Administrador
    url(r'^administrar-pedido/(?P<id_ped>\d*)$', AdministrarPedido, name='administrarpedido'),
    #[a-z_][a-z0-9_]*$.
    url(r'^lista-sin-ofertas/', lista_ofrecer, name='listasinofertas'), #Productor
    url(r'^oferta-transporte/(?P<id_ped>\d*)$', OfertaProducto, name='ofertatransporte'),
    url(r'^mis-pedidos/', lista_procesopedidos, name='mispedidos'), #Externo
    url(r'^responder-oferta/(?P<id_ped>\d*)$', ResponderOfertas, name='responderoferta'),
    url(r'^listar-ofertas/', lista_sin_transporte, name='listaparaofertar'), #Transportista
    url(r'^ofrecer-transporte/(?P<id_ped>\d*)$', OfertarTransporte, name='ofrecertrans'),
    url(r'^listar-proceso/', lista_en_proceso, name='listaproceso'), #Externo
    url(r'^responder-transport/(?P<id_proc_pedido>\d*)$', ResponderTransportes, name='respondertransport'),
    url(r'^eliminar-oferta/(?P<id_proc_pedido>\d*)$', Eliminar_ofert_transport, name='eliminaroferta'),
    url(r'^solicitar-seg/(?P<id_proc_pedido>\d*)$', SolicitarSeguimientos, name='solicitarseg'),
    url(r'^mis-seguimientos/', lista_en_seguimiento, name='misseguimientos'), #Externo
    url(r'^lista-seguimiento/', seguimiento_admin, name='listaseguimientos'), #Administrador
    url(r'^administrar-seguimiento/(?P<id_seguimiento>\d*)$', AdministrarSeguimientos, name='administrarseguimiento'),
    url(r'^lista-contratos/', listaContratos, name='listcontratos'),

]   


