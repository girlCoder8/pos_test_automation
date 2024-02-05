from .context import payment_processor

import unittest


class StripeTestAccount(unittest.TestCase):
    def test_is_paid(self):
        pay = payment_processor.PaymentProcessor()
        pay.setup()
        self.assertTrue(pay.is_paid("your_stripe_number"))
