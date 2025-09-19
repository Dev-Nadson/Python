#!/usr/bin/env python3
"""
Script para verificar a existência das pastas 'arquivos-pec' ou 'pec-arquivos' 
no diretório /opt de múltiplas VMs via SSH.
"""

import paramiko
import logging
import csv
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import os

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'vm_check_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

class VMFolderChecker:
    def __init__(self, username, password=None, key_path=None, port=22):
        """
        Inicializa o verificador de VMs
        
        Args:
            username: Nome de usuário para SSH
            password: Senha (opcional se usar chave)
            key_path: Caminho para chave privada SSH (opcional)
            port: Porta SSH (padrão: 22)
        """
        self.username = username
        self.password = password
        self.key_path = key_path
        self.port = port
        self.target_folders = ['arquivos-pec', 'pec-arquivos']
        self.base_path = '/opt'
        
    def check_vm(self, vm_ip, vm_name=None):
        """
        Verifica uma VM específica
        
        Args:
            vm_ip: IP da VM
            vm_name: Nome da VM (opcional)
            
        Returns:
            dict: Resultado da verificação
        """
        if vm_name is None:
            vm_name = vm_ip
            
        result = {
            'vm_name': vm_name,
            'vm_ip': vm_ip,
            'status': 'error',
            'found_folders': [],
            'error_message': None,
            'timestamp': datetime.now().isoformat()
        }
        
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            # Conecta na VM
            if self.key_path:
                key = paramiko.RSAKey.from_private_key_file(self.key_path)
                ssh_client.connect(
                    hostname=vm_ip,
                    port=self.port,
                    username=self.username,
                    pkey=key,
                    timeout=30
                )
            else:
                ssh_client.connect(
                    hostname=vm_ip,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    timeout=30
                )
            
            # Verifica se as pastas existem
            for folder in self.target_folders:
                folder_path = f"{self.base_path}/{folder}"
                stdin, stdout, stderr = ssh_client.exec_command(f"test -d {folder_path} && echo 'EXISTS'")
                
                if stdout.read().decode().strip() == 'EXISTS':
                    result['found_folders'].append(folder)
                    
            if result['found_folders']:
                result['status'] = 'found'
                logging.info(f"✓ {vm_name} ({vm_ip}): Encontradas pastas: {', '.join(result['found_folders'])}")
            else:
                result['status'] = 'not_found'
                logging.info(f"- {vm_name} ({vm_ip}): Nenhuma pasta encontrada")
                
        except Exception as e:
            result['error_message'] = str(e)
            logging.error(f"✗ {vm_name} ({vm_ip}): Erro - {str(e)}")
            
        finally:
            ssh_client.close()
            
        return result
    
    def check_multiple_vms(self, vm_list, max_workers=10):
        """
        Verifica múltiplas VMs em paralelo
        
        Args:
            vm_list: Lista de VMs (pode ser lista de IPs ou lista de dicts com 'ip' e 'name')
            max_workers: Número máximo de threads paralelas
            
        Returns:
            list: Lista com resultados de todas as VMs
        """
        results = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submete todas as tarefas
            future_to_vm = {}
            
            for vm in vm_list:
                if isinstance(vm, dict):
                    vm_ip = vm.get('ip')
                    vm_name = vm.get('name', vm_ip)
                else:
                    vm_ip = vm
                    vm_name = vm_ip
                    
                future = executor.submit(self.check_vm, vm_ip, vm_name)
                future_to_vm[future] = vm_name
            
            # Coleta os resultados conforme completam
            for future in as_completed(future_to_vm):
                vm_name = future_to_vm[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    logging.error(f'VM {vm_name} gerou exceção: {exc}')
                    results.append({
                        'vm_name': vm_name,
                        'vm_ip': 'unknown',
                        'status': 'error',
                        'found_folders': [],
                        'error_message': str(exc),
                        'timestamp': datetime.now().isoformat()
                    })
        
        return results
    
    def save_results_csv(self, results, filename=None):
        """Salva resultados em CSV"""
        if filename is None:
            filename = f'vm_check_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['vm_name', 'vm_ip', 'status', 'found_folders', 'error_message', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in results:
                # Converte lista para string no CSV
                result_copy = result.copy()
                result_copy['found_folders'] = ', '.join(result['found_folders'])
                writer.writerow(result_copy)
        
        logging.info(f"Resultados salvos em: {filename}")
        
    def save_results_json(self, results, filename=None):
        """Salva resultados em JSON"""
        if filename is None:
            filename = f'vm_check_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(results, jsonfile, indent=2, ensure_ascii=False)
        
        logging.info(f"Resultados salvos em: {filename}")
        
    def print_summary(self, results):
        """Imprime resumo dos resultados"""
        total_vms = len(results)
        found_vms = len([r for r in results if r['status'] == 'found'])
        not_found_vms = len([r for r in results if r['status'] == 'not_found'])
        error_vms = len([r for r in results if r['status'] == 'error'])
        
        print(f"\n{'='*60}")
        print("RESUMO DOS RESULTADOS")
        print(f"{'='*60}")
        print(f"Total de VMs verificadas: {total_vms}")
        print(f"VMs com pastas encontradas: {found_vms}")
        print(f"VMs sem as pastas: {not_found_vms}")
        print(f"VMs com erro: {error_vms}")
        print(f"{'='*60}")
        
        if found_vms > 0:
            print("\nVMs COM as pastas:")
            for result in results:
                if result['status'] == 'found':
                    print(f"  • {result['vm_name']} ({result['vm_ip']}): {', '.join(result['found_folders'])}")

def load_vms_from_file(filename):
    """
    Carrega lista de VMs de um arquivo
    Suporta formatos:
    - Texto simples: um IP por linha
    - CSV: colunas 'ip' e opcionalmente 'name'
    """
    vms = []
    
    if filename.endswith('.csv'):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                vm = {'ip': row['ip']}
                if 'name' in row:
                    vm['name'] = row['name']
                vms.append(vm)
    else:
        # Arquivo de texto simples
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                ip = line.strip()
                if ip and not ip.startswith('#'):  # Ignora linhas vazias e comentários
                    vms.append(ip)
    
    return vms

def main():
    parser = argparse.ArgumentParser(description='Verifica pastas específicas em múltiplas VMs')
    parser.add_argument('--username', '-u', required=True, help='Nome de usuário SSH')
    parser.add_argument('--password', '-p', help='Senha SSH')
    parser.add_argument('--key', '-k', help='Caminho para chave privada SSH')
    parser.add_argument('--port', type=int, default=22, help='Porta SSH (padrão: 22)')
    parser.add_argument('--vms-file', '-f', help='Arquivo com lista de VMs')
    parser.add_argument('--vms', nargs='+', help='Lista de IPs de VMs')
    parser.add_argument('--workers', type=int, default=10, help='Número de threads paralelas (padrão: 10)')
    parser.add_argument('--output-csv', help='Nome do arquivo CSV de saída')
    parser.add_argument('--output-json', help='Nome do arquivo JSON de saída')
    
    args = parser.parse_args()
    
    # Valida argumentos
    if not args.password and not args.key:
        print("Erro: Deve fornecer senha (--password) ou chave SSH (--key)")
        return
    
    if not args.vms_file and not args.vms:
        print("Erro: Deve fornecer arquivo de VMs (--vms-file) ou lista de IPs (--vms)")
        return
    
    # Carrega lista de VMs
    if args.vms_file:
        if not os.path.exists(args.vms_file):
            print(f"Erro: Arquivo {args.vms_file} não encontrado")
            return
        vm_list = load_vms_from_file(args.vms_file)
    else:
        vm_list = args.vms
    
    if not vm_list:
        print("Erro: Lista de VMs vazia")
        return
    
    # Inicializa checker
    checker = VMFolderChecker(
        username=args.username,
        password=args.password,
        key_path=args.key,
        port=args.port
    )
    
    print(f"Iniciando verificação de {len(vm_list)} VMs...")
    print(f"Procurando pelas pastas: {', '.join(checker.target_folders)}")
    print(f"No diretório: {checker.base_path}")
    print("-" * 60)
    
    # Executa verificação
    results = checker.check_multiple_vms(vm_list, max_workers=args.workers)
    
    # Salva resultados
    if args.output_csv:
        checker.save_results_csv(results, args.output_csv)
    else:
        checker.save_results_csv(results)
    
    if args.output_json:
        checker.save_results_json(results, args.output_json)
    
    # Exibe resumo
    checker.print_summary(results)

if __name__ == "__main__":
    main()

# Exemplo de uso programático:
"""
# Exemplo 1: Lista simples de IPs
from vm_folder_checker import VMFolderChecker

checker = VMFolderChecker(username='usuario', password='senha')
vms = ['192.168.1.10', '192.168.1.11', '192.168.1.12']
results = checker.check_multiple_vms(vms)
checker.print_summary(results)

# Exemplo 2: Lista com nomes
vms = [
    {'ip': '192.168.1.10', 'name': 'vm-web-01'},
    {'ip': '192.168.1.11', 'name': 'vm-db-01'},
    {'ip': '192.168.1.12', 'name': 'vm-app-01'}
]
results = checker.check_multiple_vms(vms)
checker.save_results_csv(results, 'resultado_vms.csv')
"""