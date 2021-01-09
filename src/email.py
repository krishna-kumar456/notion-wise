import os
import yagmail

from .random_notes import get_content
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_pwd = os.getenv('SENDER_PWD')
to_address = os.getenv('TO_ADDRESS')

def send_email():
  """ Helper method to send notification to
  configured email address.

  Args:
    sender_cred:
      SMTP credentials to send emails.
    to_address:
      Recevier email address.
    payload:
      Body Content for the email. Should contain randomly selected
      notes from Notion
  
  Returns:
    A success message if email has been sent correctly.
  """
  payload = get_content()

  if payload == {} or payload == None:
    raise Exception("Payload cannot be empty.")

  kl_rand_source, kl_rand_title = list(payload['kl'].items())[0]
  kh_rand_source, kh_rand_title = list(payload['kh'].items())[0]

  html = f"""\
  <html>
    <body>
      <p>Here's some Serependity<br>
        <br>
        <a href="{kl_rand_source}">{kl_rand_title}</a> 
        <br>
        <a href="{kh_rand_source}">{kh_rand_title}</a> 
      </p>
    </body>
  </html>
  """

  result = None 

  try:
    yag = yagmail.SMTP(sender_email, sender_pwd)    
    yag.send(
        to=to_address,
        subject="Bonjour from NotionWise!",
        contents=html, 
    )
    result = "success"
  except e:
    result = "failed"

  return result


