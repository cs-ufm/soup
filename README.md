# web scrapping 101

In this project we will understand the DOM and interact with it, we will learn and assure HTML and some python best practices like requirements.txt and pip.
# Pre Reqs
Go ahead and read these:

- [HTML](https://www.w3schools.com/html/html_basic.asp)
- We will try to understand the [DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp)



# Python Extras

<details> <summary> pip  </summary>
<p>
pip is the python package manage, from the web:

>  is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library

</p>
</details>


<details> <summary>  requirements.tx  </summary>
<p>
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

</p>
</details>


# Web Scraping with bs4 and requests

#### [**requests:**](https://2.python-requests.org/en/master/)

will be use to make http requests (GET by default) and retrieve a html web page content

#### [**bs4:**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
is a Python library for pulling data out of HTML and XML files


# Your project
For every item here you must display the results in a very understandable way:

```bash
<YOUR NAME GOES HERE>
=============================
1. Portal
# item_title: <result>
GET the title and print it: <result>
---------------------------------------
GET the Complete Address of UFM: <result>
------------------------------------------
.
.
.
find all properties that have href (link to somewhere):
- <result 1>
- <result 2>
- <result 3>
=============================
2. Estudios

```
> ----- : separator between items
>
> ===== : separator between parts
>
> 1. Title: Title of the section


It will be possible to pass an argument to your app to specify which section to run, if no argument provided it will default to "run all parts"

```bash
# default to run all parts
python3 soup.py

# run part 1
python3 soup.py 1

# run part 2
python3 soup.py 2

# run part 3
python3 soup.py 3
```


<br>

- [ ] If for some reason the result exceeds 30 lines you will display `"Output exceeds 30 lines, sending output to: <logfile>"` and send the output to a text file inside logs/ , example format:

```bash
$ python3 soup.py 1
=============================
1. Portal
GET the title and print it: Output exceeds 30 lines, sending output to: logs/1portal_GET_the_title_and_print_it.txt


$ ls logs/1portal_GET_the_title_and_print_it.txt

$ cat logs/1portal_GET_the_title_and_print_it.txt

Date of generation: Mon Sep  9 22:58:30 CST 2019
================================================

Universidad Francisco Marroquín
```


#### 1. Portal
using ["http://ufm.edu/Portal"](http://ufm.edu/Portal)

- [ ] GET the title and print it
- [ ] GET the Complete Address of UFM
- [ ] GET the phone number and info email
- [ ] GET all item that are part of the upper nav menu (id: menu-table)
- [ ] find all properties that have href (link to somewhere)
- [ ] get hrefs of all &lt;img>
- [ ] count all &lt;a>

---
##### 1.1 Extra points

- [ ]  From all (&lt;a>) Create a csv file (`logs/extra_as.csv`) with the following columns: Text, href


**example:**
```html
<ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/english/">UFM Key Projects</a></li>
```

| Text             	| href                         	|
|------------------	|------------------------------	|
| UFM Key Projects 	| https://www.ufm.edu/english/ 	|

<br>


#### 2. Estudios
using ["http://ufm.edu/Estudios"](http://ufm.edu/Estudios)

- [ ] now navigate to  /Estudios (better if you obtain href from the DOM)
- [ ] display all items from "topmenu" (8 in total)
- [ ] display ALL "Estudios" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)
- [ ] display from "leftbar" all &lt;li> items (4 in total)
- [ ] get and display all available social media with its links (href) "class=social pull-right"
- [ ] count all &lt;a> that have


#### 3. CS
using ["https://fce.ufm.edu/carrera/cs/"](https://fce.ufm.edu/carrera/cs/)

- [ ] GET title
- [ ] GET and display the href
- [ ] Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically)
- [ ] GET following &lt;meta>: "title", "description" ("og")
- [ ] count all &lt;a>



# Usage
In order to start your project:
- you **MUST** [fork](https://help.github.com/en/articles/fork-a-repo) this repository into **your own personal repo** in **github**
- you will need to use git and commit every once in a while, every commit must have a meaningful message.
- to start using it:
  ```bash
  # clone
  git clone <your own personal repo URL>
  # install dependencies
  pip install -r requirements
  # run it
  python soup.py
  # or
  ./soup.py
    ```

- [x] everytime you complete an "item" make sure to mark it as done [x]