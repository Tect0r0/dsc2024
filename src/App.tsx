import { useState, useEffect } from 'react';
import Logo from './assets/hey-banco-logo-white.svg';
import General from './General';
import Atencion_cliente from './Atencion_cliente';

type PageName = 'Inicio' | 'Atencion_cliente'; // Define the names of the pages

export default function App() {
  const [page, setPage] = useState<PageName | "">( () => {
  
  const savedPage = localStorage.getItem('page');
    return savedPage as PageName || "Inicio";
  })

  const pages: Record<PageName, JSX.Element> = { // Create an object with the pages
    "Inicio": <General />,
    "Atencion_cliente": <Atencion_cliente />,
  }

  useEffect(() => {
    // Save the current page to localStorage whenever it changes
    localStorage.setItem('page', page);
  }, [page]);

  return (
    <>
      <header>
        <div className='top_header'>
          <div className='logo_cont'><img className='logo' src={Logo} alt="logo"></img></div>
          <div className='nav_cont'>
            <button 
              id='inicio'
              style={{textDecoration: page === "Inicio" ? "underline" : ""}}
              onClick={() => setPage("Inicio")}
            >
              General
            </button>
            <button 
              id='atencion_cliente'
              style={{textDecoration: page === "Atencion_cliente" ? "underline" : ""}}
              onClick={() => setPage("Atencion_cliente")}
            >
              Atención al cliente
            </button>
          </div>
        </div>
      </header>
      <body className='page_cont'>
        {page ? pages[page as PageName] : <General />} {/* If there is a value, use the value as the page */}
      </body>
      <footer>
        <p>“Hey, Banco” es una marca registrada propiedad de Banco Regional S.A. Institución de Banca Múltiple Banregio Grupo Financiero © 2022 Hey, Inc.</p>
      </footer>
    </>
  )
}