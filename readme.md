docker run -it --rm -v $(pwd):/data joyzoursky/python-chromedriver:3.6 bash

cd data/

pip install -r requirements.txt

behave