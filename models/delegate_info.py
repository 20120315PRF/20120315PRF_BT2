## Creates a delegate info object factory
class DelegateInfoFactory:

    def generateDelegate (self, name):
        delegate = {}
        delegate['name'] = name
        delegate['position'] = '--'
        delegate['uptime'] = '--'
        delegate['approval'] = '--'
        delegate['status'] = DelegateInfoStatus.STATUS_NOT_FOUND
        return delegate

class DelegateInfoStatus:
    ## Delegates status
    STATUS_NOT_FORGING = "Not forging"
    STATUS_CYCLE_LOST = "Cycle lost"
    STATUS_FORGING = "Forging"
    STATUS_NOT_FOUND = "Not found in top"