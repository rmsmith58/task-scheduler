class task:
    name = ''
    date = ''
    category = ''
    def __init__(self, title, date, category):
        self.name = title
        self.date = date
        self.category = category

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getCategory(self):
        return self.category

    def display(self):
        return '%s %s %s' % (self.getName(), self.getDate(), self.getCategory())
        
