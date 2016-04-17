# dmcathis

### Run this script in a supervisor

First, install supervisor (`sudo apt-get install supervisor`).

Second, create a config file for your daemon at /etc/supervisor/conf.d/dmcathisd.conf

```ini
[program:dmcathisd]
directory=/path/to/project/root
environment=ENV_VARIABLE=example,OTHER_ENV_VARIABLE=example2
command=python dmcathisd.py
autostart=true
autorestart=true
```

3) Restart supervisor to load your new .conf

```bash
supervisorctl update
supervisorctl restart dmcathisd
```
