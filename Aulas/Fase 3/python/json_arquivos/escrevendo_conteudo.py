#Métodos de manipulação
#'r' abrir para leitura (modo padrão).
#'w' abrir para a escrita, sobrescrevendo o conteúdo.
#'x' abrir para a criação de arquivo, gerando uma falha se existir um arquivo com o mesmo nome no mesmo local.
#'a' abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente.
#'b' abrir em modo binário.
#'t' abrir em modo de texto (modo padrão).
#'+' abrir para atualização (escrita e leitura).

#Criando uma variável de texto
conteudo = "Salve o Corinthians, o campeão dos campeões, eternamente..."

#Usando a função open para criar um objeto do tipo arquivo
#arquivo = open("c:\\arquivos\\arquivo_texto.txt", "w", encoding="utf-8")

#Escrevendo o conteúdo da variável conteúdo dentro do arquivo w
#arquivo.write(conteudo)

#Escrevendo o conteúdo da variável conteúdo dentro do arquivo a
arquivo = open("c:\\arquivos\\arquivo_texto.txt", "a", encoding="UTF-8")
arquivo.write("\nTeste novo")



#Fechando o arquivo
arquivo.close()