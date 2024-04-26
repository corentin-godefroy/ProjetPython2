import socket

class PortScanner:
    def __init__(self, host):
        self.host = host

    def scan_port(self, port):
        try:
            # Créer une socket TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Définir un timeout pour la connexion
                s.settimeout(1)
                # Tenter de se connecter au port
                result = s.connect_ex((self.host, port))
                if result == 0:
                    print(f"Port {port} est ouvert")
                    return port
        except Exception as e:
            print(f"Erreur lors de la vérification du port {port}: {e}")

    def scan_range(self, start_port, end_port):
        open_ports = []
        for port in range(start_port, end_port + 1):
            if self.scan_port(port):
                open_ports.append(port)
        return open_ports

if __name__ == "__main__":
    host = input("Entrez l'hôte à scanner (par exemple, localhost) : ")
    start_port = int(input("Entrez le port de départ : "))
    end_port = int(input("Entrez le port de fin : "))

    scanner = PortScanner(host)
    open_ports = scanner.scan_range(start_port, end_port)
    print("Ports ouverts :", open_ports)