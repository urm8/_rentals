# rentals

To launch:

```bash
docker-compose up -d
```

Then go [here](http://localhost/). Login/pass for admin: mm/pass, if data didn't load for some reason, run:

```bash
docker-compose run --rm app python manage.py loaddata /app/fixtures/initial.json
```

and try again.
