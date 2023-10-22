from nmap_scan import run_nmap_scan
from harvest_info import run_theharvester
from subdomain_enum import run_sublist3r

def main():
    target = input("Introduce el dominio objetivo: ")

    # Ejecutar las herramientas
    run_nmap_scan(target)
    run_theharvester(target)
    run_sublist3r(target)

if __name__ == "__main__":
    main()
