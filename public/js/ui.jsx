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
    document.getElementById('root')
  );
}
