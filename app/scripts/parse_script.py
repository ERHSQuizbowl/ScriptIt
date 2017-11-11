class ParseScript:
    def __init__(self, file):
        self.file = file

    # parse the file and say every line except the name
    def parse(self, name):
        input_file = open(self.file)
        for line in input_file:
            print(line)
