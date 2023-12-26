import json

def get_user_configs(context):
        configFilename = context.config.userdata.get("configs")
        if(configFilename is None):
            raise ValueError('Please specify the config file path using flag "-D configs=<configs>"')
        return json.load(open(configFilename))