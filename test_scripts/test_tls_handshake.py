import socket
import ssl

def test_tls():
    context = ssl.create_default_context()
    context.load_verify_locations("certs/ca-cert.pem")
    context.load_cert_chain("certs/mcu-cert.pem", "certs/mcu-key.pem")
    
    with socket.create_connection(("localhost", 8080)) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as ssock:
            print(f"TLS Handshake Successful! Protocol: {ssock.version()}")
            return True
    return False

if __name__ == "__main__":
    if test_tls():
        print("TLS test PASSED")
    else:
        print("TLS test FAILED")