# -*- coding: utf-8 -*-
import logging
import logging.handlers

class BufferingSMTPHandler(logging.handlers.BufferingHandler):
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials, capacity):
        logging.handlers.BufferingHandler.__init__(self, capacity)
        self.mailhost, self.mailport = mailhost
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.subject = subject
        self.username, self.password = credentials
        self.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5s %(message)s"))

    def flush(self):
        if len(self.buffer) > 0:
            try:
                import smtplib
                from email.utils import formatdate
                port = self.mailport
                if not port:
                    port = smtplib.SMTP_PORT
                smtp = smtplib.SMTP(self.mailhost, port)
                msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (
                    self.fromaddr, ",".join(self.toaddrs), self.subject
                )
                for record in self.buffer:
                    s = self.format(record)
                    msg = msg + s + "\r\n"
                if self.username:
                    smtp.ehlo()  # for tls add this line
                    smtp.starttls()  # for tls add this line
                    smtp.ehlo()  # for tls add this line
                    smtp.login(self.username, self.password)
                smtp.sendmail(self.fromaddr, self.toaddrs, msg)
                smtp.quit()
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception:
                self.handleError(None)  # no particular record
            self.buffer = []





logger = logging.getLogger()

#smtp_handler = BufferingSMTPHandler(**params)
smtp_handler = BufferingSMTPHandler\
        (
    mailhost=("smtp.gmail.com", 587),
    fromaddr='bibvad@gmail.com',
    toaddrs=['bibvad@mail.ru'],
    subject='Error!',
    credentials=('bibvad@gmail.com', 'qoadpjypdywgnakc'),
    capacity=60
)
smtp_handler.setLevel(logging.DEBUG)
logger.addHandler(smtp_handler)

logger.error('Error-error-error')
