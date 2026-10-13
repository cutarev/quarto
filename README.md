# quarto

Modelador de quarto simples, estilo modo construção do The Sims. Um único arquivo: abra `quarto.html` no navegador (Linux/Windows). Precisa de internet (three.js 0.160 via jsdelivr).

- Quarto retangular (cm), portas, janelas (furam a parede), móveis como caixas com nome no topo.
- Vista 2D (ortográfica de cima) e 3D (orbit), tecla `V` alterna.
- Pôsteres e papel de parede a partir de PNG/JPG; salvar/abrir `.json` com as imagens embutidas como data URL.

## Como o código funciona

- `state` (`room`, `walls[4]`, `objs[]` com `kind` = `item|door|window|poster`) é a única fonte da verdade; `rebuild()` refaz a cena inteira a cada mudança.
- Paredes: 0=Fundo (z=0), 1=Direita (x=W), 2=Frente (z=D), 3=Esquerda (x=0). Objetos de parede usam `wall` + `pos` (centro ao longo da parede).
- Paredes são planos de um lado só virados pra dentro: a parede entre a câmera e o quarto some sozinha (cutaway).
- Texturas ficam em cache por objeto do estado (`cachedTex`), pra não reenviar imagem pra GPU a cada arraste.
