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