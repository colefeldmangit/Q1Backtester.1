import unittest
from execution.order import Order
from datetime import datetime

order = Order(dt=datetime.now(), asset='LLNW', quantity=100, side='BUY')


class generic_order_test(unittest.TestCase):
    def test_order_id(self):
        self.assertNotEqual(order.order_id, None)


if __name__ == '__main__':
    unittest.main()
