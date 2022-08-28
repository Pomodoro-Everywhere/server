from setuptools import setup

__version__ = "undefined"  # if setup fails read it from _version.py and to please PyCharm
with open("README.md", 'r') as f:
    long_description = f.read()
exec(open('pomodoro_everywhere/server/_version.py').read())

setup(
    name='pomodoro_everywhere_server',
    version=__version__,
    description='Server side for application Pomodoro Everywhere',
    license="LGPL2",
    long_description=long_description,
    author='Egor Egorov, Victor Osipov',
    author_email='egigoka@gmail.com;v.osipov08@gmail.com',
    url="https://github.com/Pomodoro-Everywhere/server/",
    packages=['pomodoro_everywhere_server'],  # same as name
    install_requires=[
        'Django==4.1'],
    extras_require={},
    package_data={'api_code': ['api/*']},
    include_package_data=True,
)
