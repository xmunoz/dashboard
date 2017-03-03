# dashboard

A very rudimentary dashboard for iCTF.

## Install

1. Install the requirements.
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --editable .
```

2. Set an environment variable

```
export FLASK_APP=dashboard
```

3. Create `login.cfg` and put it in this directory.

4. `flask run`
