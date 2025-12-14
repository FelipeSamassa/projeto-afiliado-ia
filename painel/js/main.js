// Lista inicial de produtos (vazia ou carregada do JSON via backend futuramente)
let produtos = [
  {id: 1, nome: "Curso Excel", status: "pendente", recomendacao: ""},
  {id: 2, nome: "Curso HTML/CSS", status: "pendente", recomendacao: ""}
];

// Função para atualizar a visualização dos produtos
function atualizarProdutos() {
  const container = document.getElementById('produtos');
  container.innerHTML = '';
  produtos.forEach(p => {
    const div = document.createElement('div');
    div.innerHTML = `
      <h3>${p.nome}</h3>
      <p>Status: ${p.status}</p>
      <p>Recomendação: ${p.recomendacao}</p>
      <button onclick="aprovar(${p.id})">Aprovar</button>
      <button onclick="rejeitar(${p.id})">Rejeitar</button>
    `;
    container.appendChild(div);
  });
}

// Aprovar produto
function aprovar(id) {
  const produto = produtos.find(p => p.id === id);
  if(produto) produto.status = "aprovado";
  atualizarProdutos();
}

// Rejeitar produto
function rejeitar(id) {
  const produto = produtos.find(p => p.id === id);
  if(produto) produto.status = "rejeitado";
  atualizarProdutos();
}

// Função para "conversar com a IA"
function enviarPergunta() {
  const pergunta = document.getElementById('pergunta').value.trim();
  const respostaDiv = document.getElementById('resposta');

  if(!pergunta) return;

  // Simulação inicial da IA
  // Aqui você poderia chamar uma API Python/ChatGPT real
  let sugestoes = [];

  if(pergunta.toLowerCase().includes("subnicho")) {
    sugestoes = [
      {nome: "Curso Avançado Excel", recomendacao: "Vender agora"},
      {nome: "Curso Intermediário Excel", recomendacao: "Aguardar"},
      {nome: "Template Planilhas Profissionais", recomendacao: "Vender agora"}
    ];
  } else {
    sugestoes = [
      {nome: "Produto Exemplo 1", recomendacao: "Vender agora"},
      {nome: "Produto Exemplo 2", recomendacao: "Aguardar"}
    ];
  }

  // Atualiza lista de produtos
  produtos = sugestoes.map((p, idx) => ({id: idx+1, ...p, status: "pendente"}));
  atualizarProdutos();

  respostaDiv.innerHTML = `<p><strong>IA:</strong> Sugeri ${sugestoes.length} produtos para "${pergunta}"</p>`;
}

atualizarProdutos();
