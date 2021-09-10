proyectos={}
from .aspasDeVientoDeArquimedes import mbarete as aspasDeVientoDeArquimedes
proyectos['aspasDeVientoDeArquimedes']=aspasDeVientoDeArquimedes
from .cuelloFormador import mbarete as cuelloFormador
proyectos['cuelloFormador']=cuelloFormador
from .editorGrafico import mbarete as editorGrafico
proyectos['editorGrafico']=editorGrafico
from .extrusoraUniversalImpresora3D import mbarete as extrusoraUniversalImpresora3D
proyectos['extrusoraUniversalImpresora3D']=extrusoraUniversalImpresora3D
from .myNegocio import mbarete as myNegocio
proyectos['myNegocio']=myNegocio
from .PianoArduinoPython import mbarete as PianoArduinoPython
proyectos['PianoArduinoPython']=PianoArduinoPython
from .practicaImagenes import mbarete as practicaImagenes
proyectos['practicaImagenes']=practicaImagenes
from .servidor import mbarete as servidor
proyectos['servidor']=servidor
def command(admin,G,manager):
    G.command[manager+'_transicion_aspasDeVientoDeArquimedes']=lambda : admin.transicion(G,'aspasDeVientoDeArquimedes')
    G.command[manager+'_transicion_cuelloFormador']=lambda : admin.transicion(G,'cuelloFormador')
    G.command[manager+'_transicion_editorGrafico']=lambda : admin.transicion(G,'editorGrafico')
    G.command[manager+'_transicion_extrusoraUniversalImpresora3D']=lambda : admin.transicion(G,'extrusoraUniversalImpresora3D')
    G.command[manager+'_transicion_myNegocio']=lambda : admin.transicion(G,'myNegocio')
    G.command[manager+'_transicion_PianoArduinoPython']=lambda : admin.transicion(G,'PianoArduinoPython')
    G.command[manager+'_transicion_practicaImagenes']=lambda : admin.transicion(G,'practicaImagenes')
    G.command[manager+'_transicion_servidor']=lambda : admin.transicion(G,'servidor')
