class Logger(object):

    hash_set = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.hash_set:
            last = self.hash_set[message]
            if timestamp - last >= 10:
                self.hash_set[message] = timestamp
                return True
            else:
                return False
        else:
            self.hash_set[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
