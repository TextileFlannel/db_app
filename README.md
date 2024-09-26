```docker build -t db_app .```
## Перед запуском включаем XLaunch!
```docker run -it --rm -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix db_app```