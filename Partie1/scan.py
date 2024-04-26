import socket
import multiprocessing

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
                    return port
        except Exception as e:
            pass

    def scan_range(self, start_port, end_port):
        open_ports = []
        # Nombre de processus à utiliser
        num_processes = multiprocessing.cpu_count()
        # Création du pool de processus
        with multiprocessing.Pool(processes=num_processes) as pool:
            # Utilisation de map pour distribuer les tâches de scan aux processus
            results = pool.map(self.scan_port, range(start_port, end_port + 1))
            # Filtrer les résultats pour ne garder que les ports ouverts
            open_ports = [port for port in results if port is not None]
        return open_ports

if __name__ == "__main__":
    host = input("Entrez l'hôte à scanner (par exemple, localhost) : ")
    start_port = int(input("Entrez le port de départ : "))
    end_port = int(input("Entrez le port de fin : "))

    scanner = PortScanner(host)
    open_ports = scanner.scan_range(start_port, end_port)
    print("Ports ouverts :", open_ports)

if __name__ == "__main__":
    host = input("Entrez l'hôte à scanner (par exemple, localhost) : ")
    start_port = int(input("Entrez le port de départ : "))
    end_port = int(input("Entrez le port de fin : "))

    scanner = PortScanner(host)
    open_ports = scanner.scan_range(start_port, end_port)
    print("Ports ouverts :", open_ports)