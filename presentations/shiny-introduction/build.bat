@echo off
echo Building Shiny Introduction Presentation...
echo.

REM Check if R is installed
R --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: R is not installed or not in PATH
    echo Please install R from https://cran.r-project.org/
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking required R packages...
R --slave --no-restore --no-save -e "if (!require('rmarkdown', quietly = TRUE)) { install.packages('rmarkdown', repos = 'https://cran.rstudio.com/') }"
R --slave --no-restore --no-save -e "if (!require('revealjs', quietly = TRUE)) { install.packages('revealjs', repos = 'https://cran.rstudio.com/') }"
R --slave --no-restore --no-save -e "if (!require('knitr', quietly = TRUE)) { install.packages('knitr', repos = 'https://cran.rstudio.com/') }"

REM Build the presentation using R knitr
echo Rendering presentation with R knitr...
R --slave --no-restore --no-save -e "Sys.setenv(RSTUDIO_PANDOC='C:/Program Files/RStudio/bin/pandoc'); rmarkdown::render('shiny-introduction.Rmd', output_format = 'revealjs::revealjs_presentation')"

if %errorlevel% equ 0 (
    echo.
    echo Build successful!
    echo Output file: shiny-introduction.html
    echo.
    
    REM Ask if user wants to open the presentation
    set /p choice="Do you want to open the presentation? (y/n): "
    if /i "%choice%"=="y" (
        start shiny-introduction.html
    )
) else (
    echo.
    echo Build failed!
    echo Please check the error messages above.
    echo.
    echo Common solutions:
    echo 1. Make sure R is properly installed
    echo 2. Check if all required packages are installed
    echo 3. Verify the .Rmd file syntax
)

echo.
pause 