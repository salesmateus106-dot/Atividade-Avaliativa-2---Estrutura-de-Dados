#include <iostream>
#include <vector>
#include <clocale>

using namespace std;

// Estrutura para armazenar o resultado da busca de cada matriz
struct ResultadoBusca {
    bool encontrado;
    int linha;
    int coluna;
    int comparacoes;
};

// Função de busca sequencial usando loops aninhados
ResultadoBusca buscaSequencialMatriz(const vector<vector<int>>& matriz, int valorProcurado) {
    int linhas = matriz.size();
    int colunas = matriz[0].size();
    int contComparacoes = 0;

    for (int l = 0; l < linhas; ++l) {
        for (int c = 0; c < colunas; ++c) {
            contComparacoes++;
            if (matriz[l][c] == valorProcurado) {
                return {true, l, c, contComparacoes};
            }
        }
    }
    return {false, -1, -1, contComparacoes};
}

// Função auxiliar para criar matrizes preenchidas sequencialmente
vector<vector<int>> criarMatriz(int n) {
    vector<vector<int>> matriz(n, vector<int>(n));
    int contador = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matriz[i][j] = contador++;
        }
    }
    return matriz;
}

// Função para rodar e exibir os testes mostrando a localização exata da linha
void rodarExperimento(int dimensao) {
    auto matriz = criarMatriz(dimensao);
    int totalElementos = dimensao * dimensao;

    int valorInicio = 1;
    int valorFinal = totalElementos;
    int valorInexistente = totalElementos + 999;

    ResultadoBusca rInicio = buscaSequencialMatriz(matriz, valorInicio);
    ResultadoBusca rFinal = buscaSequencialMatriz(matriz, valorFinal);
    ResultadoBusca rInexistente = buscaSequencialMatriz(matriz, valorInexistente);

    cout << "Matriz " << dimensao << "x" << dimensao << " (" << totalElementos << " elementos):\n";
   
    cout << "  - Busca no Inicio (valor " << valorInicio << "): " << rInicio.comparacoes << " comparacoes. ";
    cout << "[Encontrado: " << (rInicio.encontrado ? "Sim" : "Nao") << " | Linha: " << rInicio.linha << " | Coluna: " << rInicio.coluna << "]\n";

    cout << "  - Busca no Final  (valor " << valorFinal << "): " << rFinal.comparacoes << " comparacoes. ";
    cout << "[Encontrado: " << (rFinal.encontrado ? "Sim" : "Nao") << " | Linha: " << rFinal.linha << " | Coluna: " << rFinal.coluna << "]\n";

    cout << "  - Valor Inexistente (valor " << valorInexistente << "): " << rInexistente.comparacoes << " comparacoes. ";
    cout << "[Encontrado: " << (rInexistente.encontrado ? "Sim" : "Nao") << " | Linha: " << rInexistente.linha << " | Coluna: " << rInexistente.coluna << "]\n\n";
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    cout << "INVESTIGACAO DE BUSCA EM MATRIZES";

    rodarExperimento(2);   // Matriz 2x2
    rodarExperimento(10);  // Matriz 10x10
    rodarExperimento(100); // Matriz 100x100

    return 0;
}

/*

Questionário Analítico
a) Por que encontrar um elemento no início exige menos operações?
Porque o algoritmo analisa as posições da matriz de forma linear e sequencial, começando da primeira célula até a última. Caso o valor de interesse esteja na primeira posição, ele é identificado na primeira verificação. Desse modo, o algoritmo encerra a execução imediatamente sem varrer o restante da memória, configurando o cenário ideal conhecido como Melhor Caso.
b) O que acontece quando o elemento procurado não existe?
O algoritmo executa uma varredura completa na estrutura de dados. Como o programa não possui informação prévia sobre o conteúdo das próximas posições, ele precisa checar exaustivamente cada elemento disponível. A confirmação de que o valor é inexistente só pode ser dada após o término da leitura de todos os índices da matriz.
c) Qual é o pior caso da busca sequencial?
O pior caso se manifesta sob duas condições equivalentes em esforço computacional: quando o item pesquisado está alocado na última posição física da matriz ou quando ele não pertence ao conjunto de dados estudado. Nessas situações, o laço de repetição obrigatoriamente atinge o seu limite máximo de iterações.
d) Como o aumento das dimensões da matriz influencia a quantidade de operações?
A relação de escala ocorre de forma diretamente proporcional (linear) com respeito ao volume populacional de células da matriz. Se as dimensões mudarem de 10×10 (100 itens) para 100×100 (10.000 itens), o montante total de registros cresce 100 vezes. Consequentemente, a taxa de loops operacionais no pior cenário também é multiplicada exatamente por 100.
e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?
Em termos formais pela notação assintótica, a complexidade temporal no pior caso é descrita como \(O(m \times n)\), onde \(m\) representa as linhas e \(n\) as colunas. Considerando que o tamanho global da entrada de dados é dado por \(N = m \times n\), o comportamento do algoritmo segue o padrão linear simplificado \(O(N)\).


*/