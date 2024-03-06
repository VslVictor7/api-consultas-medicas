(Certifique-se que a primeira pasta do terminal seja "Testes" (A pasta que envolve todos os projetos) antes de seguir os passos, para não haver conflitos com os outros projetos.
Por exemplo: "C:\Users\someone\OneDrive\Desktop\Testes>")



Caso seja necessário ativar a máquina virtual para rodar, basta abrir o terminal "Git Bash" ou "Git" e escrever ". venv/Scripts/activate" no terminal.


"pip install django" e "pip install djangorestframework" para baixar o Django e o Django Rest Framework. 


Passos para rodar o projeto em Django abaixo:


Passo 1: Acessar pasta do projeto com "cd Back-End-opção-2/projeto" pelo terminal.

Passo 2: Escrever no terminal "python manage.py runserver" para rodar o projeto.



Explicando funcionalidades:



-------PROFISSIONAIS-------

-Logo ao rodar o servidor, você será redirecionado para a interface própria do Django Rest Framework.

-Nele, irá aparecer duas opções de links clicáveis para a lista de Profissionais e Consultas.

-Ao clicar na lista de Profissionais, você terá a possibilidade de ver todos os Profissionais e os cadastros que estão registrados em cada um dos Profissionais.

-Para criar um novo Profissional no banco de dados, basta olhar mais abaixo no site, onde terá as
opções de nome completo, nome social, profissão, endereço e contato.

-Insira os valores que deseja em cada campo (Contato deve ser obrigatoriamente Interger, o restante são
Charfields.)

-Após inserir tudo, clique em "POST" para inserir os valores na tabela "Profissional".

-Para conferir um profissional específico que foi cadastrado, basta ir na barra de navegação e 
inserir o ID correspondente do profissional logo após "Profissionais/" (Por exemplo, Victor Santos possui ID 1, então irei escrever "http://127.0.0.1:8000/Profissionais/1")

-Ao entrar, você poderá editar e deletar as informações do profissional do ID escolhido.

-Para deletar, basta clicar em "DELETE". 

-Para Editar, basta mudar qualquer informação nas colunas de nome completo, nome social, profissão, endereço ou contato. Após isso, clique em "PUT" para editar as informações.

-Para voltar para a lista de profissionais, basta escrever "http://127.0.0.1:8000/Profissionais" na barra de navegação ou clicar em "Profissional Api List".


-------CONSULTAS-------


-Volte para o home escrevendo "http://127.0.0.1:8000" ou clicando em "Api Root".

-Clique no link de consultas.

-Ao clicar na lista de Consultas, você terá a possibilidade de ver todos as Consultas e o ID de todos os profissionais referentes a ela.

-Para criar uma nova Consulta no banco de dados, basta olhar mais abaixo no site, onde terá as
opções de Data Consulta e Id prof (Id Prof é o ID referente a um profissional, por exemplo, o ID referente a Victor Santos seria ID 1 "Profissional object (1)").

-Insira os valores que deseja em cada campo.

-Após inserir tudo, clique em "POST" para inserir os valores na tabela "Consulta".

-Para conferir uma consulta específica que foi cadastrada, basta ir na barra de navegação e 
inserir o ID correspondente da consulta logo após "Consultas/" (Por exemplo, minha consulta de "8 de maio, 2024" possui ID 1, então irei escrever "http://127.0.0.1:8000/Consultas/1")

-Ao entrar, você poderá editar e deletar as informações da consulta do ID escolhido.

-Para deletar, basta clicar em "DELETE". 

-Para Editar, basta mudar qualquer informação nas colunas de Data consulta e Id Prof. Após isso, clique em "PUT" para editar as informações.

-Para voltar para a lista de profissionais, basta escrever "http://127.0.0.1:8000/Consultas" na barra de navegação ou clicar em "Clinica Api List".


-------TESTE UNITÁRIO-------

-O teste unitário foi feito testando o arquivo python "models.py".

-Para conferir o arquivo de teste, abra a pasta chamada "tests", dentro dela terá o arquivo python "test_models.py".

-O teste irá criar um profissional e uma consulta no método "setUp()" antes de realizar algum teste.

-Após isso, nos métodos "test_profissional_creation" e "test_consulta_creation" irá acontecer a verificação se os objetos foram criados corretamentee se os campos estão preenchidos conforme o esperado.

-Para rodar o teste, escreva "python manage.py test".
