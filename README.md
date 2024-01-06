# Bootstap project

## Set up virtual env

```
python3 -m venv ml-venv
source ml-venv/bin/activate
python -m pip install -U pip
```

## Install required dependencies

```
python -m pip install -r requirements.txt
```

# Managing the project

## Adding a requirment

You can add or remove dependencies with pip
ie

```
python -m pip install mypackage
```

## Set up env

Run `source ml-venv/bin/activate` and you should see the following

```
➜  pneumonia-detector git:(master) ✗ source ml-venv/bin/activate
(venv) ➜  pneumonia-detector git:(master) ✗
```

## Take down env

```
deactivate
```
