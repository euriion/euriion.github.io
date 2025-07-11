#!/bin/bash

echo "Building Shiny Introduction Presentation..."
echo

# Check if R is installed
if ! command -v R &> /dev/null; then
    echo "Error: R is not installed or not in PATH"
    echo "Please install R from https://cran.r-project.org/"
    exit 1
fi

# Check if required packages are installed
echo "Checking required R packages..."
R --slave --no-restore --no-save -e "if (!require('rmarkdown', quietly = TRUE)) { install.packages('rmarkdown', repos = 'https://cran.rstudio.com/') }"
R --slave --no-restore --no-save -e "if (!require('revealjs', quietly = TRUE)) { install.packages('revealjs', repos = 'https://cran.rstudio.com/') }"
R --slave --no-restore --no-save -e "if (!require('knitr', quietly = TRUE)) { install.packages('knitr', repos = 'https://cran.rstudio.com/') }"

# Build the presentation using R knitr
echo "Rendering presentation with R knitr..."
R --slave --no-restore --no-save -e "Sys.setenv(RSTUDIO_PANDOC='/usr/bin'); rmarkdown::render('shiny-introduction.Rmd', output_format = 'revealjs::revealjs_presentation')"

if [ $? -eq 0 ]; then
    echo
    echo "Build successful!"
    echo "Output file: shiny-introduction.html"
    echo
    
    # Ask if user wants to open the presentation
    read -p "Do you want to open the presentation? (y/n): " choice
    if [[ $choice == "y" || $choice == "Y" ]]; then
        if command -v xdg-open &> /dev/null; then
            xdg-open shiny-introduction.html
        elif command -v open &> /dev/null; then
            open shiny-introduction.html
        else
            echo "Please open shiny-introduction.html manually"
        fi
    fi
else
    echo
    echo "Build failed!"
    echo "Please check the error messages above."
    echo
    echo "Common solutions:"
    echo "1. Make sure R is properly installed"
    echo "2. Check if all required packages are installed"
    echo "3. Verify the .Rmd file syntax"
fi

echo 