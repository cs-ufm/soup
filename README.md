
# web scrapping 101

In this project we will understand the DOM and interact with it, we will learn and assure HTML and some python best practices like requirements.txt and pip.

---

# TOC
- [web scrapping 101](#web-scrapping-101)
- [TOC](#toc)
- [Pre Requisites](#pre-requisites)
- [Python Extras](#python-extras)
- [Web Scraping with bs4 and requests](#web-scraping-with-bs4-and-requests)
  - [**requests:**](#requests)
  - [**bs4:**](#bs4)
- [Your project](#your-project)
  - [1. Portal](#1-portal)
    - [1.1 Extra points](#11-extra-points)
  - [2. Estudios](#2-estudios)
  - [3. CS](#3-cs)
  - [4. Directorio](#4-directorio)
  - [5. Extra](#5-extra)
- [Start your project](#start-your-project)
  - [Usage Dockerfile](#usage-dockerfile)
- [Delivery](#delivery)


---
# Pre Requisites
Go ahead and read these:

- [HTML](https://www.w3schools.com/html/html_basic.asp)
- We will try to understand the [DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp)


---
# Python Extras

<details> <summary> pip  </summary>
<p>
pip is the python package manage, from the web:

>  is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library

</p>
</details>


<details> <summary>  requirements.txt  </summary>
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

---
# Web Scraping with bs4 and requests
We will be using requests to GET the html and bs4 to parse it
<br>
## [**requests:**](https://2.python-requests.org/en/master/)

will be use to make http requests (GET by default) and retrieve a html web page content

## [**bs4:**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
is a Python library for pulling data out of HTML and XML files

---
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

```bash
# ----- : separator between items

# ===== : separator between parts

# 1. Title: Title of the section

# use '-' if its a list
```

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

- [ ] **NOTE** If for some reason the result exceeds 30 lines you will display `"Output exceeds 30 lines, sending output to: <logfile>"` and send the output to a text file inside logs/ , example format:

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

> this log files will not be git tracked.

---

## 1. Portal
using ["http://ufm.edu/Portal"](http://ufm.edu/Portal)

- [ ] GET the title and print it
- [ ] GET the Complete Address of UFM
- [ ] GET the phone number and info email
- [ ] GET all item that are part of the upper nav menu (id: menu-table)
- [ ] find all properties that have href (link to somewhere)
- [ ] GET href of "UFMail" button
- [ ] GET href "MiU" button.
- [ ] get hrefs of all &lt;img>
- [ ] count all &lt;a>


### 1.1 Extra points

- [ ]  From all (&lt;a>) Create a csv file (`logs/extra_as.csv`) with the following columns: Text, href


**example:**
```html
<ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/english/">UFM Key Projects</a></li>
```

| Text             	| href                         	|
|------------------	|------------------------------	|
| UFM Key Projects 	| https://www.ufm.edu/english/ 	|

<br>


## 2. Estudios
using ["http://ufm.edu/Estudios"](http://ufm.edu/Estudios)

- [ ] now navigate to  /Estudios (better if you obtain href from the DOM)
- [ ] display all items from "topmenu" (8 in total)
- [ ] display ALL "Estudios" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)
- [ ] display from "leftbar" all &lt;li> items (4 in total)
- [ ] get and display all available social media with its links (href) "class=social pull-right"
- [ ] count all &lt;a> (just display the count)


## 3. CS
using ["https://fce.ufm.edu/carrera/cs/"](https://fce.ufm.edu/carrera/cs/)

- [ ] GET title
- [ ] GET and display the href
- [ ] Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically)
- [ ] GET following &lt;meta>: "title", "description" ("og")
- [ ] count all &lt;a> (just display the count)
- [ ] count all &lt;div> (just display the count)


## 4. Directorio
using ["https://www.ufm.edu/Directorio"](https://www.ufm.edu/Directorio)

- [ ] Sort all emails alphabetically (`href="mailto:arquitectura@ufm.edu"`) in a list, dump it to logs/4directorio_emails.txt
- [ ] Count all emails that start with a vowel. (just display the count)
- [ ] Group in a JSON all rows that have `Same Address` (dont use Room number) as address, dump it to logs/4directorio_address.json


```javascript
{
    "Edificio Academico":[
        "Arquitectura",
        "Ciencias Economicas",
        .
        .
        .
        "Crédito Educativo"
    ],
    "Centro Estudiantil":[
        "Admisiones",
        .
        .
        .
         "Desarrollo"
    ],
    .
    .
    .
}
```

- [ ] Try to correlate in a JSON Faculty Dean and Directors, and dump it to `logs/4directorio_deans.json`

```javascript
{
    "Facultad de Arquitectura": {
            "Dean/Director": "Roberto Quevedo",
            "email": "rquevedo@ufm.edu",
            "Phone Number": "2338-7709"
        },
    "Facultad de Ciencias Económicas": {
        "Dean/Director": "Mónica Rio Nevado de Zelaya",
        "email": "zelaya@ufm.edu",
        "Phone Number": "2338-7723 2338-7724"
    }
    .
    .
    .
}
```

- [ ] GET the directory of all 3 column table and generate a CSV with these columns (Entity,FullName, Email), and dump it to `logs/4directorio_3column_tables.csv`

| Entity        	| FullName                	| Email            	|
|---------------	|-------------------------	|------------------	|
| Rector        	| Gabriel Calzada Álvarez 	| rectoria@ufm.edu 	|
| Campus Madrid 	| Gonzalo Melián          	| gmelian@ufm.edu  	|
| Alumni        	| Marcela Porta           	| alumni@ufm.edu   	|


## 5. Extra
- [ ] Complete Dockerfile
- [ ] Create README section for Dockerfile under [`Usage Dockerfile`](#usage-dockerfile)
- [ ] Add CI to your own repo.


---
# Start your project
In order to start your project:
- you **MUST** [fork](https://help.github.com/en/articles/fork-a-repo) this repository into **your own personal repo** in **github**
- you will need to use git and commit every once in a while, every commit must have a meaningful message.
- to start using it:
  ```bash
  # clone
  git clone <your own personal repo URL>
  # install dependencies
  pip install -r requirements.txt
  # run it
  python soup.py
  # or
  ./soup.py
    ```

- [x] everytime you complete an "item" make sure to mark it as done [x]

## Usage Dockerfile
```bash
Put your Docker build/run/etc commands here
```

---
# Delivery
- FORK IT!!
- This will be developed individually
- You will send the response via miU
- You will respond only with the URL of your git repo. (preferable git tags)
- your name (username) MUST have commits in the git log.
- it must compile & work!
- READ all README.me first