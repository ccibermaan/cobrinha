# Antigravity Snake

Um jogo clássico da cobrinha (Snake) desenvolvido com [Brython](https://brython.info/) para rodar diretamente no navegador. Esta versão utiliza uma lib Python personalizada leve chamada `antigravity.py` e um design visual moderno.

## Como Jogar

- Use as **Setas do Teclado** ou as teclas **W, A, S, D** para direcionar a cobra.
- Coma a comida vermelha para seu corpo crescer e ganhar pontos (10 pontos por bloco de comida).
- Evite bater nas paredes da borda do jogo e no seu próprio corpo.

## Setup Técnico

- **Tecnologias**: HTML5 Canvas, Cascading Style Sheets (CSS3) e Brython para Python no Front-End.
- **Workflow em uso**: O jogo está configurado com os estilos base para uso direto. 

### Para Testar Localmente (Via Terminal)

Devido aos recursos de importação do Brython (que fazem requisições XHR como `from antigravity import Canvas`), pode haver problemas de "CORS erro" se você apenas abrir o `file://` no navegador. Desta forma, inicie um pequeno servidor local com python.

Usando Python:
```bash
python -m http.server 8000
```
- Depois, abra no seu navegador: `http://localhost:8000`.

## Hospedagem (GitHub Pages)

Para publicar o jogo no GitHub Pages:
1. Pelo GitHub Desktop, certifique-se de que os arquivos de código (index.html, style.css, antigravity.py, etc.) estão commited.
2. Clique no botão "Publish branch" ou "Push" lá.
3. No site do GitHub, vá na aba **Settings > Pages** do seu repositório.
4. Na seção **Source** (onde diz "Build and deployment"), selecione a branch `main` e a pasta `/(root)`.
5. Salve e aguarde alguns minutos, o jogo estará disponível sob o domínio do seu GitHub Pages! (ex: `https://seu-usuario.github.io/cobrinha/`)
