import resend
from logging import getLogger
from aima_emailer import RESEND_API_KEY
from aima_emailer.template import generate_email_html
from os import path
import click

log = getLogger(__name__)


@click.command()
@click.option("--full-name", type=str, help="Full name of the person", required=True)
@click.option(
    "--nationality", type=str, help="Nationality of the person", required=True
)
@click.option(
    "--appointment-date", type=str, help="Date of the appointment", required=True
)
@click.option(
    "--service-location", type=str, help="Location of the service", required=True
)
@click.option(
    "--passport-number", type=str, help="Passport number of the person", required=True
)
@click.option(
    "--correct-address", type=str, help="Correct address of the person", required=True
)
@click.option(
    "--contact-number", type=str, help="Contact number of the person", required=True
)
@click.option(
    "--from-email", type=str, help="Email address of the sender", required=True
)
@click.option(
    "--to-email",
    type=str,
    help="Email address of the recipient",
    default="aima@aima.gov.pt",
    required=True,
)
@click.option(
    "--subject",
    type=str,
    help="Subject of the email",
    default="Pedido de Atualização de Morada",
    required=True,
)
@click.option(
    "--attachment",
    type=str,
    help="Attachment file path to be sent",
    required=True,
    multiple=True,
)
def send(
    full_name,
    nationality,
    appointment_date,
    service_location,
    passport_number,
    correct_address,
    contact_number,
    from_email,
    to_email,
    subject,
    attachment,
):
    resend.api_key = RESEND_API_KEY

    log.info("Generating email HTML")
    html = generate_email_html(
        full_name=full_name,
        nationality=nationality,
        appointment_date=appointment_date,
        service_location=service_location,
        passport_number=passport_number,
        correct_address=correct_address,
        contact_number=contact_number,
    )
    log.info("Email HTML generated")

    log.info("Loading attachments")
    attachments: list[resend.Attachment] = []
    for attachment_path in attachment:
        log.info(f"Loading attachment: {attachment_path}")
        f: bytes = open(path.abspath(attachment_path), "rb").read()
        attachment: resend.Attachment = {
            "content": list(f),
            "filename": attachment_path.split("/")[-1],
        }
        attachments.append(attachment)

    log.info("Attachments loaded")

    log.info("Configuring email parameters")
    params: resend.Emails.SendParams = {
        "from": from_email,
        "to": to_email,
        "subject": subject,
        "html": html,
        "attachments": attachments,
    }
    log.info("Email parameters configured")

    log.info("Sending email")
    resend.Emails.send(params)
    log.info("Email sent")


if __name__ == "__main__":
    send()
