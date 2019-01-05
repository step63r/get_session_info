# get_session_info

Get session information from Microsoft summit.

This scripts is suitable for Microsoft Tech Summit 2018 currently.

## Description

You can get session information of Microsoft Tech Summit 2018 with this script.

You can get PDF/PPT status of each session. ``○`` means the PDF/PPT is ready to get, ``★`` means is coming soon, and ``-`` means not available, unfortunately.

## Requirement

- Windows 10 Home (64-bit)
- Python 3.6.5
- selenium 3.14.1
- Google Chrome
- ChromeDriver 2.45

## Usage

### Edit ``config.py``

At first, you have to edit ``config.py`` for your environment.

#### APP_PATH

Set your Google Chrome path. 

Usually the app exists ``Program Files`` in 32-bit or ``Program Files (x86)`` in 64-bit Windows.

#### DRIVER_PATH

Set your ChromeDriver path.

### Execute script

And then, you can execute this as below at script directory.

```
$ python ./get_session_info.py [ADDRESS] [PASSWORD] [OUTPUT_PATH]
```

#### ADDRESS

Set your Microsoft account address.

#### PASSWORD

Set you Microsoft account password.

#### OUTPUT_PATH

Set output csv file path.

## Contribution

Fork this repository and clone yours.

Please give me pull requests any time!!

## Licence

MIT License

## Author

[minato](https://blog.minatoproject.com/)