#! /bin/bash 
cd ~/Desktop
curl https://rondnelson99.github.io/website/tictacnumero.py > tictacnumero.py
let loop=1
echo "How many sheets would you like?"
read sheets
echo "OK! $sheets sheets coming right up!"
while [ $loop -le $sheets ]
do
	python tictacnumero.py > tictac$loop.txt
	let loop=loop+1
done
rm tictacnumero.py
echo "All done! They're on your desktop with names like tictac1.txt."
echo "You can close this window now."