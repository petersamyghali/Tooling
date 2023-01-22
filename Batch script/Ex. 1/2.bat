@ECHO on

SET folder=%1
SET file=%2
SET text=%3

if "%~1" =="" goto label 
if "%~2" =="" goto label 
if "%~3" =="" goto label

IF NOT EXIST %folder% (
MKDIR %folder%
)
cd %folder%

ECHO %text%>%file%
goto end
:label
echo invalid input arguments
:end
exit