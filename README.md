# quarto

Modelador de quartos no navegador. Um único arquivo: abra `quarto.html` (Linux/Windows/Mac). Precisa de internet só para baixar o three.js 0.160 (jsdelivr).

## O que tem

- **35 móveis com modelo 3D procedural**: camas (casal, queen, solteiro, beliche), guarda-roupas, armário, cômoda, criado-mudo, arara, escrivaninha, mesas, cadeiras, cadeira de escritório, pufe, poltrona, sofás, estantes com livros, nichos, prateleira de parede, rack, tapetes, plantas, luminárias, espelho, TV, computador, notebook…
- **Estrutura**: portas (abrem de verdade, com dobradiça/lado configuráveis), janelas (divisões, peitoril, cortina) e pôsteres com moldura. Portas e janelas furam a parede.
- **Vistas**: 3D, planta 2D (com grade, cotas de distância até as paredes e nomes) e 🚶 andar dentro do quarto (WASD + mouse).
- **Ímã**: encaixa em paredes e outros móveis, vira o móvel de costas pra parede; itens pequenos pousam em cima de mesas/cômodas. Móveis batendo uns nos outros ou bloqueando a porta ficam com o chão vermelho.
- Pisos com textura (madeira, porcelanato, cimento, carpete), paredes com cor ou papel de parede, rodapé, hora do dia (dia/entardecer/noite, com luminárias acesas), sombras.
- Desfazer/refazer, autosave no navegador, salvar/abrir `.json` (imagens embutidas), foto do quarto em PNG, exemplos prontos. Atalhos: tecla `?`.

## Como o código funciona

- `state` (`room`, `walls[4]`, `objs[]` com `kind` = `item|door|window|poster`) é a única fonte da verdade; `sync()` atualiza a cena de forma incremental (cada objeto só é reconstruído quando muda a geometria; arrastar só move).
- Modelos: `def(tipo, meta, build)` recebe um `kit` (`b` caixa, `rb` caixa arredondada, `cy` cilindro, `el` elipsoide); tudo com o mesmo material é fundido em um mesh só. O catálogo (`CATALOG`) liga nome/tamanho/cor padrão a um tipo de modelo; as miniaturas são renderizadas dos próprios modelos.
- Móveis: a frente aponta para +z local; `rot` = 0/90/180/270 vira para Fundo→Frente / Esquerda→ / … (`FACE_ROT` dá a rotação de costas pra cada parede).
- Paredes: 0=Fundo (z=0), 1=Direita (x=W), 2=Frente (z=D), 3=Esquerda (x=0). Objetos de parede usam `wall` + `pos` (centro ao longo da parede). São planos de um lado só virados pra dentro, então a parede entre a câmera e o quarto some sozinha.
- Imagens ficam em `assets` (id → data URL), reduzidas a 2048 px ao importar; o projeto salvo carrega só as usadas. Arquivos antigos (v1) são migrados ao abrir.
