userlist
========

CLI for listing the users on a Linux machine.

## Usage

All the arguments are optional. Pass in the path to the file you want the user list to be exported to. Pass in the desired format, json or csv.

If no path is provided, the tool outputs to terminal. If no format is provided, the tool defaults to json.

If you pass in the path to a file that doesn't exist, the tool will create one in the current directory. If the file already exists, the tool will append the user list to said file.

Example with path and format:

```
$ userlist --path /path/to/file.txt --format json
```

Example with format only:

```
$ userlist --format csv
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:jos3neto/userlist.git`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`