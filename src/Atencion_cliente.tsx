

export default function Atencion_cliente(){
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

                </div>
            </div>
        </div>
    )
}