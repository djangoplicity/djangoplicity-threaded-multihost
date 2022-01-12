import ez_setup
from setuptools import setup, find_packages

version = __import__('threaded_multihost').__version__
ez_setup.use_setuptools()
setup(
    name='django-threaded-multihost',
    version=version,
    description="Djangoplicity Threaded Multihost",
    long_description=open('README.rst').read(),
    author='Bruce Kroeze',
    author_email='brucek@solidsitesolutions.com',
    url='https://github.com/djangoplicity/djangoplicity-threaded-multihost',
    download_url='https://github.com/djangoplicity/djangoplicity-threaded-multihost/archive/refs/tags/1.4.2.tar.gz',
    license='New BSD License',
    platforms=['any'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Framework :: Django'],
    packages=['threaded_multihost'],
    # package_dir = {'':'threaded_multihost'},
    include_package_data=False,
)
