# backend for the factored technical test
this is the backend for the factored technical test developed in python using Fastapi and SQLAlchemy, the databse used is an Mysql database.

## Steps to execute the backend

## 1. Clone the repository
execute this command inside the desired folder to clone the repository

```
git clone https://github.com/carvesco/factored-test-back.git
```
## 2. Create a new virtual enviroment
Inside the cloned folder, execute one of these commands depending on your configurations to create a new virtual enviroment.
```
python -m venv venv
3python -m venv venv
```
## 3. Initialize the virtual enviroment
For windows execute the next command to initialize the virtual enviroment
```
venv/Script/activate
```
## 4. Install the dependencies
execute the next command to install all the dependencies needed.
```
pip install -r requirements.txt
```
## 5. Add the env variables
add a .env file to the root folder whit the same content of the .en.example file, but hange accordign to your configurations 

## 4. Start the API
Execute the next command to start the API in http://127.0.0.1:8000
```
uvicorn app:app
```