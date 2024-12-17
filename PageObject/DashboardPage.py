from playwright.sync_api import expect
from playwright.sync_api import Page


class DashboardPage():

    def __init__(self, page: Page):
        self.page = page
        self._homeBtn = page.get_by_role("button", name="HOME")
        self._logoHeader = page.locator(".logo h3")
        self._ordersBtn = page.get_by_role("button", name="ORDERS")

    @property
    def getHomeButton(self):
        return self._homeBtn

    @property
    def getLogoHeader(self):
        return self._logoHeader

    def getOrdersButton(self):
        return self._ordersBtn

    def verify_homebutton_appHeader(self):
        expect(self.getHomeButton).to_be_visible()
        expect(self.getLogoHeader).to_be_visible()
        print("Verification Completed and Login is Successful!!")
