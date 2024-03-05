class level:
    levels = ["نقش جهان - اصفهان", "تخت جمشید - استان فارس", "حرم حضرت شاهچراغ - شیراز"]
    def __init__(self, name:str, index:int, lock:bool) -> None:
        self.name = name
        self.index = index
        self.lock = lock
        self.place = self.levels[index-1]