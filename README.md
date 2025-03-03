# Official RadioCo website

Port of a existing wordpress project, so don't expect clean code

## Getting Started

Installation should be pretty straightforward:

### Prerequisites and Installation

Have docker installed, change your .env variables, then run:

```
./run start_dev
```

To get help just run without arguments:
```
./run
```

compress
```
rm -rf static
poetry run python manage.py collectstatic --no-input
poetry run python manage.py compress
poetry run python manage.py collectstatic --no-input
python manage.py runserver --nostatic
```

## Features

* Few dependencies
* No database
* Internationalization Support


## Built With

* [Python 3](https://www.python.org) - Programming language used
* [Django 2](https://www.djangoproject.com/) - The web framework used
* [Sass](https://sass-lang.com/) - Used to generate CSS
* [Yaml](http://yaml.org/) - Used to store data

## Contributing

Any help is welcome.

Help us to [translate](https://poeditor.com/join/project/wc3P8dCind)!
No need to install or setup anything, just follow [this link](https://poeditor.com/join/project/wc3P8dCind).

## Authors

* **Iago Veloso** - *Initial work* - [Github](https://github.com/iago1460/)

## License

This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for details
