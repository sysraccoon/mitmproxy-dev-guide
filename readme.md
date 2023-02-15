# Примеры для "ультимативного гайда по расширению mitmproxy"

Этот репозиторий содержит примеры представленные в данном видео: [COMING SOON].

Код проверен в следующем окружении:
* NixOS (unstable channel)
* python версии 3.9.16
* mitmproxy версии 9.0.1

Если хотите развернуть у себя окружение для запуска, можете использовать следующие команды:

```bash
# Если не используете nix
python3 -m venv venv
source venv/bin/activate # для linux/mac bash/zsh
venv\Scripts\activate.bat # для windows cmd.exe
pip3 install -r requirements.txt

# Если используете nix
nix-shell
```

Полезные ссылки (англ.):
* [Официальный сайт mitmproxy](https://mitmproxy.org/)
* [Страница в документации про написание аддонов](https://docs.mitmproxy.org/stable/addons-overview/)
* [Ещё больше примеров аддонов в документации](https://docs.mitmproxy.org/stable/addons-examples/)
