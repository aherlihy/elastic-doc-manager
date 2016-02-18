from setuptools import setup
import sys

setup(name='elasticsearch-docmanager',
      version='1.0.0',
      maintainer='mongodb',
      description='Elastic plugin for mongo-connector',
      platforms=['any'],
      author='10gen labs',
      author_email='mongodb-user@googlegroups.com',
      url='https://github.com/10gen-labs/',
      package_dir = {'mongo_connector.doc_managers.elasticsearch_docmanager': 'mongo_connector/doc_managers'},
      packages=["mongo_connector.doc_managers.elasticsearch_docmanager"],
      install_requires=['mongo-connector >= 2.2.0'],
      license='OSI Approved :: Apache Software License',
      keywords='mongo-connector',
      entry_points={
          'console_scripts': [
              'mongo-connector = mongo_connector.connector:main',
              ],
          }
)
