import os
import yaml
from pyautomation import LOG
from pyautomation.file_manager.file_manager import FileManager


class Config(object):

    def __init__(self, filename=None):
        self.yml_dict = None
        if os.environ.get('AUTO_CONFIG', None):
            LOG.info("getting AUTO_CONFIG configuration file")
            self.filename = os.environ['AUTO_CONFIG']
        elif filename:
            LOG.info("using log file: " + filename)
            self.filename = filename
        else:
            self.filename = os.path.join(FileManager.get_project_root(), "config", "default.yml")
            LOG.info("current working directory :" + os.getcwd())
            LOG.info("using default config file: " + self.filename)
        try:
            self._load_config(self.filename)
        except FileNotFoundError as f:
            LOG.info("Exception occured " + str(f))
            LOG.info("Please put config file in [projectRoot]/config/default.yml or set environ variable AUTO_CONFIG")

    def _load_config(self, filename):
        config_yaml = open(filename, 'r')
        self.yml_dict = yaml.load(config_yaml)
        LOG.info("Succesfully Loaded config")
        config_yaml.close()
        

    def get(self, key, default=None):
        if "." in key:
            tmp = self.yml_dict
            keys = key.split(".")
            for k in keys:
                tmp = tmp[k]
            LOG.info("config returning {0}: {1}".format(key, tmp))
            return tmp
        else:
            return default
