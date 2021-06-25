# Модуль для вычисления количества приседаний
from scrollLabel import ScrollLabel
# Здесь должен быть твой код
class Sits(ScrollLabel):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        text = "Осталось приседаний: [b]" + str(self.total) + "[/b]"
        super().__init__(text, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        text = "Осталось приседаний: [b]" + str(remain) + "[/b]"
        super().set_text(text)