# employment-platform

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

## To create a virtual environment
1- Open the project folder .

2- Run this command .
```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv
```
## Here activate a new virtual environment called .venv:
```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```
## To deactivate and leave a virtual environment type deactivate.
```bash
# Windows
(.venv) > deactivate
>

# macOS
(.venv) % deactivate
%
```

## install requirements.txt
```bash
pip install -r requirements.txt
```

## You might see a WARNING message about updating pip after running these commands. It’s always good to be on the latest version of software and to remove the annoying WARNING message each time you use pip. You can either copy and paste the recommended command or run python -m pip install --upgrade pip to be on the latest version.
```bash
(.venv) > python -m pip install --upgrade pip
```

## Now let’s confirm everything is working by running Django’s internal web server via the runserver command

```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```