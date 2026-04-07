import { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import axios from 'axios'
import Navbar from './components/Navbar'
import { CartProvider, useCart } from './contexts/CartContext' // <--- Importação Nova

// --- Componente Home (Atualizado com o botão de comprar) ---
function Home() {
  const [produtos, setProdutos] = useState([])
  const [erro, setErro] = useState(null)
  const { adicionarAoCarrinho } = useCart() // <--- Usando o "Cérebro"

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/produtos/')
      .then(res => setProdutos(res.data))
      //.catch(err => console.error(err))
      .catch(err => setErro("Erro ao buscar produtos. O Django está rodando?"))
  }, [])

  return (
    <div className="container mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-gray-800 mb-6">Produtos em Destaques:</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {produtos.map(p => (
          <div key={p.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition duration-300 flex flex-col h-full">
            <div className="h-48 flex items-center justify-center bg-gray-200">
              {p.foto ? (
                <img src={p.foto} alt={p.nome} className="h-full w-full object-cover" />
              ) : <span className="text-4xl">📷</span>}
            </div>
            <div className="p-4 flex-1 flex flex-col">
              <h3 className="text-xl font-bold mb-2 text-gray-800">{p.nome}</h3>
              <p className="text-blue-600 text-2xl font-bold my-2">R$ {p.preco}</p>
              
              {/* Botão agora chama a função do Contexto */}
              <button 
                onClick={() => adicionarAoCarrinho(p)}
                className="w-full mt-auto bg-blue-600 text-white py-2 rounded hover:bg-blue-700 font-bold transition"
              >
                Comprar
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

function Carrinho() {
  return <h1 className="text-center mt-10 text-2xl">🛒 Em breve: Lista de produtos</h1>
}

function Login() {
  return <h1 className="text-center mt-10 text-2xl">🔐 Login</h1>
}

function App() {
  return (
    // O CartProvider envolve TUDO para que todos tenham acesso
    <CartProvider>
      <BrowserRouter>
        <div className="min-h-screen bg-gray-100">
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/carrinho" element={<Carrinho />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
      </BrowserRouter>
    </CartProvider>
  )
}

export default App