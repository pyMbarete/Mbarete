@ECHO off
cd ..
cd
echo Ejecutando: git pull
echo "git pull", traer datos del repositorio remoto y luego mezclar los cambios con el repositorio local
git pull

:status
echo Ejecutando: git status
git status

echo Si optuvo algun error por favor, ingrese uno de los numeros de las siguientes opciones
echo "  1.No importan los cambios locales y desea sobrescribirlos" \n
echo "  2.Te importan los cambios y te gustaría mantenerlos después de traer los cambios remotos" \n
echo "  3.Deseas descargar los cambios remotos pero aún no aplicarlos" \n
echo "  <<< ENTER PARA SALIR >>>"

SET /p sigue=Ingrese una Opcion: 
if "%sigue%"=="1" (goto :merge)
if "%sigue%"=="2" (goto :stash)
if "%sigue%"=="3" (goto :fetsh)
goto :fin


:merge
echo Ejecutando: git fetch
echo "git fetch", solo traerá datos del repositorio remoto del 'branch' actual 
git fetch
echo Ejecutando: git reset --hard HEAD
echo "git reset --hard HEAD", restablecerá el branch a su último estado "committed"
git reset --hard HEAD
echo Ejecutando: git merge '@{u}'
echo "git merge '@{u}'", para mezclar los cambios con el repositorio local
git merge '@{u}'
goto :status


:stash
echo Ejecutando: git fetch
echo "git fetch", solo traerá datos del repositorio remoto del 'branch' actual 
git fetch
echo Ejecutando: git stash
echo "git stash", significa guardar los cambios "uncommitted" por un momento para traerlos nuevamente más tarde
git stash
echo Ejecutando: git merge '@{u}'
echo "git merge '@{u}'", para mezclar los cambios con el repositorio local
git merge '@{u}'
echo Ejecutando: git stash pop
echo "git stash pop", para recuperar los cambios guardados en el último stash.
echi "git stash pop", este comando también elimina el 'stash commit' hecho con "git stash".
git stash pop
goto :status

:fetch
echo Ejecutando: git fetch --all
echo "git fetch --all", para obtener los cambios de todos los branches.
git fetch --all


SET /p sigue=¿desea limpiar algunas de las ramas que ya NO existen en el repositorio remoto s/n?.
if "%sigue%"=="n" (goto :status)
if "%sigue%"=="N" (goto :status)
:fetch_limpiar
echo Ejecutando: git fetch --prune
echo "git fetch --prune", limpiar algunas de las ramas que ya no existen en el repositorio remoto
git fetch --prune


:fin
pause presione una tecla para salir...

