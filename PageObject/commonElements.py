class CommonElements():

    def __init__(self, page):
        self.page = page
        self._toastMessage = page.locator("div#toast-container")

    def getToastMessage(self):
        return self._toastMessage