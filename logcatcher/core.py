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
    "create_logfile": False,
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
            f"{datetime.datetime.now()} LogCatcher: Invalid configuration!"
        )

    logfile_path = get_logfile_path()

    if not config["create_logfile"] and not os.path.exists(logfile_path) and not config["create_on_exception"]:
        raise FileNotFoundError(
            f"{datetime.datetime.now()} LogCatcher: Logfile path does not exist!"
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

def log(message):
    log_entry = ""

    if config["save_dateandtime"]:
        log_entry += f"[{datetime.datetime.now()}] "

    log_entry += message

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
        raise ValueError(f"{datetime.datetime.now()} LogCatcher: Logfile path is set to False. Cannot clear logfile.")
    
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

    log(error)

    if config["manual_save"]:
        save()
    
sys.excepthook = exception_handler

