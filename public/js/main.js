function markovProb(dict, edges, node, P, k) {
    for(var k in dict) dict[k].cur = dict[k].prob = 0;
    node.cur = 1;
    for(var i=0; i<k; i++) {
        for(var k in dict) dict[k].ncur = 0;
        for(var i in edges) {
            var e = edges[i];
            dict[e.b].ncur += dict[e.a].cur * e.w;
        }
        if(i===k-1) P=1;
        for(var k in dict) {
            dict[k].cur = dict[k].ncur * (1-P);
            dict[k].prob += dict[k].ncur * P;
        }
    }
}

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

var selected = null;

d3.json("/js/data.json", function(error, graph) {
  if (error) throw error;
  var dict = {};
  graph.nodes.forEach(n => dict[n.id] = n);

  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.append("g")
      .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return color(d.group); })
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
    txt.text(selected ? 'Selected: '+selected.id : 'Click on a point...')
  }


  node.append("title")
      .text(function(d) { return d.id; });

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
