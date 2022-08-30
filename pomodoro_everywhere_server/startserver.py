import sys
import os
import manage


def check_secret():
    local_settings_paths = ["pomodoro_everywhere_server/pomodoro_everywhere_server", "pomodoro_everywhere_server"]

    secrets_path = None
    for path in local_settings_paths:
        if os.path.isdir(path):
            secrets_path = path + os.sep + "local_settings.py"
            break

    if secrets_path == None:
        print("Are you in right directory?")
        exit(1)
    
    if os.path.isfile(secrets_path):
        return True
    else:
        print("""create file pomodoro_everywhere_server/local_settings.py with following content:

"SECRET_KEY = 'your_django_secret_key'")

or I can generate it for you.
You're in? (y/n) """, end = "")
    answer = input().lower()
    if answer == "y":
        from django.utils.crypto import get_random_string

        lower_plus_numbers = (list(chr(o) for o in range(0x61, 0x7B))
                              + list(chr(o) for o in range(0x30, 0x3A)))
        punctuation = list('!@#$%^&*(-_=+)')
        upper_alpha = list(chr(o) for o in range(0x41, 0x5B))

        allowed_chars = lower_plus_numbers + punctuation + upper_alpha
        
        content_secret_py = f"SECRET_KEY = '{get_random_string(60,allowed_chars)}'"
        with open(secrets_path, mode="wb") as file:
            file.write(content_secret_py.encode("utf-8"))
        del content_secret_py
        return True
    elif answer == "n":
        sys.exit(1)
    else:
        return False
        


FIRSTRUN = "runserver" not in sys.argv
if FIRSTRUN:
    sys.argv.insert(1, "runserver")

    while check_secret() == False:
        pass

    

manage.main()
