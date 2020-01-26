# E9_Tests
[![Travis][build-badge]][build]
[build-badge]: https://img.shields.io/travis/ githubname / reponame /master.png?style=flat-square
[build]: https://travis-ci.org/ githubname / reponame

склонировать этот репозиторий;
перейти в папку с ним;
создать виртуальное окружение python -m venv venv;
активировать его;
установить зависимости pip install -r requirements.txt;
находясь в корневой папке: 
 - для просмотра и игры python hanger.py
 - для запуска тестов python -m pytest --cov=. tests/test_pytest.py
 
 p.s. Для игры с русскими словами закоментить bot.init_conf(word_base, attempts)
 и раскоментить # bot.init_conf(rus_base, attempts)
