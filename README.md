# Braze Unsubscribe Secret Lambda

Used by Braze to retrieve the unsubscribe secret token.

There is a limitation in Braze where there is no secret key value store. It is only possible to store 
basic auth credentials to endpoints. This lambda returns the password on the basic auth. Braze will use
this password as the unsubscribe hmac secret on a connected content call. 

## Install and run

```
cd ${projectDir}
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt 
python-lambda-local -l venv/lib -f lambda_handler -t 5 app.py test_payload.json
``` 

