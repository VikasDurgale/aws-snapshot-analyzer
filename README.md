# aws-snapshot-analyzer
Demo project to manage AWS EC2 instance snapshots

##About
This project is a demo and uses boto3 to manage AWS EC2 instance snapshots.

##Configuring
snapshot uses the configuration file created by aws cli. e.g.

'aws configure --profile snapshot'

##Running

'pipenv run python snapshot/snapshot.py <command> <subcommand> <--project=PROJECT>'

*command* is instances, volumes or snapshots
*subcommand* depends on command
*project* is optional

##Build project
pipenv run python setup.py bdist_wheel

bdist_wheel gives you an archive file which can be used to install project anywhere