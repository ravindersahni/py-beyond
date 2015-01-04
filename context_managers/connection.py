__author__ = 'instancetype'


class Connection:

    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('starting transaction', self.xid)
        result = self.xid
        self.xid = self.xid + 1
        return result

    def _commit_transaction(self, xid):
        print('commiting transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)