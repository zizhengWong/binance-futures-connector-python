import os
from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__)) # 里面返回的是当前脚本文件所在的目录路径

with open(
    os.path.join(root, "requirements/common.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "binance-futures-connector"
DESCRIPTION = "This is a lightweight library that works as a connector to Binance Futures public API."
AUTHOR = "zwang"
URL = "https://github.com/zizhengWong/binance-futures-connector-python"
VERSION = None

about = {}

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

if not VERSION:
    with open(os.path.join(root, "binance", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    AUTHOR=AUTHOR,
    url=URL,
    keywords=["Binance futures", "Public API"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)), # 指定要包含在发布的软件包中的包列表
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ], # 软件包的一系列分类标签
    python_requires=">=3.7",
)
