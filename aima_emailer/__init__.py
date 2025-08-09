from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s : %(levelname)s : %(name)s:%(lineno)d: %(message)s",
)
log = logging.getLogger(__name__)

RESEND_API_KEY = getenv("RESEND_API_KEY")

if not RESEND_API_KEY:
    raise ValueError("RESEND_API_KEY is not set")

__all__ = [
    "RESEND_API_KEY",
]

log.info("AIMA Emailer initialized")
