
IF "%1" == "" ( goto:VACIO ) ELSE ( goto:%1 ) 

:replace
echo parametros pasados: "%*"
set STR=%~2
set "STR_TMP="
set INDEX=1
set /A mod_antiloop=5
set /A mod_count=0
set mod_t=%~2
:EQUAL_CHAR_REPLACE_LOOP
if %mod_count% == %mod_antiloop% ( echo antiloop&goto:EOF )
set /A mod_count=%mod_count%+1
set "STR_TMP2="
for /F "tokens=%INDEX% delims== eol=" %%i in ("%STR%") do set STR_TMP2=%%i
if "%STR_TMP2%" == "" goto EQUAL_CHAR_REPLACE_LOOP_END
set "STR_TMP=%STR_TMP%%STR_TMP2%?03"
set /A INDEX+=1
goto EQUAL_CHAR_REPLACE_LOOP
:EQUAL_CHAR_REPLACE_LOOP_END
echo %STR_TMP%
goto:fin



:VACIO
echo Debes pasar parametros para poder ejecutar 
goto:fin


:fin
@echo on