from setuptools import setup, find_packages
import os

version = '1.0'

tests_require = [
    'plone.app.testing',
    'plone.namedfile', #namedfile is required with dexterity but not defined
    'unittest2',
    ]

setup(name='collective.hashtags',
      version=version,
      description="Allows to tag objects by hashtags in richtext-fields.",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        ],

      keywords='plone collective hashtags',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/collective.hashtags',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'plone.behavior',
        'plone.app.textfield',
        'plone.dexterity',
        'Plone',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
