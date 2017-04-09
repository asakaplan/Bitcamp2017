function uiUpdate(o) {
  const nodeInfo = (
    <div>
      <h2>{o.name}</h2>
      <h3>{o.comp}</h3>
      <button onClick={window.filterCompany.bind(null,o.comp)} type="button" className="btn btn-primary">⛷ Corporation</button>
    </div>
  );
  const unselected = (<div><h3>Select a node...</h3></div>);
  ReactDOM.render(
    o.selected ? nodeInfo : unselected,
    document.getElementById('nodeInfo')
  );
}
document.getElementById('back').onclick = () => window.filterAll();
function updateList(people, id='topSuspects', title='Top Suspects'){
  let rows = [];
  people.forEach( (person, index) => {
    let pick = () => {
      window.selected = person;
      window.updateSel();
    }
    // if(!person.name) continue;
    rows.push(
      <tr className='abtn' onClick={pick} key={person.id}>
        <td>{index+1}</td>
        <td>{person.name}</td>
      </tr>
    );
  });
  
  let table = (
    <table className="table">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
  // if(!rows.length) table = <span></span>;
  if(title){
    ReactDOM.render(
      <h2>{title}</h2>,
      document.getElementById(id+'Title')
    );
  }
  ReactDOM.render(
    table,
    document.getElementById(id)
  );
}