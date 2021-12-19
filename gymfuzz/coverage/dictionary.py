class Dictionary:
    def __init__(self, config):
        self.config = config
        self.content = []

        # add each token in config['tokens']
        for t in self.config['tokens']:
            self.content.append(t)
        
        # config['bytes'] is boolean
        if self.config['bytes']:
            for b in range(256):
                self.content.append(bytes([b]))

    def size(self):
        return len(self.content) + 1

    def eof(self):
        return len(self.content)

    def bytes(self, i):
        if i >= len(self.content):
            return b""
        else:
            return self.content[i]
