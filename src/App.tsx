import { useState } from 'react';
import Logo from './assets/hey-banco-logo-white.svg';
import General from './General';
import Atencion_cliente from './Atencion_cliente';

type PageName = 'Inicio' | 'Atencion_cliente'; // Define the names of the pages

export default function App() {
  const [page, setPage] = useState<PageName | "">("")

  const pages: Record<PageName, JSX.Element> = { // Create an object with the pages
    "Inicio": <General />,
    "Atencion_cliente": <Atencion_cliente />,
  }

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
              Atención a cliente
            </button>
          </div>
        </div>
      </header>
      <body className='page_cont'>
        {page ? pages[page as PageName] : <General />} {/* If there is a value, use the value as the page */}
      </body>
    </>
  )
}