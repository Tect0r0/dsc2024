import { useEffect, useState } from 'react';
import axios from 'axios'; // or use fetch API
import { Chart as ChartJS, ArcElement,Tooltip,Legend } from 'chart.js';
import {Chart as ChartJS2, LineElement, CategoryScale, LinearScale, Title, PointElement} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);
ChartJS2.register(LineElement, CategoryScale, LinearScale, Title, PointElement);

export default function Atencion_cliente() {
  
  interface TrendingTopic {
    topic: string;
    count: number;
  }

  const [trendingTopics, setTrendingTopics] = useState<TrendingTopic[]>([]);
  const [totalDudas, setTotalDudas] = useState<number>(0);
  const [totalQuejas, setTotalQuejas] = useState<number>(0);
  
  const [questions, setQuestions] = useState([]);
  const [selectedQuestion, setSelectedQuestion] = useState<number>(0);
  const [answer, setAnswer] = useState('');


  useEffect(() => {
    axios.get('http://localhost:5000/questions')
      .then(response => {
        setTotalDudas(response.data.total_dudas);
        setTotalQuejas(response.data.total_quejas);
        setTrendingTopics(response.data.trending_topics);
        setQuestions(response.data.questions);
   

      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setAnswer(event.target.value);
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    console.log('handleSubmit called')
    event.preventDefault();

    const question = questions[selectedQuestion];

    axios.post('http://localhost:5000/answer', {
      question: question,
      answer: answer
    })
    .then(response => {
      console.log(response.data);
      setAnswer('');
    })
    .catch(error => {
      console.error('There was an error!', error);
    });
    setTimeout(() => {window.location.reload();}, 2000);
  }

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
            <iframe title="Datathon_HeyBanco_Quejas" width="100%" height="100%" src="https://app.powerbi.com/view?r=eyJrIjoiZDQxZTg5NmYtNzRlMy00NTA2LWEwZWYtZGQ0YmU3MTk1ZDg1IiwidCI6ImM2NWEzZWE2LTBmN2MtNDAwYi04OTM0LTVhNmRjMTcwNTY0NSIsImMiOjR9" allowFullScreen></iframe>
          </div>
          <div id='tiempo' className="graphs1">
          <iframe title="Datathon_HeyBanco_Dudas" width="100%" height="100%" src="https://app.powerbi.com/view?r=eyJrIjoiMTE1YWFkMmQtZDYyZS00YzkzLTg2YmYtNTY2Mzk2M2FhMWQwIiwidCI6ImM2NWEzZWE2LTBmN2MtNDAwYi04OTM0LTVhNmRjMTcwNTY0NSIsImMiOjR9" allowFullScreen></iframe>
          </div>
        </div>
        <div className="graphs_cont">
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
            <div className={`mensaje ${index === selectedQuestion ? 'expanded' : 'collapsed'}`} key={index} onClick={() => setSelectedQuestion(index)}>
              {question}
            </div>
          ))}
        </div>
        <form className='answer' onSubmit={handleSubmit}>
            <input 
              type="text" 
              id="answer" 
              name="answer" 
              placeholder=""
              autoComplete='off'
              value={answer}
              onChange={handleInputChange}/>
            <button className='submit_butt' type="submit">Enviar</button>
        </form>
      </div>
    </div>
  );
}