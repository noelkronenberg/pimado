# Pimado

A minimalist and privacy-focused (i.e., local) to-do list application that is accessible via the browser and has markdown export. [View showcase](https://github.com/noelkronenberg/pimado#showcase) for visual representation.

## Set-up

1. Download and unzip file  
2. Run the following commands (in succession):
```
cd downloads/pimado-main && pipenv shell
```
```
pipenv install django==2.1 && python manage.py runserver
```
3. Access the application via http://127.0.0.1:8000

## Usage

For usage after the initial set-up, i.e., after closing the terminal and terminating the session, just refer to step 2 and 3, and adjust the directory navigation according to your structure (i.e., *cd folder/folder/.../pimado-main*). The to-do items you create will be stored locally, and are accessible for every succeeding session.

## Roadmap

- [x] Markdown file export
- [x] Better UX
- [ ] Markdown file import
- [ ] Variable dashboard text
- [ ] Easier set-up

## References

- [Basic to-do list structure](https://youtu.be/ovql0Ui3n_I)
- [File download](https://linuxhint.com/download-the-file-in-django/)
- [Marcus Aurelius quote](https://youtu.be/AiM9YcE0LT4?t=46)

## Showcase

![20210601_Pimado_00](https://user-images.githubusercontent.com/79874249/120317037-6ea88c00-c2de-11eb-9a03-4f6173dd02b8.jpg)

https://user-images.githubusercontent.com/79874249/120314448-8a5e6300-c2db-11eb-951b-ff1f17e53ad9.mp4

https://user-images.githubusercontent.com/79874249/120314502-9813e880-c2db-11eb-850e-dd29066a473c.mp4
