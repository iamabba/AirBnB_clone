<img src="https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67"> 
# AirBnB Clone - The Console

---

## Description

This project is the first step towards building a full web application of the AirBnB clone. In this first step we are building a console, a custom command interpreter that will be used in subsequent AirBnB projects to manage objects of our classes.

This console will allow us to do the following:

* Create a `new object`
* Retrieve an object from a `file, a database etc…`
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Usage

* The console can be run in both interactive and non-interactive mode.
* It prints a prompt **(hbnb)** and waits for the user for input.

### Interactive Mode

```cmd
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode

```cmd
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Commands

Command | Description
--- | ---
`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id

---
# PART 2 OF AIRBNB CLONE - WEBSTATIC 
Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages
Style guide
Fake contents
No Javascript
No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

Resources
Read or watch:

Learn to Code HTML & CSS (until “Creating Lists” included)
Inline Styles in HTML
Specifics on CSS Specificity
CSS SpeciFishity
Introduction to HTML
CSS
MDN
center boxes
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is HTML
How to create an HTML page
What is a markup language
What is the DOM
What is an element / tag
What is an attribute
How does the browser load a webpage
What is CSS
How to add style to an element
What is a class
What is a selector
How to compute CSS Specificity Value
What are Box properties in CSS
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be W3C compliant and validate with W3C-Validator
All your CSS files should be in styles folder
All your images should be in images folder
You are not allowed to use !important and id (#... in the CSS file)
You are not allowed to use tags img, embed and iframe
You are not allowed to use Javascript
Current screenshots have been done on Chrome 56 or more.
No cross browsers
You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

finall product should be as follows
![image](https://camo.githubusercontent.com/d21799d44f5d8839a1716dba0d9e16ebd5b4a1dd9609478e8690e6db9163cfe5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3330392f68626e625f325f302e6a7067)
![image](https://camo.githubusercontent.com/ddf532ea65ccbe7c1a8c70b515e045bb105772422160ce128edaf0e6bb78df6d/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3330392f68626e625f315f322e6a7067)

## Authors

* ** christian ng'ang'a** - Github: [themathecs](https://github.com/themathematcs) 
* ** Ahmed Abba Musa ** - Github: [iamabaa](https://github.com/iamabaa) 
