# My Project

## Описание

Проект включает в себя:
- FastAPI приложение с MongoDB для хранения сообщений
- Telegram бот на aiogram3
- Nginx для реверс-прокси
- Redis для кэширования

## Установка и запуск

1. Склонируйте репозиторий:
       git clone <repository-url>
    
2. Перейдите в директорию проекта:
       cd my_project
    
3. Запустите Docker Compose:
       docker-compose up --build
    
4. Для первоначального получения сертификата SSL:
       docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email your_email --agree-tos --no-eff-email -d your_domain
    
## Использование

- FastAPI приложение будет доступно по адресу: http://localhost:80
- Telegram бот будет взаимодействовать с API приложения для отображения и создания сообщений.