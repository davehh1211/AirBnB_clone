# AirBnB Clone Project - Console

The console is the first part of the AirBnB project assigned to the second trimester for Holberton Students. It a clone of the AirBnb website and its content in backend and frontend. 

The objective of this project is to cover up the basics and fundamental topics of higher programming languages and its applicability in the deployment of webservers. 

In this segment we will have the opportunity of creating a command line interpreter with the module `` cmd `` and respond to it.

## [AirBnB Project link](https://intranet.hbtn.io/projects/263)
For further information, click on the previous link. 

## Table of content
- [AirBnB Clone Project - Console](#airbnb-clone-project---console)
	- [AirBnB Project link](#airbnb-project-link)
	- [Table of content](#table-of-content)
	- [Prerequisites](#prerequisites)
	- [Environment](#environment)
	- [Installation](#installation)
	- [Functionalities and contents](#functionalities-and-contents)
	- [Examples](#examples)
	- [Built with...](#built-with)
	- [Authors](#authors)

## Prerequisites

For further installation is necessary to set this program on Ubuntu 14.04 LTS using Vagrant in VirtualBox.

You need to install this software
```
1. VirtualBox - Virtual Machine
2. Vagrant
3. Emacs
4. Vim/Vi
5. VSCode
```

## Environment

This project was constructed and tested in Ubuntu 14.04 LTS

## Installation
Follow the following instructions to get a copy of the program and run in your local machine.

- Clone the following repository. 
 > `https://github.com/angellovc/AirBnB_clone`  

- Run the program
 > `./console.py`

## Functionalities and contents

| File | Method | Description |
| ---- | ------ | ----------- |
| [console.py](./console.py) | command interpreter | The starting point of the console functionality |
|| ``quit`` | It terminates the console and exit the program |
|| ``help`` | It gives information about a command line |
|| ``<emptyline>`` | It loops the console when the user presses enter |
|| ``create`` | It creates a new instance of the BaseModel and saves it to JSON file |
|| ``show`` | It shows and prints the string representation of the instances created |
|| ``destroy`` | It deletes an instance based on the class name and id |
|| ``all`` | It prints all the string representation of all instances |
|| ``update`` | It updates an instance based on the class name and id by adding or updating an attribute |
| [base_model.py](./models/base_model.py) | Instanciator | The BaseModel defines all common attributes/methos for other classes |
|| ``def __init__(self, *args, **kwargs)`` | Initialization of BaseModel receiving commands line |
|| ``def save(self)`` | It saves new instances and updates attributes to a JSON file |
|| ``def to_dict(self)`` | It returns a dictionary containing all keys/values of an instance |
|| ``def __str__(self)`` | It prints the string representation of the BaseModel class |
| [classes that inherits from BaseModel](./models) | ``user.py`` | It represents the user |
|| ``amenity.py``| It represents the amenity that the user requires |
|| ``city.py`` | The city to visit|
|| ``place.py``| The place to stay |
|| ``review.py`` | The critic of the place|
|| ``state.py`` | The state of the city |
|[File Stoorage](./models/engine/file_storage.py)|File Storage|It serializes instances to JSON file and deserializes JSON file to instances|
||``all``|It returns a dictionary of instances and attributes|
||``new``|It sets the object to a new instance and key into the dictionary|
||``save``|It serializes the dictionary to the JSON file|
||``reload``|It deserializes the JSON file to a directory|


## Examples

To start the console, execute the file console.py ``./console `` and then write the command line. Press enter to run the command. 

```
vagrant@;[AirBnB_clone]; ~$./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all mymodel
** class doesn't exist **
(hbnb) create BaseModel
2750042b-bd56-417a-abae-f27c10352036
(hbnb) all BaseModel
["[BaseModel] (2750042b-bd56-417a-abae-f27c10352036) {'created_at': datetime.datetime(2020, 6, 30, 14, 27, 25, 108889), 'updated_at': datetime.datetime(2020, 6, 30, 14, 27, 25, 108979), 'id': '2750042b-bd56-417a-abae-f27c10352036'}", "[BaseModel] (c59f04fc-e383-4347-bf11-c7e3ddfbc400) {'__class__': 'BaseModel', 'created_at': datetime.datetime(2020, 6, 29, 4, 1, 43, 637709), 'updated_at': datetime.datetime(2020, 6, 29, 4, 1, 43, 637811), 'id': 'c59f04fc-e383-4347-bf11-c7e3ddfbc400'}", "[BaseModel] (33fd6e27-6c3a-481c-a517-7244602a90db) {'first_name': 'Betty', '__class__': 'BaseModel', 'created_at': datetime.datetime(2020, 6, 29, 3, 59, 47, 707579), 'updated_at': datetime.datetime(2020, 6, 29, 4, 1, 10, 362353), 'id': '33fd6e27-6c3a-481c-a517-7244602a90db'}"]
```
Here you can evidence the execution of the commands help, create and and all. As you can see, a new instance is created and then shown as a directory. 

```
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 2750042b-bd56-417a-abae-f27c10352036
[BaseModel] (2750042b-bd56-417a-abae-f27c10352036) {'created_at': datetime.datetime(2020, 6, 30, 14, 27, 25, 108889), 'updated_at': datetime.datetime(2020, 6, 30, 14, 27, 25, 108979), 'id': '2750042b-bd56-417a-abae-f27c10352036'}
```

Here, we want to see an instance created, but for that we need the specific Id to see that instance.

```
(hbnb) destroy BaseModel 2750042b-bd56-417a-abae-f27c10352036
(hbnb) show BaseModel 2750042b-bd56-417a-abae-f27c10352036
** no instance found **
```
Here we want to delete an instance. We must give the id and then enter, it will delete that instance. 

## Built with...

- Visual Studio Code - Coding and structuring.

##  Authors

- [GitHub - Angello Villegas](https://github.com/angellovc)

- [GitHub - Oscar David Henao Hidalgo](https://github.com/davehh1211)
