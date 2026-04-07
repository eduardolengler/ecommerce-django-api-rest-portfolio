import { createContext, useState, useContext } from 'react';

// 1. Cria o contexto (a "nuvem" de dados)
const CartContext = createContext();

// 2. Cria o Provedor (o componente que envolve o site e fornece os dados)
export function CartProvider({ children }) {
  const [carrinho, setCarrinho] = useState([]);

  // Função para adicionar produto
  const adicionarAoCarrinho = (produto) => {
    setCarrinho((listaAtual) => [...listaAtual, produto]);
    alert(`✅ ${produto.nome} adicionado ao carrinho!`);
  };

  // Função para limpar (usaremos depois)
  const limparCarrinho = () => {
    setCarrinho([]);
  };

  return (
    <CartContext.Provider value={{ carrinho, adicionarAoCarrinho, limparCarrinho }}>
      {children}
    </CartContext.Provider>
  );
}

// 3. Cria um atalho para usar esses dados facilmente
export const useCart = () => useContext(CartContext);