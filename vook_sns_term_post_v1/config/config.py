import os

from vook_sns_term_post_v1.config.local_config import OPENAI_API_KEY

# def config_loader():
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
