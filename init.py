import logging
import logging.handlers


class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            import string  # for tls add this line
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                self.fromaddr,
                self.toaddrs,
                self.getSubject(record),
                formatdate(), msg)
            if self.username:
                smtp.ehlo()
                smtp.starttls()  # for tls add this line
                smtp.ehlo()  # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


logger = logging.getLogger()

gm = TlsSMTPHandler(("smtp.gmail.com", 587), fromaddr='bibvad@gmail.com', 'Error found!',
                    (toaddr='bibvad@gmail.com', 'qoadpjypdywgnakc'))
gm.setLevel(logging.ERROR)

logger.addHandler(gm)

try:
    1 / 0
except:
    logger.exception('FFFFFFFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUU-')
