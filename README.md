# gDash ( g- ) Open Source Intelligence Dashboard

![alt text](https://i.ibb.co/9ckGBZp/2021-04-13-05-09.png)

Open Source Intelligence Dashboard for watching current event's unfold. Leveraging osint, python, and web framework's for user's to spectate the macro world.

## Getting Started

### Running the app locally
I suggest creating a separate virtual environment running Python 3 for this app, and install all of the required dependencies there. Run in Terminal/Command Prompt:
```
git clone https://github.com/antonio-hickey/gDash/
cd gDash
python3 -m venv env
```
In UNIX system:

```
source env/bin/activate
```
In Windows:

```
env\Scripts\activate
```

To install all of the required packages to this environment, simply run:

```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the app will be able to run.

To run the app:
```
flask run
```
which will output:

```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Go to the link `http://127.0.0.1:5000/`
