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
  people.forEach( (person, index) => {
    // if(!person.name) continue;
    rows.push(
      <tr key={person.id}>
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
  ReactDOM.render(
    table,
    document.getElementById('topSuspects')
  );
}