import uuid
import numpy as np
from datetime import datetime

class Order(object):
    def __init__(self, dt, asset, quantity, side, commission=0.0, order_id=None):
        self.created_dt = dt
        self.cur_dt = dt
        self.asset = asset
        self.quantity = quantity
        self.commission = commission
        self.side = side
        self.order_id = self._set_or_generate_order_id(order_id)

    def __repr__(self):
        """ Output a string representation of the object"""
        return (
                "Order(dt='%s', asset='%s', quantity=%s, "
                "commission=%s, side=%s, order_id=%s)" % (
                    self.created_dt, self.asset, self.quantity,
                    self.commission, self.side, self.order_id
                )
        )

    def _set_or_generate_order_id(self, order_id=None):
        """ Sets or generates a UUID order ID for the order"""
        if order_id is None:
            return uuid.uuid4().hex
        else:
            return order_id
