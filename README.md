# Ekologické modely


## Online version

[https://ekoly.streamlit.app/](https://lotka-volterra.streamlit.app/)


## Streamlit

~~~
streamlit run app.py
~~~

## Docker composet

Build (pokud je potřeba) a spuštění
~~~
docker compose up
~~~
Nastavení čísla portu, na kterém aplikace poběží, je v souboru `compose.yml`.

## Docker bez compose

Build
~~~
sudo docker build -t streamlit-lv .
~~~

Run on localhost port 80 (http)
~~~
sudo docker run -p 80:80 streamlit-lv
~~~

Enter the container
~~~
sudo docker run -it --entrypoint=/bin/bash streamlit-lv -i
~~~