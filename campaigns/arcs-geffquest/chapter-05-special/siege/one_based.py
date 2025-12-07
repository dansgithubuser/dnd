class OneBasedList(list):
    def __getitem__(self, i):
        assert 1 <= i <= len(self)
        return super().__getitem__(i - 1)

    def __str__(self):
        return '\n'.join(f'{i+1}: {v}' for i, v in enumerate(self))
