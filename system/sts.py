from portfolio._portfolio_construction_model import PortfolioConstructionModel


class SimTradingSystem(object):
    """Simulated trading system which connects strategies, risk models, cost/slippage model,
    portfolio model, and 'execution' model."""
    def __init__(self, **kwargs):
        # TODO: figure out parameters and initialize
        pass

    def _create_order_sizer(self, **kwargs):
        # TODO: create order_sizer based on 'long_only' parameter and order_sizer classes
        # order_sizer = some class created
        pass

    def _initialize_models(self, **kwargs):
        """Initialises the portfolio construction and execution models for the simulated
        trading strategy."""

        order_sizer = self.create_order_sizer()

    def __call__(self, dt, stats = None):
        """Construct the portfolio and (optionally) execute the orders
        with the broker.
        Parameters:
        dt : `pd.Timestamp`:= current time"""
        # Construct the target portfolio
        # TODO: implement portfolio construction model
        balance_orders = self.portfolio_construction_model(dt, stats=stats)

        # Execute the orders
        self.execution_handler(dt, balance_orders)