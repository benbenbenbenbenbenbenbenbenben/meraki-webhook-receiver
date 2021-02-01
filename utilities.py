import datetime

class colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Style our console log messages
def message_print(title, message = 'No Message Details'):
    timestamp = datetime.datetime.now()
    print(f'{colors.OKBLUE}<---{timestamp}----{title}------------------------->{colors.ENDC}')
    print(message)
