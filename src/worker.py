from threading import Thread
from queue import Queue
from typing import List
import logging

from src.define import LabelArgs
from src.label import Label
from src.printer import Printer


class Worker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._queue: Queue[List[LabelArgs]] = Queue()
        self._label = Label()
        self._printer = Printer()
        self.start()
        logging.info("Worker started")

    def run(self):
        while True:
            task = self._queue.get()
            for label_args in task:
                logging.info(
                    f"Printing {label_args.order_id} {label_args.index[0]}/{label_args.index[1]}"
                )
                im = self._label.make(label_args)
                self._printer.print(im.tobytes())
            self._queue.task_done()

    def add(self, data: List[LabelArgs]):
        self._queue.put(data)
