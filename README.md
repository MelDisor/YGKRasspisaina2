## Part 1. Установка ОС

- **Действия:**
  - Установлена Ubuntu 20.04 Server LTS без графического интерфейса в VirtualBox.
- **Версия Ubuntu:**
  - ![Скриншот вывода команды `cat /etc/issue`](https://github.com/user-attachments/assets/fa22a9fa-eff4-4de3-9149-1935d0d3ba51)
)

## Part 2. Создание пользователя

- **Действия:**
  - Создан новый пользователь `<имя_пользователя>` и добавлен в группу `adm`.
- **Создание пользователя:**
  - ![Скриншот вызова команды для создания пользователя](https://github.com/user-attachments/assets/fe1a0d24-bb34-4ccc-ad0f-c72f83c78ed3)
)
- **Проверка в /etc/passwd:**
  - ![Скриншот вывода команды `cat /etc/passwd`](https://github.com/user-attachments/assets/fe1a0d24-bb34-4ccc-ad0f-c72f83c78ed3)

## Part 3. Настройка сети ОС

- **Переименование машины:**
  - Название машины установлено в `user-1`.
- **Установка часовой зоны:**
  - Установлена временная зона `<ваша_часовая_зона>`.
- **Сетевые интерфейсы:**
  -   
  - _Объяснение наличия интерфейса `lo`._
- **IP от DHCP:**
  -   
  - _Расшифровка DHCP: Dynamic Host Configuration Protocol — протокол автоматической настройки сетевых параметров._
- **Внешний и внутренний IP шлюза:**
  - Внешний IP шлюза: `<внешний_ip>`
  - Внутренний (по умолчанию) IP шлюза: `<внутренний_ip>`
- **Статические настройки:**
  - IP: `<статичный_ip>`
  - Gateway: `<статичный_gw>`
  - DNS: `1.1.1.1`, `8.8.8.8`
  - 
- **Пинг удалённых хостов:**
  - ![Скриншот вывода `ping 1.1.1.1` и `ping ya.ru` с 0% потерь](https://github.com/user-attachments/assets/3c336623-b6dc-4190-8f55-b05bcbf831ed)
)

## Part 4. Обновление ОС

- **Обновление пакетов до последней версии:**
  - Выполнена команда `sudo apt update && sudo apt upgrade -y`.
- **Проверка отсутствия обновлений:**
  - ![Скриншот сообщения о том, что обновления отсутствуют](https://github.com/user-attachments/assets/7627a778-44a5-48d9-91a4-18e7c412ec47)
)

## Part 5. Использование команды sudo

- **Разрешение sudo для пользователя:**
  - Пользователь `<имя_пользователя>` добавлен в группу `sudo` или внесён в `/etc/sudoers`.
- _Назначение команды sudo: позволяет выполнять команды от имени суперпользователя с проверкой прав и логированием._
- **Изменение hostname от имени пользователя:**
  - ![Скриншот с новым hostname](https://github.com/user-attachments/assets/29177267-187f-46b9-a858-e03d51825269)
)

## Part 6. Установка и настройка службы времени

- **Настройка автоматической синхронизации:**
  - Включён и запущен сервис `systemd-timesyncd` (или `ntp`/`chrony`).
- **Текущее время и часовой пояс:**
  - ![Скриншот вывода `timedatectl`](https://github.com/user-attachments/assets/e6d5ece7-29bf-4e5f-bff2-83c2c163658f)
- **Проверка NTPSynchronized=yes:**
  - ![Скриншот вывода `timedatectl show`]

## Part 7. Установка и использование текстовых редакторов

- **Установка редакторов:**
  - Установлены VIM, NANO, MCEDIT.
- **Создание файлов и сохранение:**
  - VIM: ![Скриншот `vim test_vim.txt` с никнеймом перед закрытием](https://github.com/user-attachments/assets/8f794450-fe54-47cd-94a1-4b522943022b)
    _Действие для сохранения и выхода: `:wq`._
    
  - NANO: ![Скриншот `nano test_nano.txt` с никнеймом перед закрытием](https://github.com/user-attachments/assets/e4690698-907c-4398-bbfa-d5ec3b9cfe55)
    _Действие: `Ctrl+O`, `Enter`, `Ctrl+X`._
    
  - MCEDIT: ![Скриншот `mcedit test_mcedit.txt` с никнеймом перед закрытием](https://github.com/user-attachments/assets/01be9210-d83d-4369-9e13-3f8dc3aee2c1)
    _Действие: `F2` (Save), `F10` (Exit)._
    
- **Редактирование без сохранения:**
  - VIM: ![Скриншот после редактирования в VIM без сохранения](https://github.com/user-attachments/assets/f24bd058-b86d-48f8-822f-9bd4297fe815)
    _Действие: `:q!`._
    
  - NANO: ![Скриншот после редактирования в NANO без сохранения](https://github.com/user-attachments/assets/d01fc61c-98ca-438c-8461-2f4faf9aa761)
    _Действие: `Ctrl+X`, при запросе `N`._
    
  - MCEDIT: ![Скриншот после редактирования в MCEDIT без сохранения](https://github.com/user-attachments/assets/1e6b07b9-8185-449a-ab7c-4a5d73fe393b)
    _Действие: при запросе сохранить `No`._

- **Поиск и замена:**
  - VIM: ![Скрин поиска слова в VIM](https://github.com/user-attachments/assets/27657771-c907-4fd3-9b1b-3479f610c6f8)
    Команда поиска: `/<слово>`  
    Замена: `:%s/old/new/g`.
    
  - NANO: ![Скрин поиска в NANO](https://github.com/user-attachments/assets/8d60c138-cea9-4772-abb1-8d9c09d16cdf)
    Поиск: `Ctrl+\\`  
    Замена: `Ctrl+\\` и ввод новых данных.

    
  - MCEDIT: ![Скрин поиска в MCEDIT](https://github.com/user-attachments/assets/2f5f491f-2086-4efd-83ee-5f5770e1d5b0)(![Снимок экрана от 2025-04-25 14-31-40](https://github.com/user-attachments/assets/529c1296-c7fa-45a6-afe2-b582c8826cfe)
    Поиск и замена через `F9` (Search) и `F9` (Replace).

## Part 8. Установка и базовая настройка сервиса SSHD

- **Установка SSHd:**
  - `sudo apt install openssh-server`.
- **Автостарт:**
  - `sudo systemctl enable ssh`.
- **Порт 2022:**
  - Изменён `Port` в `/etc/ssh/sshd_config`.
- **Проверка процесса sshd:**
  - ![Скриншот вывода `ps aux | grep sshd`](https://github.com/user-attachments/assets/c8be5ee9-c121-4a87-b766-0bfdd18ebc64)
    _Объяснение: `ps aux` — `a` все пользователи, `u` формат с владельцем, `x` без терминала._
    
- **Перезагрузка и проверка прослушивания порта:**
  - ![Скриншот `netstat -tan | grep 2022`](https://github.com/user-attachments/assets/74a65503-9963-40c8-b43e-0282933181a6)
    _Ключи `-tan`: `t` TCP, `a` все, `n` числовые адреса; 0.0.0.0 — слушает на всех интерфейсах._

## Part 9. Установка и использование утилит top, htop

- **Установка и запуск:**
  - `sudo apt install htop`.
- **Данные из top:**
  - **uptime:** `<1498>`  
  - **Авторизованные пользователи:** `<root>`  
  - **Средняя загрузка:** `<load averages>`  
  - **Общее число процессов:** `<42>`  
  - **Загрузка CPU:** `<8%>`  
  - **Загрузка памяти:** `<0.9%>`  
  - **PID процесса с наибольшей памятью:** `<pid 1698>`  
  - **PID процесса с наибольшей загрузкой CPU:** `<pid 1498>`
- **Скриншоты htop:**
  - Отсортированный по PID: ![![Снимок экрана от 2025-04-25 14-45-45](https://github.com/user-attachments/assets/d1906ad2-dc38-4dd0-ae2d-451f9a4c70db)
](#)
  - По PERCENT_CPU: ![![Снимок экрана от 2025-04-25 14-45-45](https://github.com/user-attachments/assets/9d719f31-09ee-41d3-bce7-f2601e862fe6)
](#)
  - По PERCENT_MEM: ![![Снимок экрана от 2025-04-25 14-46-39](https://github.com/user-attachments/assets/395c2469-b844-42f6-bd30-d151fb7e1a3b)
](#)
  - По TIME: ![![Снимок экрана от 2025-04-25 14-46-50](https://github.com/user-attachments/assets/8a7ceea9-9a8c-4d5c-959b-4d3d20f05c33)
](#)
  - Отфильтрованный для sshd: ![![Снимок экрана от 2025-04-25 14-47-06](https://github.com/user-attachments/assets/d535fbf6-2cd2-464f-8df1-1370c6cd6c56)
](#)
  - Процесс syslog, найденный через поиск: ![![Снимок экрана от 2025-04-25 14-47-36](https://github.com/user-attachments/assets/9c7f3d84-ff4e-4804-8e7c-06435f6ccb90)
](#)
  - Добавлены hostname, clock, uptime: ![![Снимок экрана от 2025-04-25 14-50-54](https://github.com/user-attachments/assets/fe731ea8-4148-4724-a59c-69d18c8b4da4)
](#)

## Part 10. Использование утилиты fdisk

- **Вывод fdisk -l:**
  - ![Скриншот вывода `fdisk -l`](https://github.com/user-attachments/assets/a988b2b0-1009-4890-896f-db72f903652e)
)
- **Данные о диске:**
  - Название диска: `<VBOX HARDDISK>`  
  - Размер: `<25gib>`  
  - Количество секторов: `<52428800>`  
  - Размер swap: `<2g>`

## Part 11. Использование утилиты df

- **Вывод df:**
  - ![Скриншот `df`](https://github.com/user-attachments/assets/6ce3a405-4354-4246-8371-60573e98bf54)
)
  - Для `/`: размер, занято, свободно, процент использования: `<значения>`
  - Единица измерения: `<KB/MB/...>`
- **Вывод df -Th:**
  - ![Скриншот `df -Th`](https://github.com/user-attachments/assets/2e87c145-1a89-430f-94f9-4b0fa1d869a8)
)
  - Для `/`: размер, занято, свободно, процент использования, тип файловой системы: `<значения>`

## Part 12. Использование утилиты du

- **Вывод du:**
  - ![Скриншот `du`](https://github.com/user-attachments/assets/52a49dcd-faed-424f-93da-5e697f6d862e)
)
- **Размеры папок:**
  - `/home`, `/var`, `/var/log` в байтах и человекочитаемом виде: ![835 mb ](![Снимок экрана от 2025-04-25 14-58-28](https://github.com/user-attachments/assets/847a7c37-15de-4ac9-82a9-420fcb764225)
)
- **Размер каждого элемента в /var/log:**
  - ![Скриншот `du /var/log/*`](https://github.com/user-attachments/assets/33999877-0a13-49f5-be6f-85e86cb4e145)
)

## Part 13. Установка и использование утилиты ncdu

- **Установка:**
  - `sudo apt install ncdu`.
- **Вывод ncdu:**
  - Размеры `/home`, `/var`, `/var/log`: ![...](https://github.com/user-attachments/assets/b3863179-e24e-402e-9d5e-6420ccf9726f)
)

## Part 14. Работа с системными журналами

- **Просмотр логов:**
  - `/var/log/dmesg`, `/var/log/syslog`, `/var/log/auth.log`: ![...](![Снимок экрана от 2025-04-25 15-01-01](https://github.com/user-attachments/assets/ea036239-dbd3-4d72-94dc-cbb90d9add66) ![Снимок экрана от 2025-04-25 15-01-17](https://github.com/user-attachments/assets/92cd6618-2630-4b1a-b8f7-58e9e830cf4b) ![Снимок экрана от 2025-04-25 15-01-32](https://github.com/user-attachments/assets/d4ac9792-f61b-494a-93bc-4ece9c7c788f)


- **Последняя успешная авторизация:**
  - Время: `<15:12>`, пользователь: `<meldis3>`, метод: `<uptime>`
- **Перезапуск sshd:**
  - ![Скриншот сообщения о рестарте в логах](https://github.com/user-attachments/assets/e7ef7187-61c8-48fe-8699-903c35332722)
)

## Part 15. Использование планировщика заданий CRON

- **Запуск uptime каждые 2 минуты:**
  - Запись в crontab: `*/2 * * * * /usr/bin/uptime`.
- **Логи выполнения:**
  - ![Скриншот строк о выполнении из syslog](![Снимок экрана от 2025-04-25 15-12-31](https://github.com/user-attachments/assets/ac6462cf-4f6f-464e-a9a7-ed1415a6129e)
)
- **Список текущих заданий CRON:**
  - ![Скриншот `crontab -l`](![Снимок экрана от 2025-04-25 15-13-48](https://github.com/user-attachments/assets/991a5015-c6e3-49c6-9bd2-daf5aea4fa45)
)
- **Удаление всех заданий:**
  - `crontab -r`.
- **Проверка пустого списка:**
  - ![Скриншот пустого `crontab -l`](https://github.com/user-attachments/assets/15149dbe-7f1a-408c-a536-4d8e92252b30)
)
