workers = 1                 # 进程数量
worker_class = "gevent"     # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:8000"
preload_app = True