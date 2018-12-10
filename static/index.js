// const canvas = d3.select("canvas");
const svg = d3.select("svg");
const group = svg.append('g');
d3.json('~/projects/home-projects/static/d.json').then(data =>{
  const circs = svg.selectAll('circle')
    .data(data);
  
  console.log(circs);
  
  circs.attr('cy', d => d.fields.cy)
        .attr('cx', d => d.fields.cx)
        .attr('r', d => d.fields.r)
        .attr('cy', d => d.fields.cy)
        .attr('fill', d => d.fields.fill);
  console.log(circs);
  
  circs.enter()
    .append('circle')
      .attr('cx', d => d.fields.fields.cx)
      .attr('r', d => d.fields.fields.r)
      .attr('cy', d => d.fields.fields.cy)
      .attr('fill', d => d.fields.fields.fill);
  console.log(circs);
})
group.append('circle')
  .attr('r', 50)
  .attr('cx', 300)
  .attr('cy', 70)
  .attr('fill', 'pink');