import socket
import time

def check_connection(host, port=80, timeout=3):
    """
    测试到指定主机和端口的 TCP 连通性
    """
    try:
        socket.setdefaulttimeout(timeout)
        start_time = time.time()
        # 尝试建立 TCP 连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        end_time = time.time()
        return True, (end_time - start_time) * 1000 # 返回延迟，单位毫秒
    except socket.error as ex:
        return False, str(ex)

if __name__ == "__main__":
    # 常用的测试节点，包含国内外的网站和公共 DNS
    hosts = [
        "www.baidu.com",
        "223.5.5.5",      # 阿里公共 DNS
        "114.114.114.114",# 114 DNS
        "www.bing.com",
        "8.8.8.8"         # Google 公共 DNS
    ]
    
    print("========================================")
    print("           网络连通性测试工具           ")
    print("========================================")
    
    for host in hosts:
        print(f"正在测试 -> {host}")
        # 测试 80 端口 (HTTP) 或者 53 端口 (DNS)
        # 对于域名，我们测试 80 端口；对于 IP 地址形式的 DNS，测试 53 端口
        port = 53 if host.count('.') == 3 and not host.startswith('www') else 80
        
        is_connected, result = check_connection(host, port=port)
        
        if is_connected:
            print(f"[\033[92m成功\033[0m] 连通正常! 端口: {port}, 延迟: {result:.2f} ms")
        else:
            print(f"[\033[91m失败\033[0m] 无法连通! 端口: {port}, 错误: {result}")
        print("-" * 40)
    
    print("测试完成。")
