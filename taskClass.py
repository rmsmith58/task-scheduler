class task:
    name = ''
    date = ''
    remind = ''
    def __init__(self, title, date, remind):
        self.name = title
        self.date = date
        self.remind = remind

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getRemind(self):
        return self.remind

    def display(self):
        print('%s %s %s' % (self.getName, self.getDate, self.getRemind))
        
