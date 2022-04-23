# ei_instabot

python -m virtualenv ei_virtual_env
source ei_virtual_env/bin/activate
pip install instapy
python -m pip install "kivy[base]"

Make sure you have a geckodriver installed if not installed than run the below command or you can skip it
sudo apt-get install firefox 
sudo apt install firefox-geckodriver

After all the above commands are successfull you can run the below command to run it 
python3 main.py (if you use python version 3 or you can run 
python main.py
