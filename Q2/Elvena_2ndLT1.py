class Publication:
  def __init__(self, title, author):
     self.title = title
        self.author = author


    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Magazine (Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number


    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)


magazine1 = Magazine("Tech Today", "Mia Santos", 12)
magazine1.display_info()


