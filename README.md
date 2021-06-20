# Pimado

A local browser-based to-do list application with markdown export.  
View the [showcase](https://github.com/noelkronenberg/pimado#showcase) for visual a representation of the current product, or [this](https://github.com/noelkronenberg/pimado/projects/1) project for the future roadmap.

## Basic Requirements

- macOS
- Browser
- Terminal
- Python 3 (e.g., via [Homebrew](https://brew.sh/))
- pip3 (should come with Homebrew)

## Set-up

```
git clone https://github.com/noelkronenberg/pimado
cd pimado
python pimado.py
```

## Usage

After running `pimado.py`, you can access the application via http://127.0.0.1:8000/. To-do items you create will be stored locally, and are accessible for every succeeding session. If you want to update to a newer version of Pimado, simply replace the database (i.e., the *db.sqlite3* file) in the updated version with your current instance.

## References

- [Basic to-do list structure](https://youtu.be/ovql0Ui3n_I)
- [File download](https://linuxhint.com/download-the-file-in-django/)
- [Marcus Aurelius quote](https://youtu.be/AiM9YcE0LT4?t=46)

## Showcase

![20210601_Pimado_00](https://user-images.githubusercontent.com/79874249/120317037-6ea88c00-c2de-11eb-9a03-4f6173dd02b8.jpg)

https://user-images.githubusercontent.com/79874249/120314448-8a5e6300-c2db-11eb-951b-ff1f17e53ad9.mp4

https://user-images.githubusercontent.com/79874249/120314502-9813e880-c2db-11eb-850e-dd29066a473c.mp4

## Beginner

If you are new to Python and/ or CS in general, refer to the [Initial Usage](https://github.com/noelkronenberg/pimado#initial-usage) section for first-time use. For use after the first, just refer to the [Normal Usage](https://github.com/noelkronenberg/pimado#normal-usage) section.

### Initial Usage

1. Open your terminal (hit command + space bar and search for `Terminal`)
2. Paste the following command, hit enter, and follow the prompts:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Paste the following commands and hit enter:
```
git clone https://github.com/noelkronenberg/pimado
cd pimado
python pimado.py
```
4. Open http://127.0.0.1:8000/ in your browser

### Normal Usage

1. Open your terminal (hit command + space bar and search for `Terminal`)
2. Paste the following commands and hit enter:
```
cd pimado
python pimado.py
```
3. Open http://127.0.0.1:8000/ in your browser

