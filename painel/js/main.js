let produtos = [];

// Atualiza produtos do servidor
async function atualizarProdutos() {
  const res = await fetch("/produtos");
  produtos = await res.json();

  const container = document.getElementById('produtos');
  container.innerHTML = '';
  produtos.forEach(p => {
    const div = document.createElement('div');
    div.innerHTML = `
      <h3>${p.produto}</h3>
      <p>Status: ${p.status}</p>
      <p>Recomendação: ${p.recomendacao || ""}</p>
      <button onclick="aprovar(${p.id})">Aprovar</button>
      <button onclick="rejeitar(${p.id})">Rejeitar</button>
    `;
    container.appendChild(div);
  });
}

// Aprovar produto
async function aprovar(id) {
  await fetch("/produto/atualizar", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({id: id, acao: "aprovar"})
  });
  atualizarProdutos();
}

// Rejeitar produto
async function rejeitar(id) {
  await fetch("/produto/atualizar", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({id: id, acao: "rejeitar"})
  });
  atualizarProdutos();
}

// Simula IA respondendo à pergunta
function enviarPergunta() {
  const pergunta = document.getElementById('pergunta').value.trim();
  const respostaDiv = document.getElementById('resposta');
  if(!pergunta) return;

  let sugestoes = [
    {id: 1, produto: "Curso Avançado Excel", status: "pendente", recomendacao: "Vender agora", link_afiliado: "#", nicho: "Dinheiro"},
    {id: 2, produto: "Template Planilhas Profissionais", status: "pendente", recomendacao: "Vender agora", link_afiliado: "#", nicho: "Dinheiro"}
  ];

  // Atualiza JSON via endpoint (poderíamos criar um endpoint POST /produtos no futuro)
  produtos = sugestoes;
  atualizarProdutos();

  respostaDiv.innerHTML = `<p><strong>IA:</strong> Sugeri ${sugestoes.length} produtos para "${pergunta}"</p>`;
}

atualizarProdutos();
