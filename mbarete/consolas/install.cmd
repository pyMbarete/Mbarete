@ECHO off
SET pwd=%cd%
:: -R --root                         Root installation directory
SET R=C:\cygwin64
SET binCigW=%R%\bin\mintty.exe
SET CigW=servidor\cigwin_setup-x86_64.exe
SET admin=mbarete\config\systemAdmin.py 
SET rutaEnv=env\Scripts\activate.bat
if "%1"=="prueba" ( goto :decorador )
if "%1"=="root" ( goto :decorador )
if "%1"=="instalando" ( goto :decorador )
if "%1"=="requirements" ( goto :decorador )
if "%1"=="nginx" ( goto :decorador )
if "%1"=="virtual" ( goto :decorador )
if "%1"=="cigwin" ( goto :decorador )
python %admin% rootCall -go %USERPROFILE%\mbareteAdmin.cmd -cmd %0 -goto instalando
start mbarete\config\as_root.lnk
goto :fin
:decorador
echo %0 %1
@ECHO on
goto :%1

:root
::Seccion para ejecutar instrucciones en modo Administrador
goto :fin

:instalando
::configuramos los datos iniciales del entorno virtual
if exist "env" ( .\%rutaEnv% mbarete install.cmd cigwin )
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade wheel
python -m pip install --upgrade python3-env
virtualenv env
echo if "%%1"=="mbarete" ( goto :mbarete ) >> %rutaEnv%
echo goto :fin >> %rutaEnv%
echo :mbarete >> %rutaEnv%
echo %%2 %%3 >> %rutaEnv%
echo :fin >> %rutaEnv%
.\%rutaEnv% mbarete install.cmd requirements
goto :f

:nginx
::configuramos los datos iniciales de nuestro servidor NGINX
SET comprimido=nginx-1.20.2.zip
SET descomprimido=nginx-1.20.2
SET renombrar=nginx
SET ubicar=servidor
SET exist_True=goto config_nginx
SET goto_final=config_nginx
goto :descomprimir
:config_nginx
goto :f

:uwsgi
SET comprimido=uwsgi-2.0.20.tar.gz
SET descomprimido=uwsgi-2.0.20
SET renombrar=uwsgi
SET ubicar=servidor
SET exist_True=goto config_uwsgi
SET goto_final=config_uwsgi
goto :descomprimir
:config_uwsgi
%binCigW% -e python servidor//uwsgi//setup.py install
goto :f


:descomprimir
if exist "%ubicar%\%renombrar%" ( %exist_True% )
tar -xf .\%ubicar%\%comprimido%
rename %descomprimido% %renombrar% 
move %renombrar% %ubicar%\
goto :%goto_final%
::python %admin% configBIND -server_name 
::python %admin% regla -file servidor/reglaDNS.cmd -port 53 
::servidor\reglas.cmd
goto :f

:requirements
python -m pip install -r requirements.txt
goto :nginx

:virtual
echo entorno Virtual ya instalado
.\%rutaEnv% mbarete install.cmd prueba
@ECHO off
goto :fin

:cigwin
::Command Line Options:
:: -t --allow-test-packages          Consider package versions marked test
::    --allow-unsupported-windows    Allow old, unsupported Windows versions
:: -a --arch                         Architecture to install (x86_64 or x86)
:: -C --categories                   Specify entire categories to install
:: -o --delete-orphans               Remove orphaned packages
:: -A --disable-buggy-antivirus      Disable known or suspected buggy anti virus software packages during execution.
:: -D --download                     Download packages from internet only
:: -f --force-current                Select the current version for all packages
:: -h --help                         Print help
:: -I --include-source               Automatically install source for every package installed
:: -i --ini-basename                 Use a different basename, e.g. "foo", instead of "setup"
:: -U --keep-untrusted-keys          Use untrusted keys and retain all
:: -L --local-install                Install packages from local directory only
:: -l --local-package-dir            Local package directory
:: -m --mirror-mode                  Skip package availability check when installing from local directory (requires local directory to be clean mirror!)
:: -B --no-admin                     Do not check for and enforce running as Administrator
:: -d --no-desktop                   Disable creation of desktop shortcut
:: -r --no-replaceonreboot           Disable replacing in-use files on next reboot.
:: -n --no-shortcuts                 Disable creation of desktop and start menu shortcuts
:: -N --no-startmenu                 Disable creation of start menu shortcut
:: -X --no-verify                    Don't verify setup.ini signatures
::    --no-version-check             Suppress checking if a newer version of setup is available
::    --enable-old-keys              Enable old cygwin.com keys
:: -O --only-site                    Do not download mirror list.  Only use sites specified with -s.
:: -M --package-manager              Semi-attended chooser-only mode
:: -P --packages                     Specify packages to install
:: -p --proxy                        HTTP/FTP proxy (host:port)
:: -Y --prune-install                Prune the installation to only the requested packages
:: -K --pubkey                       URL or absolute path of extra public key file (RFC4880 format)
:: -q --quiet-mode                   Unattended setup mode
:: -c --remove-categories            Specify categories to uninstall
:: -x --remove-packages              Specify packages to uninstall
:: -R --root                         Root installation directory
:: -S --sexpr-pubkey                 Extra DSA public key in s-expr format
:: -s --site                         Download site URL
:: -u --untrusted-keys               Use untrusted saved extra keys
:: -g --upgrade-also                 Also upgrade installed packages
::    --user-agent                   User agent string for HTTP requests
:: -v --verbose                      Verbose output
:: -V --version                      Show version
:: -W --wait                         When elevating, wait for elevated child process
:: -D --download                     Download packages from internet only
:: -L --local-install                Install packages from local directory only

::if exist "%R%" ( goto :uwsgi )
:: -l --local-package-dir            Local package directory
SET l="%pwd%\cygwin.mirror.constant.com"
:: -C --categories                   Specify entire categories to install
SET C="Devel"
:: -P --packages   
SET P=libintl-devel,python3-devel,python38-devel,gettext-devel,gcc-g++,gcc-core,python37-pip,nginx,gzip,python37-wheel,mercurial,pylint,python-libxslt,python36,python36-devel,python37,python37-devel,python37-setuptools,python38,python38-devel,python38-pip,python38-ply,python38-setuptools,python38-virtualenv,python38-wx,scons,urlgrabber,tailor
:: -s --site                         Download site URL
SET s="http://cygwin.mirror.constant.com"

::Parametros para instalar CigWin solamente
SET SigWinInstall=--only-site --no-version-check --no-shortcuts --no-desktop 
::Parametros para instalar Paquetes dentro de SigWin
SET APT_Param=--no-version-check --verbose --package-manager --no-shortcuts 
::Primero instalamos CIGWIN y la categoria Devel Completa
.\%CigW% %SigWinInstall% --root %R% --categories %C% --site %s%
:: Ahora instalamos los paquetes que necesitamos
SET C="All"
.\%CigW% %APT_Param% --root %R% --packages "%P%" -L --local-package-dir %l%
goto :uwsgi

@ECHO off
goto :f


:prueba
echo test uwsgi
::python python-dev
python -m pip install uwsgi
python uwsgi --http :8000 --wsgi-file servidor\nginx\test.py
pause
@ECHO off
goto :fin

:f
@ECHO off
SET /p sigue=Continuar Session s/n?:
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)
if "%sigue%"=="" (goto :fin)
cmd
:fin