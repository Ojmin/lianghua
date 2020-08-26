import redis
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

from spider import JISILUConvertibleBond


class BondPremium(tk.Tk):
    def __init__(self):
        super(BondPremium, self).__init__()
        self.spider = JISILUConvertibleBond()
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.root = tk.Tk()
        self.fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasTkAgg(self.fig, self.root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.root.mainloop()

    def get_result(self):
        print(1)
        rows = self.spider.get_result()
        row_list = []
        for row in rows:
            premium_rt = float(row["cell"]["premium_rt"].strip("%")) / 100
            if row["cell"]["convert_cd"] != "未到转股期" and premium_rt < -0.01:
                row_list.append(row)
        sorted(row_list, key=lambda x: float(x["cell"]["premium_rt"].strip("%")))
        premium_rate = float(row_list[0]["cell"]["premium"].strip("%")) / 100
        mytime = row_list[0]["cell"]["price_tips"]
        bond_id = row_list[0]["cell"]["bond_id"]
        self.r.hmset(bond_id, {mytime: premium_rate})

    def refresh_data(self, wait_time=1000):
        # 需要刷新数据的操作
        # 代码...
        self.get_result()

        self.after(wait_time, self.refresh_data)  # 这里的10000单位为毫秒


if __name__ == '__main__':
    BondPremium().refresh_data()
