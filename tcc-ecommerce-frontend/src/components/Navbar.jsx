import { Link } from 'react-router-dom';
import { useCart } from '../contexts/CartContext'; // <--- Importar o gancho

function Navbar() {
  const { carrinho } = useCart(); // <--- Pegar a lista de compras

  return (
    <nav className="bg-blue-600 shadow-lg sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center py-4">
          <Link to="/" className="text-white text-2xl font-bold">
            🏪 Loja TCC
          </Link>
          
          <div className="space-x-6 flex items-center">
            <Link to="/" className="text-white hover:text-blue-200 font-medium">Home</Link>
            
            <Link to="/carrinho" className="relative text-white hover:text-blue-200 font-medium flex items-center">
              🛒 Carrinho
              {/* Bolinha vermelha com a quantidade */}
              {carrinho.length > 0 && (
                <span className="ml-2 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded-full">
                  {carrinho.length}
                </span>
              )}
            </Link>

            <Link to="/login" className="bg-white text-blue-600 px-4 py-2 rounded hover:bg-gray-100 font-bold">
              Entrar
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;