# LogCatcher

A simple and lightweight Python library for capturing, storing, and managing logs.

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

```pip install logcatcher```

## Functions

- ```logcatcher.setup()``` : Setups  LogCatcher with your customized configurations.

- ```logcatcher.log()``` :  Logs an customized input. Saves to the memory instead if ```manual_save``` is ```True```.

- ```logcatcher.save()``` : Saves the memory logs to the file.

- ```logcatcher.current_conf()``` : Shows the current configuration in a JSON format.

- ```logcatcher.clear()``` : Clears the logs or the file depending on the configurations. If ```manual_save``` is ```True```, then it clears the memory. If it's ```False```, it clears the file.

- ```logcatcher.clear_memory()``` : Clears the memory.

- ```logcatcher.clear_logfile()``` : Clears the logfile.