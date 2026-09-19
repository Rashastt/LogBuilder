# LogBuilder

## Current version: 1.1.1
[Changelog](CHANGELOG.md)

A simple and lightweight Python library for building, storing, and managing logs.

## Features

- Automatic log file creation
- Date and time support
- Traceback capturing
- Manual or automatic log saving
- Save logs only when an exception occurs
- Memory log storage
- Log file management
- Simple configuration system

## Installation

Install from PyPI:

```pip install LogBuilder```

## Functions

- ```LogBuilder.setup()``` : Setups LogBuilder with your customized configurations.

- ```LogBuilder.log()``` :  Logs an customized input. Saves to the memory instead if ```manual_save``` is ```True```.

- ```LogBuilder.save()``` : Saves the memory logs to the file.

- ```LogBuilder.current_conf()``` : Shows the current configuration in a JSON format.

- ```LogBuilder.clear()``` : Clears the logs or the file depending on the configurations. If ```manual_save``` is ```True```, then it clears the memory. If it's ```False```, it clears the file.

- ```LogBuilder.clear_memory()``` : Clears the memory.

- ```LogBuilder.clear_logfile()``` : Clears the logfile.