try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='wirecurly',
    version='0.1',
    description='A simple XML generation tool to handle FreeSWITCH mod_xml_curl',
    author='Joao Mesquita',
    author_email='jmesquita@indicium.com.ar',
    url='',
    install_requires=[
        "lxml",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
