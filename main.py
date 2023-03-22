from printer import Printer
from label import Label
from datetime import datetime

if __name__ == "__main__":
    label = Label()
    im = label.make(
        1565889,
        datetime.now(),
        (1, 3),
        "麥香雞腿堡",
        ["大份", "加蛋", "加醬", "加洋蔥", "加生菜"],
        "洪健淇",
        # debug=True,
    )

    if im is not None:
        printer = Printer()
        printer.print(im.tobytes())
