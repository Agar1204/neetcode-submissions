class BrowserHistory:  
    def __init__(self, homepage: str):
        self.i = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if self.i < len(self.history)-1:
            self.history = self.history[:self.i + 1]
        self.history.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(len(self.history)-1, self.i + steps)
        return self.history[self.i]