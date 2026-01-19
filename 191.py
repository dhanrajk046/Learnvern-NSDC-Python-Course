class RBI:
    def interest(self):
        """Base method to be overridden by bank classes."""
        raise NotImplementedError("Subclasses should implement this method")


class SBI(RBI):
    def interest(self):
        print('SBI Interest is 5%')


class HDFC(RBI):
    def interest(self):
        print('HDFC Interest is 2%')


if __name__ == '__main__':
    s = SBI()
    h = HDFC()
    s.interest()
    h.interest()