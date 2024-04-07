### Utilize os seguintes comandos caso retorne algum erro na execução do script para alterar as permissões do script e executar o mesmo, modefique os diretorios para onde estão os seus arquivos python.


```sh
chmod +x /home/ / /linux_automation_py/backup.py
```

```sh
 python3 /home/ / /linux_automation_py/backup.py
```
```sh
python3 /usr/bin /home/ / /linux_automation_py/backup.py   
```

### CRONTAB PARA AUTOMATIZAR O BACKUP DOS ARQUIVOS E DELETAR

```sh
crontab -e
```

```sh
 45 12 * 4 1-6 /usr/bin/python3 /home/thlinux/Documents/Projects/linux_automation_py/backup.py
```

# Para entender melhor os campos do cron:

- `45:` Especifica o minuto em que a tarefa será executada `(45 minutos após a hora)`.
- `12:` Especifica a hora em que a tarefa será executada `(12 horas)`.
- `*:` Este é um curinga e significa` "qualquer"` para o campo do dia do mês, permitindo que a tarefa seja executada em qualquer dia do mês.
- `4: `Especifica o mês em que a tarefa será executada `(fevereiro)`.
- `1-6:` Especifica o dia da semana em que a tarefa será executada `(segunda a sábado)`. O número `1` representa `segunda-feira` e o número `6` representa `sábado`.

- Linux references [Schedule Jobs with Cron](https://learning.lpi.org/en/learning-materials/102-500/107/107.2/107.2_01/)
- Python references [os module](https://docs.python.org/3/library/os.html)
- Python references [shutil module](https://docs.python.org/3/library/shutil.html)

### Monitoramento de memoria, cpu e disco

- `psutil.cpu_percent():` Retorna o uso atual da` CPU` como uma porcentagem.
- `psutil.virtual_memory().percent:` Retorna o uso atual da` memória` como uma porcentagem.
- `psutil.disk_usage('/'):` Retorna estatísticas de uso do `disco` para o diretório raiz.

- Python references [psutil module](https://pypi.org/project/psutil/)
- Python references [psutil module](https://psutil.readthedocs.io/en/latest/)
  
Para verificar os dados de uso de memoria, cpu e disco rode o ocomando abaixo para exibir os resultados.
```sh
python3 /usr/bin /home/ / /linux_automation_py/system_monitor.py   
```
### Gerenciamento de permissões de arquivos pyhton.

- `file_path = 'backup_files':` Esta linha define o caminho do arquivo ou diretório cujas permissões serão alteradas. No caso já está definido como o diretório backup_files ('/backup_files') mais você alterar conforme a sua necessidade.

- `mode = 0o755:` Esta linha define o novo modo de permissões para o arquivo ou diretório. No exemplo fornecido, o modo de permissões está definido como `755` no formato octal.

- `change_permissions(file_path, mode):` Esta linha chama a função `change_permissions`, passando o caminho do arquivo ou diretório e o modo de permissões como argumentos para realizar a alteração de permissões.
  
Para aplicar a mudança de permissões nos arquivos definidos no script rode o comando abaixo.

```sh
python3 /usr/bin /home/ / /linux_automation_py/permissions.py
```
confira se as permissões foram aplicada no diretorio utiloizando o comando abaixo.
```sh
ls -la backup_files 
```
- Python references [os module](https://docs.python.org/3/library/os.html)
- Python references [oschmod ](https://pypi.org/project/oschmod/)
- Python references [Errors and Exceptions ](https://pypi.org/project/oschmod/)