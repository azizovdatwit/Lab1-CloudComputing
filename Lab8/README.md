Docker Compose Setup: MinIO, Postfix Email Server, MailHog, Redis

This Docker Compose provides:

- MinIO:  object storage.
- Postfix: Local SMTP server for testing email delivery.
- MailHog: Email testing tool with web UI to catch outgoing messages.
- Redis: In-memory key-value data store.

## Setup & Run

1. Clone the repo or copy the `docker-compose.yml` file.
2. Start the stack:
   ```bash
   docker-compose up -d
   ```
3. Access services by following instructions below.

---

# Services

### MinIO
- Web Console: [http://localhost:9001]
- Credentials:  
  - Username: `minioadmin`  
  - Password: `minioadmin`
You can also store images if you would like

### Postfix
- Acts as a local SMTP server for testing.
- Relays mail to MailHog.

Ports exposed:
- `1587`: SMTPS
- `2525`: SMTP

To access the container:
```
docker exec -it postfix /bin/sh
```

Set up Postfix relay manually (if needed):
```bash
echo "relayhost = [mailhog]:1025" >> /etc/postfix/main.cf
```

Send a test email:
```bash
echo "Hello MailHog" | sendmail testuser@dummy.dev
```

###  MailHog
- Catches and displays emails sent by Postfix.
- Web UI: [http://localhost:8025]

Ports exposed:
- `8025`: Web UI
- `2025`: SMTP

### Redis
- Default Redis setup on port `6379`.
- To test, run 'docker logs redis' or 'docker exec -it redis redis-cli ping'. 

---

Note: there is test2.py file where I used google smtp server to send an email to myself. 
If you'd like to run this you need to generate an App password for your google account and use that as login parameters.
To generate an app password, follow the instructions on here:  https://support.google.com/mail/answer/185833?hl=en
Side note, You can't generate unless you has 2FA enabled. The name of the app on Gmail itself doesn't really matter, 
you only need the password so that you can pass it into server.login. 
