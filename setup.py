'''
Behavioural_cloning package definition
'''

from setuptools import setup

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='behavioural_cloning',
    version='0.1',
    author='Nick Truesdale',
    author_email='truesdalen@gmail.com',
    description='Behavioural cloning server',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/NickTruesdale/behavioural-cloning',
    packages=[
        'behavioral_cloning'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'python-dotenv',
        'uvicorn',
        'eventlet',
        'flask-socketio',
        'fastapi',
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn',
        'scikit-image',
        'matplotlib',
        'h5py',
        'moviepy',
        'tensorflow',
        'keras',
    ]
)
