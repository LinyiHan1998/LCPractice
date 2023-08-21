class PnLCalculator:
    def __init__(self):
        self.price = {}
        self.trade = {}
    def process_trade(self,trade_id,instrument_id,buy_sell,price,volume):
        if instrument_id in self.trade:
            self.trade[instrument_id].append((buy_sell,price,volume,trade_id))
        else:
            self.trade[instrument_id] = [(buy_sell,price,volume,trade_id)]
    def process_price_update(self, instrument_id, price):
        self.price[instrument_id] = price
    def output_worst_trade(self, instrument_id):
        min_diff,res = 0,"NO BAD TRADER"
        for buy_sell,price,volume,trader_id in self.trade[instrument_id]:
            if buy_sell == 'BUY':
                diff = (self.price[instrument_id] - price) * volume
            else:
                diff = (price-self.price[instrument_id])*volume
            if diff<min_diff:
                min_diff = diff
                res = trader_id
        return res