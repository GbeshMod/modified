"""Generic progress_callback for Modified upload.py and download.py"""
import time
import math
import random
from .bytesformat import *
from .exceptions import CancelProcess
from ..function import edit_or_reply

pro_load = [
  progressfz,
  progressp, 
  progressx, 
  progress_old, 
  progressf, 
  progressv, 
  progressl, 
  progressj,
  ]



progress = random.choice(pro_load)


async def progressfz(current, total, event, start, prog_type, file_name=None, is_cancelled=False):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if 'upload' in prog_type.lower():
            status = 'Uploading'
        elif 'download' in prog_type.lower():
            status = 'Downloading'
        else:
            status = 'Unknown'
        progress_str = "`{0}` | [{1}{2}] `{3}%`".format(
            status,
            ''.join(["■" for i in range(
                    math.floor(percentage / 10))]),
            ''.join(["▨" for i in range(
                    10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = "{}\n`{} of {} @ {}`\n`ETA` ➺ {}\n`Duration` ➺ {}".format(progress_str, humanbytes(current), humanbytes(total), humanbytes(speed), time_formatter(eta), time_formatter(elapsed_time))
        await event.edit(f"`{prog_type}`\n\n"
                          f"`Status`\n{tmp}")


async def progressp(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["❂" for i in range(math.floor(percentage / 10))]),
            ''.join(["⊚" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA➻ {2}".format(humanbytes(current), humanbytes(total), time_formatter(estimated_total_time))
        if file_name:
            await event.edit("{}\nFile Name ➫  `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


async def progressx(current, total, event, start, prog_type, file_name=None, is_cancelled=False):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if 'upload' in prog_type.lower():
            status = 'Uploading'
        elif 'download' in prog_type.lower():
            status = 'Downloading'
        else:
            status = 'Unknown'
        progress_str = "`{0}` | [{1}{2}] `{3}%`".format(
            status,
            ''.join(["✦" for i in range(
                    math.floor(percentage / 10))]),
            ''.join(["✧" for i in range(
                    10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = "{}\n`{} of {} @ {}`\n`ETA` ➬  {}\n`Duration` ➬  {}".format(progress_str, humanbytes(current), humanbytes(total), humanbytes(speed), time_formatter(eta), time_formatter(elapsed_time))
        await event.edit(f"`{prog_type}`\n\n"
                          f"`Status`\n{tmp}")


async def progress_old(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress ➻ {2}%\n".format(
            "".join(["█" for i in range(math.floor(percentage / 5))]),
            "".join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA ➻ {2}".format(humanbytes(current), humanbytes(total), time_formatter(estimated_total_time))
        if file_name:
            await event.edit("{}\nFile Name ➻ `{}`\n{}".format(type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


async def progressf(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current != total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            "".join(["■" for i in range(math.floor(percentage / 5))]),
            "".join(["▢" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA ➻ {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit("{}\nFile Name ➻ `{}`\n{}".format(type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


async def progressv(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress ➻ {2}%\n".format(
            "".join(["⦿" for i in range(math.floor(percentage / 5))]),
            "".join(["❍" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA ➻ {2}".format(humanbytes(current), humanbytes(total), time_formatter(estimated_total_time))
        if file_name:
            await edit_or_reply(
                event, "{}\nFile Name ➻ `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await edit_or_reply(event, "{}\n{}".format(type_of_ps, tmp))


async def progressl(current, total, event, start, prog_type, file_name=None, is_cancelled=False):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if "upload" in prog_type.lower():
            status = "Uploading"
        elif "download" in prog_type.lower():
            status = "Downloading"
        else:
            status = "Unknown"
        progress_str = "`{0}` | `[{1}{2}] {3}%`".format(
            status,
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = "{}\n`{} of {} @ {}`\n`ETA` ➻ {}\n`Duration` ➻ {}".format(progress_str, humanbytes(current), humanbytes(total), humanbytes(speed), time_formatter(eta), time_formatter(elapsed_time))
        if file_name:
            await event.edit(
                f"**{prog_type}**\n\n"
                f"**File Name ➻ **`{file_name}`**\nStatus**\n{tmp}"
            )
        else:
            await event.edit(f"**{prog_type}**\n\n" f"**Status**\n{tmp}")


async def progressj(current, total, event, start, prog_type, file_name=None, is_cancelled=False):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if 'upload' in prog_type.lower():
            status = 'Uploading'
        elif 'download' in prog_type.lower():
            status = 'Downloading'
        else:
            status = 'Unknown'
        progress_str = "`{0}` | [{1}{2}] `{3}%`".format(
            status,
            ''.join(["●" for i in range(
                    math.floor(percentage / 10))]),
            ''.join(["○" for i in range(
                    10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = "{}\n`{} of {} @ {}`\n`ETA` ➺ {}\n`Duration` ➺ {}".format(progress_str, humanbytes(current), humanbytes(total), humanbytes(speed), time_formatter(eta), time_formatter(elapsed_time))
        await event.edit(f"`{prog_type}`\n\n"
                          f"`Status`\n{tmp}")

