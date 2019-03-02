from setuptools import setup

setup(
	name='aws-snapshotanalyzer',
	version='0.1',
	author='Vikas Durgale',
	author_email='vikas@example.com',
	description='AWS SnapshotAnalyzer is a tool to manage AWS EC2 snapshots',
	license='GPLv3+',
	packages=['snapshot'],
	url="https://github.com/VikasDurgale/aws-snapshot-analyzer/",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		snapshot=snapshot.snapshot:cli
	''',
)