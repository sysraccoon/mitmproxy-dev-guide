"""
Простой вариант запускающий mitmdump как подпроцесс.
Если хотите пример запускающий mitmdump внутри текущего процесса,
можете посмотреть на integrate_mitmdump_inside_app.py
"""

import subprocess

def main():
    subprocess.run(["mitmdump", "-s", "url_log_addon.py"])


if __name__ == "__main__":
    main()
