# To-Do List

A minimalist and privacy-focused (i.e., local) to-do list application that is accessible via the browser and has markdown export.

*Notice: Due to active development videos might be temporarily outdated*

https://user-images.githubusercontent.com/79874249/120218723-76aef000-c23a-11eb-99db-e7488d4e4249.mp4

https://user-images.githubusercontent.com/79874249/120218739-7b73a400-c23a-11eb-8270-69b8bc1be99b.mp4

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

## Roadmap

- [x] Markdown file export
- [x] Better UX
- [ ] Markdown file import
- [ ] Variable dashboard text
- [ ] Easier set-up

## References

- [Basic to-do list structure](https://youtu.be/ovql0Ui3n_I)
- [File download](https://linuxhint.com/download-the-file-in-django/)
