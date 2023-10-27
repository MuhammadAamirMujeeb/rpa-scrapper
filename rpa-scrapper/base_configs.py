import os

XPATHS_MAPPER_VARIABLE_NAME = 'XPATHS_MAPPER'  # set name for xpath mapper variable name to be used in scrapers
ENVIRONMENT = os.getenv('environment', default=None)
DOWNLOAD_DIRECTORY = f'{os.getcwd()}/output'
