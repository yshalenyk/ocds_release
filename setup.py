from setuptools import setup


install_requires = []
test_requires = []
entry_points = {}


setup(name='openprocurement.ocds_release',
      version='0.0.1',
      description='openprocurement.ocds_release',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=test_requires,
      entry_points=entry_points)
