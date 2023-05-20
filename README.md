# Monefy Data Formatter

A simple package with a CLI to download and format a [Monefy](https://monefy.me/) app backup data .csv to make easier to keep your personal finances on track :money_with_wings: :rocket:

## Installation
Use [poetry](https://python-poetry.org) python dependency manager to install the formatter.
```
poetry install
```

## How to use

You can provide a shared link of the raw data from monefy app backup .csv in a google drive folder

```
monefy format --url https://drive.google.com/file/d/your_file_id/view?usp=share_link
```

Or you can provide a file_id

```
monefy format --file_id your_file_id
```
