from setuptools import setup


install_requires = [
    'pyyaml',
    'CouchDb',
    'iso8601',
    'Flask',
    'Flask-CouchDB',
    'voluptuous',
    'iso8601',
    'ocdsmerge',
    'jsonpatch',
    'simplejson'
]

test_requires = []
entry_points = {
    "console_scripts": [
        "export = ocds_release.app:main",
    ]
}


setup(name='ocds_release',
      version='0.0.1',
      description='ocds_release',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      include_package_data=True,
      packages=['ocds_release'],
      zip_safe=False,
      install_requires=install_requires,
      tests_require=test_requires,
      entry_points=entry_points)
