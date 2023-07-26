import win32com.client
import re
import ctypes
from ctypes import wintypes
import logging

from src.define import IS_DEBUG

PRINTER_COMMANDS = [
    """SIZE 38.5 mm, 30 mm
SET RIBBON OFF
DIRECTION 0,0
REFERENCE 0,0
OFFSET 0 mm
SET PEEL OFF
SET CUTTER OFF
SET TEAR ON
CLS 
BITMAP 0,0,40,240,1,""",
    """
PRINT 1,1
""",
]
IMAGE_BUFFER_SIZE = 9600


class Printer:
    def __init__(self):
        if IS_DEBUG:
            return
        vid, pid = self._getPrinterVidPid()

        if vid is None or pid is None:
            raise Exception("找不到列印支援裝置")

        self._handle = ctypes.WinDLL("./jsprinter_64.dll")
        self._device = self._handle.uniOpenUsbByVidPid(
            ctypes.c_int(int(vid, 16)),
            ctypes.c_int(int(pid, 16)),
        )

        if self._device < 0:
            raise Exception("無法連接列印機")

    def _getPrinterVidPid(self):
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            if "列印支援" in usb.Name or "Xprinter" in usb.Name:
                match = re.search(
                    r"VID_(?P<vid>[0-9A-F]{4})&PID_(?P<pid>[0-9A-F]{4})",
                    usb.DeviceID,
                )
                if match:
                    return match.group("vid"), match.group("pid")
        raise Exception("找不到列印支援裝置")

    def print(self, buffer: bytes):
        if IS_DEBUG:
            logging.debug(f"Print: {len(buffer)} bytes")
            return

        if len(buffer) != IMAGE_BUFFER_SIZE:
            raise Exception(
                f"buffer長度不正確: {len(buffer)} != {IMAGE_BUFFER_SIZE}"
            )

        msg = PRINTER_COMMANDS[0].encode()
        msg += buffer
        msg += PRINTER_COMMANDS[1].encode()
        cmd = ctypes.c_char_p(msg)
        size = wintypes.DWORD(len(msg))
        self._handle.uniWrite(self._device, cmd, size)

    def close(self):
        self._handle.uniClose(self._device)
