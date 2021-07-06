proyectos={}
from .aspasDeVientoDeArquimedes import mbarete as aspasDeVientoDeArquimedes
proyectos['aspasDeVientoDeArquimedes']=aspasDeVientoDeArquimedes
from .cuelloFormador import mbarete as cuelloFormador
proyectos['cuelloFormador']=cuelloFormador
from .extrusoraUniversalImpresora3D import mbarete as extrusoraUniversalImpresora3D
proyectos['extrusoraUniversalImpresora3D']=extrusoraUniversalImpresora3D
from .practicaImagenes import mbarete as practicaImagenes
proyectos['practicaImagenes']=practicaImagenes
def command(admin,G,manager):
    G.command[manager+'_transicion_aspasDeVientoDeArquimedes']=lambda : admin.transicion(G,'aspasDeVientoDeArquimedes')
    G.command[manager+'_transicion_cuelloFormador']=lambda : admin.transicion(G,'cuelloFormador')
    G.command[manager+'_transicion_extrusoraUniversalImpresora3D']=lambda : admin.transicion(G,'extrusoraUniversalImpresora3D')
    G.command[manager+'_transicion_practicaImagenes']=lambda : admin.transicion(G,'practicaImagenes')
