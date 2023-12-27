import json

class ConfigsManager:

    user_configs = None

    def __init__(self, context):
        configFilename = context.config.userdata.get("configs")
        if(configFilename is None):
            raise ValueError('Please specify the config file path using flag "-D configs=<configs>"')
        self.user_configs = json.load(open(configFilename))

    @property
    def browser_name(self):
        return self.user_configs['browser_name']

    @property
    def base_url(self):
        return self.user_configs['base_url']

    @property
    def headless_mode_enabled(self):
        return bool(self.user_configs['headless_mode_enabled'])

    @property
    def page_load_timeout(self):
        return int(self.user_configs['page_load_timeout_seconds'])

    @property
    def implicitly_wait(self):
        return int(self.user_configs['implicitly_wait_seconds'])