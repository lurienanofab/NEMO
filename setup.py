from setuptools import setup, find_packages

setup(
	name='NEMO',
	version='1.0.0',
	python_requires='>=3.6',
	packages=find_packages(exclude=['NEMO.tests']),
	include_package_data=True,
	url='https://github.com/usnistgov/NEMO',
	license='Public domain',
	author='Dylan Klomparens',
	author_email='dylan.klomparens@nist.gov',
	description='NEMO is a laboratory logistics web application. Use it to schedule reservations, control tool access, track maintenance issues, and more.',
	long_description='Find out more about NEMO on the GitHub project page https://github.com/usnistgov/NEMO',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'License :: Public Domain',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.6',
	],
	install_requires=[
		'cryptography',
		'Django==1.11.9',
		'django-filter',
		'djangorestframework',
		'ldap3',
		'python-dateutil',
		'requests',
		'Pillow',
	],
	entry_points={
		'console_scripts': ['nemo=NEMO.provisioning:entry_point'],
	},
)
