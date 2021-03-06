class Map:
    def __init__(self):
        self._rules = []

    def add_rule(self, endpoint, slave_ids, function_codes, addresses, starting_address=None, quantities=None):
        self._rules.append(DataRule(endpoint, slave_ids, function_codes,
                                    addresses, starting_address, quantities))

    def match(self, slave_id, function_code, address, starting_address, quantity):
        for rule in self._rules:
            if rule.match(slave_id, function_code, address, starting_address, quantity):
                return rule.endpoint


class DataRule:
    def __init__(self, endpoint, slave_ids, function_codes, addresses, starting_address, quantities):
        self.endpoint = endpoint
        self.slave_ids = slave_ids
        self.function_codes = function_codes
        self.addresses = addresses
        self.starting_address = starting_address
        self.quantities = quantities

    def match(self, slave_id, function_code, address, starting_address, quantity):
        if slave_id in self.slave_ids and \
            function_code in self.function_codes and \
            (True if self.starting_address is None else starting_address == self.starting_address) and \
            (True if self.quantities is None else quantity in self.quantities) and \
                address in self.addresses:
            return True

        return False
