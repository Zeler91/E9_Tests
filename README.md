# E9_Tests
[![Travis][build-badge]][build]
[build-badge]:https://img.shields.io/travis/Zeler91/E9_Tests/master.png?style=flat-square
[build]:https://travis-ci.org/Zeler91/E9_Tests

1. склонировать этот репозиторий;
2. перейти в папку с ним;
3. создать виртуальное окружение python -m venv venv;
4. активировать его;
5. установить зависимости pip install -r requirements.txt;
6. находясь в корневой папке: 
 - для просмотра и игры python hanger.py
 - для запуска тестов python -m pytest --cov=. tests/test_pytest.py
 
 p.s. Для игры с русскими словами закоментить bot.init_conf(word_base, attempts)
 и раскоментить # bot.init_conf(rus_base, attempts)
