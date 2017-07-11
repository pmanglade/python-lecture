#!/bin/bash

#pdflatex tp_derivation/main.tex
#pdflatex tp_dl/main.tex
#pdflatex tp_integration/main.tex
echo "*******************"
echo "Prepare tp_polynome"
echo "*******************"

cd tp_polynome
rm *.log
rm *.pdf
rm *.aux
cd -

echo "*******************"
echo "Prepare tp_stat"
echo "*******************"

cd tp_stat
rm *.log
rm *.pdf
rm *.aux 
cd -

echo "*******************"
echo "Prepare tp_aleatoire"
echo "*******************"

cd tp_aleatoire
rm *.log
rm *.pdf
rm *.aux
cd -

