from PO_demo.index_page import IndexPage

class TestWX:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        #self.index.goto_login().goto_register()

        self.index.goto_register().register()