from PIL import Image, ImageFont, ImageDraw
import numpy as np
from datetime import timedelta

from src.define import LabelArgs, IS_DEBUG

WIDTH = 320
HEIGHT = 240

GLOBAL_PADDING = 10

ORDER_PADDING = 5
TITLE_HEIGHT = 45

META_HEIGHT = 25
META_PADDING = 5
DATE_HEIGHT = 18
USER_HEIGHT = 22

NAME_HEIGHT = 45
OPTIONS_HEIGHT = 25


class Label:
    def __init__(self):
        self._font_order = ImageFont.truetype(
            "fonts/JetBrainsMono-Bold.ttf", TITLE_HEIGHT - ORDER_PADDING
        )
        self._font_date = ImageFont.truetype(
            "fonts/JetBrainsMono-Regular.ttf", DATE_HEIGHT
        )
        self._font_index = ImageFont.truetype(
            "fonts/JetBrainsMono-Regular.ttf", TITLE_HEIGHT - ORDER_PADDING - 10
        )
        self._font_name = ImageFont.truetype(
            "fonts/NotoSansTC-Bold.otf", NAME_HEIGHT
        )
        self._font_options = ImageFont.truetype(
            "fonts/NotoSansTC-Regular.otf", OPTIONS_HEIGHT
        )
        self._font_user = ImageFont.truetype(
            "fonts/NotoSansTC-Regular.otf", DATE_HEIGHT
        )

    def make(
        self,
        args: LabelArgs,
    ):
        im = Image.new("1", (WIDTH, HEIGHT), 255)
        draw = ImageDraw.Draw(im)
        cursorY = GLOBAL_PADDING

        # [Title]
        # Order ID
        order_text = f"#{args.order_id}"
        optb = self._font_order.getbbox(order_text)
        ot_w = optb[2] - optb[0]
        ot_h = optb[3] - optb[1]
        ot_x = optb[0]
        ot_y = optb[1]
        draw.rectangle(
            (
                GLOBAL_PADDING,
                cursorY,
                GLOBAL_PADDING + ot_w + ORDER_PADDING * 2,
                cursorY + TITLE_HEIGHT,
            ),
            fill=0,
        )
        draw.text(
            (
                GLOBAL_PADDING - ot_x + ORDER_PADDING,
                cursorY - ot_y + TITLE_HEIGHT / 2 - ot_h / 2,
            ),
            order_text,
            font=self._font_order,
            fill=255,
        )

        # Index
        index_text = f"{args.index[0]}/{args.index[1]}"
        itb = self._font_index.getbbox(index_text)
        it_w = itb[2] - itb[0]
        it_h = itb[3] - itb[1]
        it_x = itb[0]
        it_y = itb[1]
        draw.text(
            (
                WIDTH - GLOBAL_PADDING - it_x - it_w,
                cursorY - it_y + TITLE_HEIGHT / 2 - it_h / 2,
            ),
            index_text,
            font=self._font_index,
            fill=0,
        )

        # [Meta]
        # Date
        cursorY += TITLE_HEIGHT
        date_text = (args.date + timedelta(hours=8)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        dtb = self._font_date.getbbox(date_text)
        dt_h = dtb[3] - dtb[1]
        dt_x = dtb[0]
        dt_y = dtb[1]
        draw.text(
            (
                GLOBAL_PADDING + META_PADDING - dt_x,
                cursorY - dt_y + META_HEIGHT / 2 - dt_h / 2,
            ),
            date_text,
            font=self._font_date,
            fill=0,
        )

        # [User]
        utb = self._font_user.getbbox(args.user)
        ut_w = utb[2] - utb[0]
        ut_h = utb[3] - utb[1]
        ut_x = utb[0]
        ut_y = utb[1]
        draw.text(
            (
                WIDTH - GLOBAL_PADDING - META_PADDING - ut_x - ut_w,
                cursorY - ut_y + META_HEIGHT / 2 - ut_h / 2,
            ),
            args.user,
            font=self._font_user,
            fill=0,
        )
        draw.rectangle(
            (
                GLOBAL_PADDING,
                cursorY,
                WIDTH - GLOBAL_PADDING,
                cursorY + META_HEIGHT,
            ),
            outline=0,
        )

        # [Name]
        cursorY += META_HEIGHT + 10
        ntb = self._font_name.getbbox(args.name)
        nt_h = ntb[3] - ntb[1]
        nt_x = ntb[0]
        nt_y = ntb[1]
        draw.text(
            (
                GLOBAL_PADDING - nt_x,
                cursorY - nt_y + NAME_HEIGHT / 2 - nt_h / 2,
            ),
            args.name,
            font=self._font_name,
            fill=0,
        )

        # [Options]
        cursorY += NAME_HEIGHT + 10
        option_texts = [""]
        for option in args.options:
            concat_text = (
                option_texts[-1] + " / " + option
                if option_texts[-1] != ""
                else option
            )
            ctb = self._font_options.getbbox(concat_text)
            ct_w = ctb[2] - ctb[0]
            if ct_w > WIDTH - GLOBAL_PADDING * 2:
                option_texts.append(option)
            else:
                option_texts[-1] = concat_text

        for option_text in option_texts:
            optb = self._font_options.getbbox(option_text)
            opt_h = optb[3] - optb[1]
            opt_x = optb[0]
            opt_y = optb[1]
            draw.text(
                (
                    GLOBAL_PADDING - opt_x,
                    cursorY - opt_y + OPTIONS_HEIGHT / 2 - opt_h / 2,
                ),
                option_text,
                font=self._font_options,
                fill=0,
            )
            cursorY += OPTIONS_HEIGHT + 5

        if IS_DEBUG:
            im.show()

        return np.packbits(
            np.array(
                im.rotate(180),
            ).flatten()
        )
