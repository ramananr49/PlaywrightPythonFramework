from playwright.sync_api import Page


class CommonElements():

    def __init__(self, page: Page):
        self.page = page
        self._toastMessage = page.locator("div#toast-container")

    def getToastMessage(self):
        return self._toastMessage