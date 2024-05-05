import React, { useEffect, useState } from 'react';
import axios from 'axios'; // or use fetch API

export default function Atencion_cliente() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/questions')
      .then(response => {
        setQuestions(response.data);
        console.log(response.data);
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  return (
    <div className="page">
      <div className='page1'>
        <div className="graphs_cont">
          <div id='tiempo' className="graphs1">
            graphica tiempo
          </div>
          <div id='nums' className="graphs1">
            <div className="graphs2">
              <h2 className='info'>80 dudas</h2>
            </div>
            <div className="graphs2">
              <h2 className='info'>68 quejas</h2>
            </div>
          </div>
        </div>
        <div className="graphs_cont">
          <div className="graphs1">
            faq
          </div>
          <div className="graphs1">
            tematicas
          </div>
        </div>
      </div>
      <div className="page2">
        <div className="title">
          Dudas y Preguntas
        </div>
        <div className="questions">
          {questions.map((question, index) => (
            <div key={index}>
              {question}
            </div>
          ))}
            <button onClick={() => console.log('click')}>
            log
            </button>
        </div>
      </div>
    </div>
  );
}