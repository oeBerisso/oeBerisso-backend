def must_be_closed(maintenance, page, exceptions):
    return True if (int(maintenance) and (not page in exceptions)) else False
