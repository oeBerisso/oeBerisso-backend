from flaskps.helpers import field as validation
from flaskps.helpers import auth as helper_auth
from flask import session

def validate(rules, form=[], js=False):
    username = helper_auth.authenticated(session) or ""
    switch = {
        "compare_fields": lambda field: validation.compare_fields(
            js,
            form[field],
            rules[field]["name"],
            form[rules[field]["compare_fields"]],
            rules[rules[field]["compare_fields"]]["name"],
        ),
        "min_length": lambda field: validation.min_length(
            js, form[field], rules[field]["name"], rules[field]["min_length"]
        ),
        "max_length": lambda field: validation.max_length(
            js, form[field], rules[field]["name"], rules[field]["max_length"]
        ),
        "email": lambda field: validation.email(js, form[field]),
        "unique_mail": lambda field: validation.unique_mail(js, form[field], username),
        "unique_user": lambda field: validation.unique_user(js, form[field]),
        "presence": lambda field: validation.presence(
            js, form[field], rules[field]["name"]
        ),
        "type_number": lambda field: validation.type_number(
            js, form[field], rules[field]["name"]
        ),
        "name": lambda field: 0,
    }
    error_count = 0
    json = {}
    for field_rules in dict.keys(rules):
        json = {**json, field_rules: []}

        for rule in dict.keys(rules[field_rules]):
            func = switch.get(rule, lambda: "nothing")
            result = func(field_rules)
            if js:
               if not result == 0: json[field_rules].append(result)
            else:
                error_count += result

            if (result == 1 or result == "El campo es requerido") and rule == "presence":
                break
    if js:
        for key in list(json.keys()):
            if len(json[key]) == 0: json.pop(key)

        return json
    else:
        return error_count
