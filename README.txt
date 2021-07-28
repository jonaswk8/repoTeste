Para executar o jupyter Projeto_Neoway_StefannoRuizManni.ipnyb e necessario ter instalado o anaconda e Python versao 3.7.10

Para executar siga os seguintes passos:


1- crie um novo ambiente no anaconda com o seguinte comando:

conda create -name nome_env python=3.7.10

2 - Ative o ambiente com o seguinte comando:

conda activate nome_env

3 - Navegue ate o diretorio onde o codigo e os demais arquivos se encontram (garanta que o arquivo requirements.txt esteja nesse diretrio)

4 - Instale os pacotes necessarios com o seguinte comando

pip install -r requirements.txt

5 - Adicione o ambiente no kernel do jupyter com o seguinte comando:

python -m ipykernel install --user --name nome_env --display-name "Python (nome_env)"

6 - Abra o jupyter no diretorio do arquivo Projeto_Neoway_StefannoRuizManni.ipnyb

7 - Garanta que o arquivo funcoes.py esteja no mesmo diretorio do arquivo Projeto_Neoway_StefannoRuizManni

8 - Na celula Leitura de Bases altere a variavel diretorio para o seu respectivo diretorio, apontando para a pasta Dados.