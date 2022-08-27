from setuptools import find_packages, setup
from io import open
from os import path

readme = open('README.rst', encoding='utf-8').read()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name='django-quiz-app',
    version='0.0.12',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A configurable quiz app for Django.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jackkweyunga/django_quiz',
    author='Tom Walker',
    author_email='jackkweyunga@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django',
        'Pillow',
        'django-model-utils',
        'six'
    ],
    test_suite='runtests.runtests'
)
