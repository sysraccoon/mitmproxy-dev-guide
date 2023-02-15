"""
Не документированный вариант запуска mitmproxy из кода на Python.
Данный пример написан на основе кода представленного тут:
https://github.com/mitmproxy/mitmproxy/blob/244ff35e606e8ae7ca8aa15d7529566a97ec69f5/mitmproxy/tools/main.py

Если хотите более надёжный (в том смысле что он опирается на оффициальную документацию) вариант запуска,
можете посмотреть на integrate_mitmdump_subprocess.py
"""

import asyncio
import signal

from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster


def main():
    asyncio.run(start_mitmproxy())


async def start_mitmproxy():
    options = Options()
    master = DumpMaster(options=options)

    loop = asyncio.get_running_loop()
    register_safe_exit(loop, master)

    await master.run()


def register_safe_exit(loop, master):
    def _sigint(*_):
        loop.call_soon_threadsafe(
            getattr(master, "prompt_for_exit", master.shutdown)
        )

    def _sigterm(*_):
        loop.call_soon_threadsafe(master.shutdown)

    signal.signal(signal.SIGINT, _sigint)
    signal.signal(signal.SIGTERM, _sigterm)


if __name__ == "__main__":
    main()
