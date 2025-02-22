def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet_float = float(parts[0])
    inches_float = float(parts[1])
    return {"feet": feet_float, "inches": inches_float}


