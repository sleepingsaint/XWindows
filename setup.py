from setuptools import setup, find_packages

VERSION = '0.0.7' 
DESCRIPTION = 'X Server client to access windows and automate keypresses'

with open('README.md') as f:
    long_description = f.read()

# Setting up
setup(
        name="XWindows", 
        version=VERSION,
        author="sleepingsaint",
        author_email="suryasantosh14523@gmail.com",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=["python-xlib"], 
        license='MIT License',
        project_urls={
        'GitHub Project': 'https://github.com/sleepingsaint/XWindows',
        'Issue Tracker': 'https://github.com/sleepingsaint/XWindows/issues'
        },

        keywords=['python3', 'XServer', 'Xlib', 'linux'],

        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux",
            'Environment :: X11 Applications',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License'
        ]
)