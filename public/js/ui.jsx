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
function updateList(people){
  let rows = [];
  let counter = 0;
  for(person in people){
    counter++;
    rows.push(
      <tr key={person.id}>
        <td>{counter}</td>
        <td>{person.name}</td>
      </tr>
    );
  }
  const table = (
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
  ReactDOM.render(
    table,
    document.getElementById('topSuspects')
  );
}