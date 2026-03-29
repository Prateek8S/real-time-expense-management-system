import logging


###  Creating and configure a custom logger

def setup_logger(name, Log_file = "server_logs.log", Level = logging.DEBUG):
    
    logger = logging.getLogger(name)
    
    logger.setLevel(Level)
    file_handler = logging.FileHandler(Log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger