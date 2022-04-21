#!/bin/bash
#Importamos las variables dentro del archivo 'info'

t="$fuente"tmp.sh
echo "#!$SHELL" > $t
while IFS=: read -r var valor;do
    echo $var=$valor 
    echo $var=$valor >> $t
done < "$fuenteinfo"
chmod +x $t
source $t
#rm $t
t=$cross_temporal.sh
declare -A my_array
#importar funciones
source "$fuente"bash_modulo.sh



cross()
{
    IFS=";" read -r -a arr <<< $1
    principal="${arr[0]}"
    confirmar=${arr[1]}
    param="${arr[2]}"
    salida="${arr[3]}"
    obs="${arr[4]}"
    if [ "$confirmar" == " " ];then
        confirmar=true
    fi
    if [ "${arr[2]}" == " " ];then
        my_array=()
    else
        my_array=()
        IFS=":" read -r -a arg <<< "${arr[2]}"
        for elemento in "${arg[@]}";do
            IFS="=" read -r -a clave <<< "${elemento}"
            my_array[${clave[0]}]=${clave[1]}
            #echo my_array[${clave[0]}] = ${clave[1]}
        done
    fi

    super_comand
    #echo "principal : '${principal}'"
    #echo "confimar : '${confirmar}'"
    #echo "argumentos : '${my_array}'"
    #echo "salida : '${salida}'"
}
my_pruebas()
{    
    echo pruebas con while
    segui_loop_1=true
    while [ $segui_loop_1 == true ] ;do
        echo comando de inicio
        echo Si optuvo algun error por favor, ingrese uno de los numeros de las siguientes opciones
        echo "  1.No importan los cambios locales y desea sobrescribirlos" 
        echo "  2.Te importan los cambios y te gustaría mantenerlos después de traer los cambios remotos" 
        echo "  3.Deseas descargar los cambios remotos pero aún no aplicarlos" 
        echo "  <<< ENTER PARA SALIR >>>"
        read -p "Ingrese una Opcion:" mi_var
        if [ -z $mi_var ];then segui_loop_1=false ;fi
        if [ "$mi_var" == "1" ];then
            cross "git fetch;false; ; ;solo traerá datos del repositorio remoto del 'branch' actual"
            cross "git reset --hard HEAD; ; ; ;restablecerá el branch a su último estado committed"
            cross "git merge '@{u}'; ; ; ;para mezclar los cambios con el repositorio local"
        elif [ "$mi_var" == "2" ];then
            cross "git fetch; ; ; ;solo traerá datos del repositorio remoto del 'branch' actual"
            cross "git stash; ; ; ;significa guardar los cambios 'uncommitted' por un momento para traerlos nuevamente más tarde"
            cross "git merge '@{u}'; ; ; ;para mezclar los cambios con el repositorio local"
            cross "git stash pop; ; ; ;para recuperar los cambios guardados en el último stash, este comando también elimina el 'stash commit' hecho con 'git stash'"
        elif [ "$mi_var" == "3" ];then
            cross "git fetch --all; ; ; ;para obtener los cambios de todos los branches."
        fi

    done
}
get_info()
{
    for i in ${!info[@]};do
        echo "$i=${info[$i]}"
    done
}
