class SearchPage:

    context = None

    def __init__(self, context):
        self.context = context

    def search_term(self, search_term):
        self.context.driver.find_element_by_xpath("//textarea[@id='APjFqb']").send_keys(search_term)
        self.context.driver.find_element_by_xpath("(//input[@name='btnK'])").click()

    def get_element_matching_text(self, search_result):
        return self.context.driver.find_element_by_xpath("//*/h3[contains(.,'{}')]".format(search_result))
