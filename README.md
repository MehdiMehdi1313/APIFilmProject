# APIFilmProject

To launch in terminal

```bash 
pip install -r requirements.txt
export FLASK_ENV=development   
export FLASK_APP=application.py
flask run
```

Once the command executed, the terminal launch the local address and its port associated : 

![My Image](./images/imageAddressLocal.png)

We can now click on this address or use it in our browser.

Once we did it, our web application will display.
It can take a few secondes because several API requests are sent during the loading of the page.

![My Image](./images/HomePage.png)

On this page, we can 2 of our features. The first one display actors that are born today and the second one show us the popular movie of the moment.

We can now click on an actor (for example Tom Hardy) and this page will appear 

![My Image](./images/TomHardy.png)

Here, we can see our 2 last features. In fact, the third one diplay the wards of the actor and the last one display a picture of the actor.


