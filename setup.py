# install local package in my virtual env
from setuptools import find_packages, setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Jack Chen',
    author_email='chenhongzhi90@gmail.com',
    install_requires=["openai", "langchain",
                      "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
