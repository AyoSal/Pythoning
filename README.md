# Pythoning
Set of python scripts to automate addition of ingress-rules to security groups.
1. sg_ingress.py - for creating the ingress rule using a json file with the parameteres - params.json 
2. script creates the rule and generates another json file. both json files updated into an S3 bucket
3. dates.py / revoke.py - for removal of ingress rule from security group in AWS

modules used -
datetime
boto3
json
