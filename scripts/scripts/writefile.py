from typing import Any
from datetime import datetime
from random import random
import sys


class HumanLikeCommit():
    """
    人間みたいにrecordをする。毎日ではなく人間ぽっく休みも挟む。
    path:           file path for record.
    human_like:     Ture to records human likily,  False to records evetry time.
    """
    __DATE_FORMATE = "%Y-%m-%d %X"

    def __init__(self, path: str, human_like: bool = True) -> None:
        self.path = path
        self.human_like = human_like
        self.__call__()

    def __call__(self) -> Any:
        self.human_like_record()

        # test = "off***  "
        # test2 = "commit  "
        # for i in range(1, 5):
        #     test += "%d日目で%-0.3f, " % (i + 1, self.__nverse_proportional_like_func(x=i, k=-1, a=1.1, b=1, c=1))
        #     test2 += "%d日目で%-0.3f, " % (i + 1, self.__nverse_proportional_like_func(x=i, k=1.1, a=0.2, b=1))
        # test2 += "%d日目で%-0.3f, " % (10, self.__nverse_proportional_like_func(x=9, k=1.1, a=0.2, b=1))
        # test2 += "%d日目で%-0.3f, " % (30, self.__nverse_proportional_like_func(x=29, k=1.1, a=0.2, b=1))

        # print(test, "\n", test2)
        # print(self.__now())

    def human_like_record(self) -> Any:
        """
        record text like:
        2021-10-15 14:59:21 commit from 2021-10-15 14:59:21
        2021-10-16 14:59:21 off***
        """
        commit_text = self.__now() + " commit from " + self.__now() + "\n"
        if not self.human_like:
            return self.record(commit_text)

        with open(self.path) as file:
            lines = file.readlines()
            last_line = lines[-1][:-1]

        status = last_line[20:26]

        try:
            if status == "commit":

                index_from = len(self.__now()) + len(" commit from ")
                num_of_day_commited = self.__get_interval_day(
                    last_line[index_from:index_from + len(self.__now())]  # 連続recordの最初の日
                )

                if self.__is_record_after_n_days_commit(num_of_day_commited):
                    self.record(commit_text)
                else:
                    self.record(self.__now() + " off***" + "\n")

            elif status == "off***":

                index_to = len(self.__now())
                num_of_day_off = self.__get_interval_day(last_line[:index_to]) - 1

                if self.__is_record_after_n_days_off(num_of_day_off):
                    self.record(commit_text)

            else:
                self.record(commit_text)
        except ZeroDivisionError:
            return
        except BaseException:
            self.record(commit_text)

    def __get_interval_day(self, date: str) -> int:
        from_date = datetime.strptime(date, HumanLikeCommit.__DATE_FORMATE)
        return (datetime.now() - from_date).days

    def record(self, text: str) -> Any:
        """
        write record to text file at self.path.
        """
        with open(self.path, "a") as file:
            file.write(text)

    def __is_record_after_n_days_off(self, n: int) -> bool:
        """
        連続して休んだ日数 (n >= 1) に基づいて、今日recordするかどうか (True or False) を返す。
        マジックナンバー k=-1, a=1.1, b=1, c=1 を使うと次の確率でrecordする:2日目で0.524, 3日目で0.688, 4日目で0.767, 5日目で0.815。
        """
        if n == 0:
            raise ZeroDivisionError
        elif n < 1:
            return True
        record_probability = self.__nverse_proportional_like_func(x=n, k=-1.5, a=1.1, b=1, c=1)  # yapf: disable
        return random() <= record_probability

    def __is_record_after_n_days_commit(self, n: int) -> bool:
        """
        連続してコミットがある日数 (n >= 1) に基づいて、今日recordするかどうか (True or False) を返す。
        マジックナンバー x=n, k=1.1, a=0.2, b=1 を使うと次の確率でrecordする:2日目で0.917, 3日目で0.786, 4日目で0.688, 5日目で0.611, 10日目で0.393, 30日目で0.162。
        """
        if n == 0:
            raise ZeroDivisionError
        elif n < 1:
            return True
        record_probability = self.__nverse_proportional_like_func(x=n, k=1.1, a=0.2, b=1)
        return random() <= record_probability

    def __nverse_proportional_like_func(
        self,
        x: float,
        k: float = 1,
        a: float = 1,
        b: float = 0,
        c: float = 0,
    ) -> float:
        """
        y = k / (ax + b) + c, (ax + b != 0)
        """
        return k / (a * x + b) + c

    def __now(self):
        return datetime.now().strftime(HumanLikeCommit.__DATE_FORMATE)


if __name__ == "__main__":
    path = sys.argv[-1]

    HumanLikeCommit(path="./test/records.txt")

    # for i in range(30):
    #     HumanLikeCommit(path="./test/records.txt")
