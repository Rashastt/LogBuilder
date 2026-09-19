from .core import setup, save, log, clear, clear_memory, clear_logfile, dtn, current_conf
import datetime

def config():
    raise AttributeError(f'{datetime.datetime.now} LogBuilder: "config" is not callable. Did you mean "LogBuilder.setup"?'
)