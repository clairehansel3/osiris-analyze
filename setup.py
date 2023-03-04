import setuptools

setuptools.setup(
    name='osiris-analyze',
    version='0.0.1',
    description='A data analysis tool for the particle-in-cell code OSIRIS.',
    url='https://github.com/clairehansel3/osiris-analyze',
    author='Claire Hansel',
    author_email='clairehansel3@gmail.com',
    license='GPLv3',
    packages=['osiris_analyze'],
    install_requires=['numpy', 'scipy', 'matplotlib'],
    scripts=['bin/osiris-analyze']
)
