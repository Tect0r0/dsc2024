import React, { useEffect, useState } from 'react';
import axios from 'axios'; // or use fetch API
import { Chart as ChartJS, ArcElement,Tooltip,Legend } from 'chart.js';
import {Chart as ChartJS2, LineElement, CategoryScale, LinearScale, Title, PointElement} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
import {Line} from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);
ChartJS2.register(LineElement, CategoryScale, LinearScale, Title, PointElement);

export default function Atencion_cliente() {
  const [questions, setQuestions] = useState([]);
  const [trendingTopics, setTrendingTopics] = useState([]);
  const [totalDudas, setTotalDudas] = useState<number>(0);
  const [totalQuejas, setTotalQuejas] = useState<number>(0);
  const [dudasByDay, setDudasByDay] = useState([]);
  const [quejasByDay, setQuejasByDay] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/questions')
      .then(response => {
        setTotalDudas(response.data.total_dudas);
        setTotalQuejas(response.data.total_quejas);
        setTrendingTopics(response.data.trending_topics);
   

      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  //Data for the doughnut chart
  const data = {
    labels: ['Dudas', 'Quejas'],
    datasets: [
      {
        data: [82, 23],
        backgroundColor: ['#36A2EB', '#FF6384'],
        hoverBackgroundColor: ['#36A2EB', '#FF6384']
      }
    ]
  };

  

  const options = {
    responsive: true,
    maintainAspectRatio: false
  };

  return (
    <div className="page">
      <div className='page1'>
        <div className="graphs_cont">
          <div id='tiempo' className="graphs1">
 
                 </div>
          <div id='nums' className="graphs1-2">
            <div className='Numeros'>
              <div className="graphs2">
                <h2 className='info'>{totalDudas} <br /> DUDAS</h2>
              </div>
              <div className="graphs2">
                <h2 className='info'>{totalQuejas} <br /> QUEJAS</h2>
              </div>
            </div>
            <div className="graphs3">
             
              <Doughnut data={data} options={options} />

            </div>
          </div>
          
        </div>


        <div className="graphs_cont">
          <div className="graphs1">
            faq
          </div>
          <div className="graphs1">
          <table>
            <thead>
              <tr>
                <th>Tema</th>
                <th>Cantidad</th>
              </tr>
            </thead>
            <tbody>
              {trendingTopics.map((topic, index) => (
                <tr key={index}>
                  <td>{topic.topic}</td>
                  <td>{topic.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
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