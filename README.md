# server for application Pomodoro-Everywhere

To clone and setup server run:
```
git clone https://github.com/Pomodoro-Everywhere/server/
cd server
python3 pomodoro_everywhere_server/manage.py migrate
python3 pomodoro_everywhere_server/startserver.py [PORT]
```

By default port is 8000. So this argument is not required.

Then you can go to [http://localhost:PORT/api](http://localhost:8000/api) to check that server is running.

