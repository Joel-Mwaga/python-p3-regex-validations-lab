import re

# Allow for names like D'Angelo (single uppercase letter after apostrophe)
# Fix: allow for just one uppercase letter after apostrophe/hyphen/space
name = r"^[A-Z][a-z]*(?:[ '-][A-Z][a-z]*)*$"
name_regex = re.compile(name)

phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

email_address = r"^[a-z]+(?:\.[a-z0-9]+)*@[a-z]+\.[a-z]+$"
email_regex = re.compile(email_address)
