# dashboard

A very rudimentary dashboard for iCTF.

## Install

Install the requirements.
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --editable .
```

Set an environment variable

```
export FLASK_APP=dashboard
```

Create `login.cfg` and put it in this directory.

`flask run` and go to the browser.
