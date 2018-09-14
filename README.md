# Braze Unsubscribe Secret Lambda

Used by Braze to retrieve the unsubscribe secret token.

Braze does not have a secret key value store. It is only possible to store 
basic auth credentials. This lambda returns the password on the basic auth request. Braze will use
this password as the unsubscribe hmac secret when constructing the unsubscribe token. 


## Deploy

Deploy cfn.yaml to the identity cloudformation stack, braze-unsubscribe-secret-lambda 
The endpoint code is inlined in cfn.yaml
