try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='wirecurly',
    version='0.1',
    description='A simple XML generation tool to handle FreeSWITCH mod_xml_curl as well as file written XML',
    author='Joao Mesquita',
    author_email='jmesquita@indicium.com.ar',
    url='https://github.com/Wirephone/wirecurly',
    install_requires=[
        "lxml",
        "nose"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
