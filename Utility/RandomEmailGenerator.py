import os
import random
from Utility.common_cache import CommonCache


class RandomEmailGenerator:
    def __init__(self):
        self.email_domain = os.getenv("TEST_EMAIL_DOMAIN", "example.test")
        if "@" in self.email_domain:
            self.email_domain = self.email_domain.split("@", 1)[1]

    def generate_random_email(self):
        random_integer = random.randint(1, 99999)
        random_email = f"test+{random_integer}@{self.email_domain}"
        CommonCache.set_email(random_email)
        return random_email

# rand_email = RandomEmailGenerator()
# config.email = rand_email.generate_random_email()


# def random_email_gen():
#     # random email generator
#     random_integer = random.randint(1, 99999)
#     # Use a non-production domain for generated test accounts.
#     email = "test@example.test"
#     # Split the email address into local part and domain
#     local_part, domain = email.split("@")
#     # Append the random integer to the local part
#     random_email = f"{local_part}+{random_integer}@{domain}"
#     return random_email
