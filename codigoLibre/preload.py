proyectos={}
from .aspasDeVientoDeArquimedes import mbarete as aspasDeVientoDeArquimedes
proyectos['aspasDeVientoDeArquimedes']=aspasDeVientoDeArquimedes
from .editorGrafico import mbarete as editorGrafico
proyectos['editorGrafico']=editorGrafico
from .controlMental import mbarete as controlMental
proyectos['controlMental']=controlMental
from .servidor import mbarete as servidor
proyectos['servidor']=servidor
from .PianoArduinoPython import mbarete as PianoArduinoPython
proyectos['PianoArduinoPython']=PianoArduinoPython
from .practicaImagenes import mbarete as practicaImagenes
proyectos['practicaImagenes']=practicaImagenes
from .proyectoLinuxControlMental import mbarete as proyectoLinuxControlMental
proyectos['proyectoLinuxControlMental']=proyectoLinuxControlMental
from .extrusoraUniversalImpresora3D import mbarete as extrusoraUniversalImpresora3D
proyectos['extrusoraUniversalImpresora3D']=extrusoraUniversalImpresora3D
from .cuelloFormador import mbarete as cuelloFormador
proyectos['cuelloFormador']=cuelloFormador
def command(admin,G,manager):
    G.command[manager+'_transicion_aspasDeVientoDeArquimedes']=lambda : admin.transicion(G,'aspasDeVientoDeArquimedes')
    G.command[manager+'_transicion_editorGrafico']=lambda : admin.transicion(G,'editorGrafico')
    G.command[manager+'_transicion_controlMental']=lambda : admin.transicion(G,'controlMental')
    G.command[manager+'_transicion_servidor']=lambda : admin.transicion(G,'servidor')
    G.command[manager+'_transicion_PianoArduinoPython']=lambda : admin.transicion(G,'PianoArduinoPython')
    G.command[manager+'_transicion_practicaImagenes']=lambda : admin.transicion(G,'practicaImagenes')
    G.command[manager+'_transicion_proyectoLinuxControlMental']=lambda : admin.transicion(G,'proyectoLinuxControlMental')
    G.command[manager+'_transicion_extrusoraUniversalImpresora3D']=lambda : admin.transicion(G,'extrusoraUniversalImpresora3D')
    G.command[manager+'_transicion_cuelloFormador']=lambda : admin.transicion(G,'cuelloFormador')
