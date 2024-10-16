# lotka-volterra

Lotkuv Volterruv model s lovem, streamlit aplikace


## Online version

[https://lotka-volterra.streamlit.app/](https://lotka-volterra.streamlit.app/)


## Streamlit

~~~
streamlit run app.py
~~~


## Docker

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