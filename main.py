def format_string(string:str, length:int):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        string = " " * spaces + string
        return string
format_string("aaaa",10)