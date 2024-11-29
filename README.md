<h1>Alistamento Militar - Python
</h1>

<p>Este é um projeto em Python que simula o processo de alistamento militar, coletando informações pessoais e fornecendo uma análise de acordo com os dados fornecidos pelo usuário. O sistema solicita informações como nome, idade, CPF, telefone, estado civil, escolaridade, profissão e se há problemas de saúde. Em seguida, ele avalia se o usuário está na idade de se alistar e exibe as informações formatadas de forma organizada.

</p>

<h2>Funcionalidades</h2>

<p>• <b>Cadastro de dados pessoais:</b> Solicita ao usuário informações como nome, idade, CPF, telefone, estado civil, escolaridade, profissão e problemas de saúde.</p>

<p>• <b>Verificação da idade para alistamento:</b> O sistema verifica se o usuário está na idade de se alistar, se já passou da idade ou se está fora da faixa etária exigida para o alistamento.</p>

<p>• <b>Formatação de CPF e telefone:</b> O sistema formata o CPF e o telefone inseridos para exibição adequada.
</p>

<p>• <b>Exibição dos dados:</b> Após o preenchimento, o sistema exibe todos os dados coletados de forma organizada e formatada.</p>

<h2>Estrutura do código</h2>

<p>• <b>Função</b> <code>formatar_cpf(cpf_digitado):</code> Formata o CPF digitado para o formato xxx.xxx.xxx-xx.</p>
<p>• <b>Função </b> <code>formata_telefone(telefone):</code> Formata o número de telefone no formato xxxx-xxxx.</p>

<p>• <b>Entrada de dados:</b> O programa solicita informações ao usuário, valida e formata os dados conforme necessário.</p>
<p>• <b>Cálculo de idade e alistamento:</b> O sistema calcula a idade do usuário, determina se ele está dentro da faixa etária de alistamento e apresenta as opções de acordo com a idade.</p>
<p>• <b>Exibição dos resultados:</b> O programa exibe todos os dados fornecidos pelo usuário de forma organizada.</p>


<h2>Exemplo de execução</h2>

```
Digite seu nome completo: João Silva
Digite sua idade: 22
Digite seu CPF (apenas números): 12345678909
Selecione seu estado: 
1° Alagoas
2° Pernambuco
3° São Paulo
4° Rio de janeiro
3
Digite seu telefone (apenas números): 98765432
Qual e o seu estado civil:
1° Solteiro
2° Casado
3° Divorciado
4° Viúvo
5° Separado judicialmente
6° União Estável
1
Qual e a sua escolaridade:
1° Analfabeto
2° Ensino Fundamental Incompleto/Completo
3° Ensino Médio Incompleto/Completo                   
4° Ensino Técnico
5° Ensino Superior Incompleto/Completo
6° Pós-Graduação
7° Outros Cursos
5
Digite sua profissão: Desenvolvedor
Possui algum problema de saúde [S/N]: N

Nome: João Silva
Você passou da idade de se alistar.
São Paulo
CPF: 123.456.789-09
Telefone:  9876-5432
Solteiro
Ensino Superior Incompleto/Completo
Profissão:  Desenvolvedor
Não possui problema de saúde
```


<h2>Contribuições</h2>

<p>Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork, enviar pull requests ou abrir problemas.</p>


















