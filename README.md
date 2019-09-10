# web scrapping 101

We will try to understand the DOM

## pip
pip is the python package manage, from the web:

>  is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library

## requirements.tx
“Requirements files” are files containing a list of items to be installed using pip install like so:

```bash
pip install -r requirements.txt
```

Requirements are meant for (but not limited to):

1. Requirements files are used to hold the result from pip freeze for the purpose of achieving repeatable installations
    ```bash
    pip freeze > requirements.txt
    pip install -r requirements.txt
    ```
2. Requirements files are used to force pip to properly resolve dependencies. As it is now, pip doesn’t have true dependency resolution, but instead simply uses the first specification it finds for a project. E.g. if pkg1 requires pkg3>=1.0 and pkg2 requires pkg3>=1.0,<=2.0, and if pkg1 is resolved first, pip will only use pkg3>=1.0, and could easily end up installing a version of pkg3 that conflicts with the needs of pkg2. To solve this problem, you can place pkg3>=1.0,<=2.0 (i.e. the correct specification) into your requirements file directly along with the other top level requirements
```markdown
pkg1
pkg2
pkg3>=1.0,<=2.0
```
3. Requirements files are used to force pip to install an alternate version of a sub-dependency. For example, suppose ProjectA in your requirements file requires ProjectB, but the latest version (v1.3) has a bug, you can force pip to accept earlier versions like so:
```markdown
ProjectA
ProjectB<1.3
```


There are other ways of achieving the same result but will leave those for later.

# Web Scraping with bs4 and requests

**requests:** will be use to make http requests (GET by default) and retrieve a html web page content

**bs4:**