user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    # init new dictionary
    user_preferences_clean = {}
    # loop over dictionary
    for key, value in user_preferences.items():
        # if item is not not, add to new one
        if value != None:
            user_preferences_clean[key] = value
    return user_preferences_clean


print(update_preferences(user_preferences))
