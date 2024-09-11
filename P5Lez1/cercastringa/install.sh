crea la cartella CercaStringa mkdir $home/CercaStringa
Copia nella cartella i due file
Crea il virtual environment

mkdir $home/CercaStringa
cp cerca.py $home/Cercastringa
cp requirements.txt $home/CercaStringa
cd $home/CercaStringa
pip install virtualenv
source myenv/bin/activate
pip install -r requirements.txt

