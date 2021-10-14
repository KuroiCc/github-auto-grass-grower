from typing import Any
from datetime import datetime
from random import random
import sys


class HumanLikeCommit():
    def __init__(self, path: str, human_like: bool = True) -> None:
        self.path = path
        self.human_like = human_like
        self.__call__()

    def __call__(self) -> Any:
        # self.record()
        pass

    def human_like_record(self) -> Any:
        if not self.human_like:
            return self.record()

        last_row = "row"
        status = last_row[0:4]

        if status == "work":
            # num_of_day_worked = 1
            pass
        elif status == "off*":
            num_of_day_off = 1
            if self.__is_record_after_n_days_off(n=num_of_day_off):
                self.record(self.__now() + "work from" + self.__now())
        else:
            self.record()

    def record(self, text: str) -> Any:
        """
        write record to text file at self.path.
        """
        with open(self.path, "a") as file:
            file.write(text)

    def __is_record_after_n_days_off(self, n: int) -> bool:
        """
        今まで休んだ日数 (n) に基づいて、今日recordするかどうか (True or False) を返す。
        マジックナンバー a = 0.7, k = 1/4 を使うと次の確率でrecordする:2日目0.250、3日目で0.406、4日目で0.539、5日目で0.660、6日目で0.771、7日目で0.876、8日目で0.976、9日目で1.072。
        """
        record_probability = self.__power_func(n, 0.7, 1 / 4)
        return random() <= record_probability

    def __power_func(self, x: float, a: float = 1, k: float = 1, b: float = 0) -> float:
        """
        y = kx^a + b
        """
        return k * x**a + b

    def __now(self):
        return datetime.now().strftime("%Y-%m-%d %X")


if __name__ == "__main__":
    path = sys.argv[-1]

    HumanLikeCommit(path="aa")
