# `basic_pkg_viky`

The `basic_pkg_viky` is a simple testing example to understand the basics of developing your first Python package.

## Install & Usage

You can install `basic_pkg_viky` as follows:
```
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps basic-pkg-viky
```
```
pip install -i https://test.pypi.org/simple/ basic-pkg-viky==1.0.0
```
Try to have fun with `basic_pkg_viky`:

```
from multipe import mul_viky

mul_viky.mul_by_same_number(5)
```

## Useful Resources

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Demo Tutorial](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/)
* [Configuring setuptools using setup.cfg files](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)