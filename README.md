# aws-snapshot-analyzer
Demo project to manage AWS EC2 instance snapshots

##About
This project is a demo and uses boto3 to manage AWS EC2 instance snapshots.

##Configuring
snapshot uses the configuration file created by aws cli. e.g.

'aws configure --profile snapshot'

##Running

'pipenv run python snapshot/snapshot.py <command> <--project=PROJECT>'

*command* is list, start or stop
*project* is optional