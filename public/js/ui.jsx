function uiUpdate(o) {
  const nodeInfo = (
    <div>
      <h2>{o.name}</h2>
      <h3>{o.comp}</h3>
    </div>
  );
  const unselected = (<div><h3>Select a node...</h3></div>);
  ReactDOM.render(
    o.selected ? nodeInfo : unselected,
    document.getElementById('nodeInfo')
  );
}
function updateList(people){
  let rows = [];
  let counter = 0;
  for(person in people){
    counter++;
    rows.push(
      <tr>
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