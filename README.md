# Pimado

A minimalist and privacy-focused (i.e., local) to-do list application that is accessible via the browser and has markdown export.

![20210601_Pimado_00](https://user-images.githubusercontent.com/79874249/120317037-6ea88c00-c2de-11eb-9a03-4f6173dd02b8.jpg)

https://user-images.githubusercontent.com/79874249/120314448-8a5e6300-c2db-11eb-951b-ff1f17e53ad9.mp4

https://user-images.githubusercontent.com/79874249/120314502-9813e880-c2db-11eb-850e-dd29066a473c.mp4

## Set-up

### Beginner

1. Download and unzip file  
2. Open your terminal
4. Paste the following commands and hit enter:
```
cd downloads/pimado-main && pipenv shell
```
4. Paste the following commands and hit enter:
```
pipenv install django==2.1 && python manage.py runserver
```
5. Open http://127.0.0.1:8000 in your browser

### Regular

1. Direct terminal to the downloaded folder
2. Launch subshell in virtual environment (*pipenv shell*)
3. Install Django 2.1 (*pipenv install django==2.1*)
4. Start development server (*python manage.py runserver*)
5. Open development server URL

https://user-images.githubusercontent.com/79874249/120315832-0c9b5700-c2dd-11eb-9e2c-e0c04b2c5b74.mp4

## Roadmap

- [x] Markdown file export
- [x] Better UX
- [ ] Markdown file import
- [ ] Variable dashboard text
- [ ] Easier set-up

## References

- [Basic to-do list structure](https://youtu.be/ovql0Ui3n_I)
- [File download](https://linuxhint.com/download-the-file-in-django/)
