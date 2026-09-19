import datetime
import traceback
import os
import sys
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logs = []
ExcCheck = False


config = {
    "save_dateandtime": True,
    "save_exception": True,
    "create_on_exception": False,
    "create_logfile": True,
    "exception_type": None,
    "logfile_path": "",
    "manual_save": True
}

def current_conf():
    print(config)

def get_logfile_path():
    path = config["logfile_path"]

    if path == "" or path is False:
        return os.path.join(os.getcwd(), "log.txt")

    if path.endswith("/") or path.endswith("\\"):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(path, f"log_{now}.txt")

    return path


def setup(**options):
    config.update(options)

    if not config["create_logfile"] and (
        config["logfile_path"] == "" or config["logfile_path"] is False
    ):
        raise ValueError(
            f"{datetime.datetime.now()} LogBuilder: Invalid configuration!"
        )

    logfile_path = get_logfile_path()

    if not config["create_logfile"] and not os.path.exists(logfile_path) and not config["create_on_exception"]:
        raise FileNotFoundError(
            f"{datetime.datetime.now()} LogBuilder: Logfile path does not exist!"
        )

    if config["create_logfile"]:
        folder = os.path.dirname(logfile_path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(logfile_path):
            with open(logfile_path, "w", encoding="utf-8"):
                pass
        

def save():
    logfile_path = get_logfile_path()
    with open(logfile_path, "a", encoding="utf-8") as f:
        for log_entry in logs:
            f.write(log_entry + "\n")

    logs.clear()

def log(message, type):
    log_entry = ""

    if type is None:
        type_entry = None
    elif type == "info":
        type_entry = "[INFO]"
    elif type == "warn":
        type_entry = "[WARNING]"
    elif type == "error":
        type_entry = "[ERROR]"
    else:
        raise ValueError(
            f"{datetime.datetime.now()} LogBuilder: Invalid type!"
        )

    if config["save_dateandtime"]:
        log_entry += f"[{datetime.datetime.now()}] "

    log_entry += (type_entry if type_entry is not None else "") + (" " if type_entry is not None else "") + message

    if config["save_exception"]:
        tb = traceback.format_exc()

        if tb != "NoneType: None\n":
            log_entry += "\n" + tb

    logs.append(log_entry)

    if not config["manual_save"]:
        save()


def clear():
    if config["manual_save"]:
        logs.clear()
    else:
        with open(config["logfile_path"], "w", encoding="utf-8") as f:
            f.write("")

def clear_memory():
    logs.clear()

def clear_logfile():
    if config["create_logfile"]:
        if config["logfile_path"] == "":
            logfile_path = os.path.join(os.getcwd(), "log.txt")
        else:
            logfile_path = config["logfile_path"]

        with open(logfile_path, "w", encoding="utf-8") as f:
            f.write("")
    
    elif config["logfile_path"] == False:
        raise FileNotFoundError(f"{datetime.datetime.now()} LogBuilder: Could not find LogFile!")
    
def dtn(function):
    if function == "dat":
        return datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    elif function == "date":
        return datetime.date.today().strftime("%Y-%m-%d")

    elif function == "time":
        return datetime.datetime.now().strftime("%H:%M:%S")
    
def exception_handler(exc_type, exc_value, exc_traceback):
    if not config["save_exception"]:
        return

    error = "".join(
        traceback.format_exception(
            exc_type,
            exc_value,
            exc_traceback
        )
    )

    if config["manual_save"]:
        save()
    else:
        log(error, config["exception_type"])

    
sys.excepthook = exception_handler



