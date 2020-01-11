import re


def get_all_ascii_text(text):
    ''' 
    remove all the non-ascii characters from the text
    Args:
        text: str
    Returns:
        modified_text: text with all the non-ascii characters removed.
    '''
    return re.sub('[^\x00-\x7F]', '', text)  # 7F is 127


def get_all_non_ascii_text(text):
    '''
    Remove all the ascii characters from the given text
    Args:
        text: str
            Can be combination of both ascii and non-ascii characters.
    '''
    # allows space (\x20) in the text
    return re.sub('[\x00-\x19\x21-\x7F]', '', text)

