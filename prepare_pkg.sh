#!/bin/bash

#pdflatex tp_derivation/main.tex
#pdflatex tp_dl/main.tex
#pdflatex tp_integration/main.tex
echo "\n*******************"
echo "Prepare tp_polynome"
echo "*******************\n"

cd tp_polynome
pdflatex main.tex
if [ $? -eq 0 ]
then
    sleep 4
    rm *.log
    rm *.aux
    rm *.tex
    rm exemples/*.tex
    rm exercices/*.tex
    rm -fr correction
    rm comments.txt
fi
cd -

echo "\n*******************"
echo "Prepare tp_stat"
echo "*******************\n"
cd tp_stat
pdflatex main.tex
if [ $? -eq 0 ]
then
    sleep 4
    rm *.log
    rm *.aux 
    rm *.tex
    rm exemples/*.tex
    rm exercices/*.tex
    rm -fr correction
    rm comments.txt
fi
cd -

echo "\n*******************"
echo "Prepare tp_aleatoire"
echo "*******************\n"

cd tp_aleatoire
pdflatex main.tex
if [ $? -eq 0 ]
then
    sleep 4
    rm *.log
    rm *.aux
    rm *.tex
    rm exemples/*.tex
    rm exercices/*.tex
    rm -fr correction
    rm comments.txt
fi
cd -

