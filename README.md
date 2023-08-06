# Webscraper Project

This is a web scraper project crafted in Python

## Installation

### Virtual Environment

First, you would have to create a virtual environment if you would not want to install the required dependencies globally.

Use the following command in the directory where you intend to house your application.

```
py -m venv venv
```

OR

```
python -m venv venv
```

Then, activate the virtual environment by running:
On Windows:

```
.\venv\Scripts\activate
```

OR on Mac / GitBash:

```
source ./venv/Scripts/activate
```

### Install the dependencies:

```
pip install -r requirements.txt
```

### Optional: Global Installation of Dependencies

You may also wish to install globally, the dependencies we used. Thereby, skipping the virtual environment and requirements.txt file steps above.
If so, use these commands instead in any order:

```
pip install beautifulsoup4
```

```
pip install lxml
```

```
pip install requests
```

## To run the webscraper:

Use either of the following commands, based on your operating system.

```
py index.py
```

OR

```
python index.py
```

## To run the webscraper and have the results saved to a file:

Use either of the following commands, based on your operating system.

```
py file_index.py
```

OR

```
python file_index.py
```
