// const canvas = d3.select("canvas");
const svg = d3.select("svg");
const group = svg.append('g');

group.append('circle')
  .attr('r', 50)
  .attr('cx', 300)
  .attr('cy', 70)
  .attr('fill', 'pink');