# Coffeegonewild

## Description
This project was implemented as a part of the Python full-stack sofeware development course at Coding Dojo (https://www.codingdojo.com/). The main purpose was to practice and to showcase the technologies and skillsets that I have acquired during the bootcamp. 

As a coffee enthusiast myself, I look for exotic coffee recipes often but found it frustrating due to the scatterness of the resources. Therefore, I wanted to create an online library of the most unique coffee recipes so that people like me can enjoy exotic coffee drinks even without stepping out of the house. 

Besides the technologies, the two most important skills that I have improved on were project management and problem solving, both of the which were critical in ensuring smooth development and on-time delivery of the project. 

## Demo
https://www.youtube.com/watch?v=bogAChZY-VA

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Todo](#todo)

## Prerequisites
- [Python 3.10](https://www.python.org/downloads/) (Mac)
- [Python 3.10](https://www.python.org/downloads/windows/) (Windows)

## Installation 
1. Clone the repo
   ```
   git clone https://github.com/jingwenl0718/Coffeegonewild.git
   ```

2. Install Virtual Environment tool
   Mac:
   ```
   pip3 install pipenv
   ```
   Windows:
   ```
   pip install pipenv
   ```

3. Install Flask
   ```
   pipenv install flask
   ```
   Note: If you receive an error using pipenv, you may need to import it as a module first before it can be run as a script. You can do so using the -m flag as below. You will need to do this every time you use pipenv.
   Mac:
   ```
   python3 -m pipenv
   ```
   Windows:
   ```
   python -m pipenv
   ```

## Usage
1. Activate Virtual Environment
   ```
   pipenv shell
   ```
   Note: To deactivate the Virtual Environment, use 
   ```
   exit
   ```

2. Run the application
   After navigating to the project directory, run the following command. Make sure the Virtual Environment is running already.
   ```
   python server.py
   ```

3. Open a browser and navigate to localhost:5000/coffeegonewild. 

## License
MIT License (https://github.com/jingwenl0718/Coffeegonewild/blob/main/LICENSE.md)

## Todo
- Implement uploading recipes functionality to allow users share coffee recipes with other coffee enthusiasts. 

- Implement saving recipes functionality to allow users to favorite recipes and save them in their individual accounts.
