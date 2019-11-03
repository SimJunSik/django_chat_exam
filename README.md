## nginx
```
server {
        listen 80;
        server_name 13.209.53.205;
        charset utf-8;
        client_max_body_size 128M;

        location / {
                proxy_pass http://0.0.0.0:8000;
        }

        location /ws {
                proxy_pass http://0.0.0.0:8001;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";

                proxy_redirect     off;
                proxy_set_header   Host $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
        }

        location /static/ {
                root /home/ubuntu/chat_env/django_chat_exam/;
        }
}
```

## daphne.service
```
[Unit]
Description=daphne Emperor service
After=syslog.target

[Service]
User=root
Group=root
WorkingDirectory=/home/ubuntu/chat_env/django_chat_exam/
Environment=DJANGO_SETTINGS_MODULE=chat_ex.settings
ExecStart=/home/ubuntu/chat_env/bin/daphne -b 0.0.0.0 -p 8001 chat_ex.asgi:application --access-log /var/log/daphne/daphne.log

# KillSignal=SIGQUIT
# Type=notify
# StandardError=syslog
# NotifyAccess=all
# Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## redis
- 설치
```
sudo apt-get install redis-server
```
- 버전확인
```
redis-server --version
```
- cli 실행
```
redis-cli
```
- vm 스펙확인(메모리)
```
vmstat -s
```
- maxmemory 등 설정
```
sudo nano /etc/redis/redis.conf
```
- redis 재시작
```
sudo systemctl restart redis-server.service
```
- 인스턴스 재부팅시 자동 재시작
```
sudo systemctl enable redis-server.service
```

#### load balancing
## nginx
```
server {
        listen 80;
        server_name 13.209.53.205;
        charset utf-8;
        client_max_body_size 128M;

        location / {
                proxy_pass http://0.0.0.0:8000;
        }

        location /ws {
                proxy_pass http://daphne-server;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";

                proxy_redirect     off;
                proxy_set_header   Host $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
        }

        location /static/ {
                root /home/ubuntu/chat_env/django_chat_exam/;
        }
}

# load balancing - round robin
upstream daphne-server{
        server 13.209.53.205:8002;
        server 13.209.53.205:8003;
        server 13.209.53.205:8004;
}
```

## daphne
- 기존에 만들었던 방식과 똑같이 daphne1.service, daphne2.service, daphne3.service 를 만들고
nginx에서 round robin 방식으로 처리
- 각각 다 enable, start 해줄것


#### Test
- Jmeter 사용