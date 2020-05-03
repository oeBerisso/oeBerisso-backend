from flaskps.helpers import field as validation
from flaskps.helpers import auth as helper_auth
from flask import session

def validate(rules, form=[]):
    username = helper_auth.authenticated(session) or ""
    switch = {
        "compare_fields": lambda field: validation.compare_fields(
            form[field],
            rules[field]["name"],
            form[rules[field]["compare_fields"]],
            rules[rules[field]["compare_fields"]]["name"],
        ),
        "min_length": lambda field: validation.min_length(
            form[field], rules[field]["name"], rules[field]["min_length"]
        ),
        "max_length": lambda field: validation.max_length(
            form[field], rules[field]["name"], rules[field]["max_length"]
        ),
        "email": lambda field: validation.email(form[field]),
        "unique_mail": lambda field: validation.unique_mail(form[field], username),
        "unique_user": lambda field: validation.unique_user(form[field]),
        "presence": lambda field: validation.presence(
            form[field], rules[field]["name"]
        ),
        "type_number": lambda field: validation.type_number(
            form[field], rules[field]["name"]
        ),
        "name": lambda field: 0,
    }
    error_count = 0
    for field_rules in dict.keys(rules):
        for rule in dict.keys(rules[field_rules]):
            func = switch.get(rule, lambda: "nothing")
            result = func(field_rules)
            error_count += result
            if result == 1 and rule == "presence":
                break

    return error_count
