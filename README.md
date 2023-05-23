# Python Virtual Environment Set up

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtualenv dependency.

``` bash
pip install virtualenv
```

Create a virtual environment (Python v3.9.7) inside the project folder with the following command.

``` bash
python<version> -m venv <virtual-environment-name>
```

Now active your virtual environment with the following command.

``` bash
env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershel
```

# Dependencies Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

``` bash
pip install -r requirements.txt
```