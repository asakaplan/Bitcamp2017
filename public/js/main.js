function deprocess(data) {
    var mult = 10;
    var maxval = data.links.reduce((best, l) =>
        Math.max(best, l[2]), 1);
    return {
        nodes: data.nodes.map(a => ({
            id: a[0],
            name: a[1],
            comp: a[2],
            bad: a[3],
            location_state: a[4],
            location_city: a[5],
            visible: true
        })),
        links: data.links.map(a => ({
            source: a[0], target: a[1],
            value: mult*a[2]/maxval
        }))
    };
}
function removeNode(graph, dedges, node){
  for(var i = dedges.length -1; i >= 0 ; i--){
    if(dedges[i].source==node.id || dedges[i].target==node.id){
        dedges.splice(i, 1);
    }
  }
  index = graph.nodes.indexOf(node);
  if (index>-1){
    graph.nodes.splice(index,1)
  }
  else{
    console.log("Unknown node to be removed: %d",node.id)
  }
}

function addNode(graph, dedges, node, edges){
  dedges = dedges.concat(edges);
  graph.nodes.add(node);
}

function markovProb(dict, dedges, node, P, S, iters) {
    for(var k in dict) dict[k].cur = dict[k].prob = 0;
    node.cur = 1;
    for(var iter=0; iter<iters; iter++) {
        for(var k in dict) dict[k].ncur = 0;
        for(var i in dedges) {
            var e = dedges[i];
            dict[e.target].ncur += dict[e.source].cur * e.value;
        }
        if(iter===iters-1) P=1;
        for(var k in dict) {
            dict[k].cur = dict[k].ncur * (1-P);
            dict[k].prob += dict[k].ncur * P;
        }
    }
    node.sketch = 0;
    var totProb = 0;
    for(var k in dict) {
      totProb += dict[k].prob;
      node.sketch += dict[k].prob*dict[k].bad;
    }
    if(totProb === 0) S = 1;
    node.sketch = S*node.bad + (1-S)*node.sketch;
}
function dirEdges(edges) {
    var seen = {};
    var totals = {};
    var out = [];
    edges.map(e => {
        var st = [e.source, e.target];
        st.sort();
        e.source = st[0], e.target = st[1];
        var key = st.join("'");//apostrophes don't exist in input data
        if(seen[key]) return null;
        seen[key] = true;
        st.forEach(k => totals[k] = (totals[k]||0) + e.value);
        return e;
    }).filter(e => e).forEach(e => {
        var a = Object.assign({}, e),
          b = Object.assign({}, e);
        b.source = a.target; b.target = a.source;
        a.value /= totals[a.source];
        b.value /= totals[b.source];
        out.push(a); out.push(b);
    });
    return out;
}

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20);

var charge =  d3.forceManyBody();
charge.distanceMax(100);
charge.strength(-100);
var grav =  d3.forceManyBody();
grav.strength(8);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", charge)
    .force("grav", grav)
    .force("center", d3.forceCenter(width / 2, height / 2));

var selected = null;

d3.json("/js/data.json", function(error, graph) {
  if (error) throw error;

  var updateNodes = window.updateNodes = function updateNodes(graph, dict, dedgesT){
    //graph.nodes = ;
    graph.nodes.length=0;
    [].push.apply(graph.nodes,Object.keys(dict).map(e => dict[e]).filter(e => e.visible))
    graph.links.length = 0;
    [].push.apply(graph.links,dedgesT.filter(e => {
      console.log(e)
      return (dict[e.source].visible && dict[e.target].visible)
    }).map(o => Object.assign({}, o)));
  }

  var filterCompany = window.filterCompany = function filterCompany(comp) {
    Object.keys(dict).forEach((key,i) => dict[key].visible = (dict[key].comp === comp));
    filter();
  }

  var filterAll = window.filterAll = function filterAll(comp) {
    Object.keys(dict).forEach((key,i) => dict[key].visible = true);
    filter();
  }

  var filterLoc = window.filterLoc = function filterLoc(comp, city, state) {
    Object.keys(dict).forEach((key,i) => dict[key].visible = (dict[key].comp === comp
    && dict[key].location_city === city && dict[key]
    && dict[key].location_state === state));
    filter();
  }

  graph = deprocess(graph);
  var dict = window.dict = {};
  graph.nodes.forEach(n => dict[n.id] = n);
  graph.nodes = Object.keys(dict).map(k => dict[k]);
  var dedges = dirEdges(graph.links);
  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.pow(d.value, 2/3); });
  for(var k in dict) {
    markovProb(dict, dedges, dict[k], 0.4, 0.6, 10);
  }
  window.dedgesStash = dedgesStash = JSON.parse(JSON.stringify(dedges));

  window.filter = function filter(){
    updateNodes(graph,dict,dedgesStash)
    node = node.data(graph.nodes, function(d) { return d.id;});
      node.exit().remove();
      node = node.enter().append("circle").attr("r", 5)
      .attr("fill", function(d) { return d3.hsl((1-Math.pow(d.sketch,1/2.5))*100, 1, 0.5); })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

      // Apply the general update pattern to the links.
      link = link.data(graph.links, function(d) { return d.source.id + "-" + d.target.id; });
      link.exit().remove();
      link = link.enter().append("line").merge(link);

      // Update and restart the simulation.
      simulation.nodes(graph.nodes);
      simulation.force("link").links(graph.links);
      simulation.alpha(1).restart();
      updateSel();

  }
  var node = svg.append("g")
      .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return d3.hsl((1-Math.pow(d.sketch,1/2.5))*100, 1, 0.5); })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));
  var txt = d3.select("#status");

  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
    selected = selected == d ? null : d;
    updateSel();
  }

  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }

  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = d.fy = null;
  }
  updateSel();
  function updateSel() {
    node.attr("class", function(d) { return selected === d ? 'selected' : ''; });
    txt.text(selected ? 'Selected: '+selected.name + ", " + selected.comp+', '+selected.sketch : 'Click on a point...');
    var mostWanted = graph.nodes.slice();
    mostWanted.sort((a,b) => (b.sketch-b.bad)-(a.sketch-a.bad));
    mostWanted.length = 10;
    mostWanted = mostWanted.map(node => ({
        id: node.id,
        name: node.name
    }));
    uiUpdate(Object.assign({
        selected: !!selected
    }, selected ? {
        name: selected.name,
        comp: selected.comp
    } : {}));
    if(!selected) return;
    updateList(mostWanted);
    console.log(selected);
  }


  node.append("title")
      .text(function(d) { return d.name+", "+d.comp; });

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  }
});
