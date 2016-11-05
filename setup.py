from setuptools import setup, find_packages
setup(name='sunshine',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      package_data={
          'static': 'sunshine/static/*',
          'template': 'sunshine/templates/*'}   
      )
