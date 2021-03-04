from .utils import availability_utils


def end_all_conversation():
    if availability_utils.is_available():
        return

    # End all conversation
    print('ended all conversations')
