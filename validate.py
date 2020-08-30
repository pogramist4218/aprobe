import os
import re
import sys
from pathlib import Path


def validate(args):
    if not os.path.exists(args.path):
        raise NotExistPath(args.path)
    elif not os.path.isfile(args.path):
        raise NotFile(args.path)
    elif Path(args.path).suffix != '.wav':
        raise NotNeededExtensionOfFile(args.path)
    elif not re.fullmatch('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', args.phone):
        raise NotValidFormatOfPhone(args.phone)
    return True


class NotFile(Exception):
    pass

class NotExistPath(Exception):
    pass

class NotNeededExtensionOfFile(Exception):
    pass

class NotValidFormatOfPhone(Exception):
    pass
