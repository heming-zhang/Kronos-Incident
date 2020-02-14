<template>
  <div>
    <h1>Kronos Incident</h1>
    <div id="search">
      <div id="name-search">
        <strong>Name:</strong>
        <select v-model="name" class="select" style="width:120px;">
            <option disabled value selected>--Name--</option>
            <option>All Employee</option>
            <option v-for="(pinfo, index) in personal_info" :key="index">{{pinfo.firstname}} {{pinfo.lastname}}</option>
        </select>
      </div>
      <div id="time-search">
        <strong>From:</strong>
        <select v-model="start_date" class="time" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="start_hour" class="time" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="start_minute" class="time" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>To:</strong>
        <select v-model="end_date" class="time" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="end_hour" class="time" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="end_minute" class="time" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        <br>
        <button @click="searchRange">Search</button>
      </div>
    </div>
    <div>
      <div id="point"></div>
      <div id="map"></div>
    </div>
    <div id = "card">
      <!-- <ul>
        <li v-for="(d, index) in card_info" :key="index">{{d.type}} : {{d.location}}, 
          {{d.timestamp}}, {{d.price}}, {{d.name}}</li><br>
      </ul> -->
       <table style="width:100%">
        <tr>
          <th>Type</th>
          <th>Location</th>
          <th>Time</th>
          <th>Price</th>
          <th>Name</th>
        </tr>
        <tr v-for="(d, index) in card_info" :key="index">
          <th>{{d.type}}</th>
          <th>{{d.location}}</th>
          <th>{{d.timestamp}}</th>
          <th>{{d.price}}</th>
          <th>{{d.name}}</th>
        </tr>
      </table> 
    </div>
    <div id = "histogram">
    </div>
    <div id = "wordcloud">
    </div>
    <div id = "bottom">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchGps",
  data() {
    return {
      personal_info: [],
      time_info: [],
      gps_info: "",
      card_info: "",
      slot_info: "",
      dataset: [],
      name: "",
      firstname: "",
      lastname: "",
      start_date: "",
      start_hour: "",
      start_minute: "",
      end_date: "",
      end_hour: "",
      end_minute: ""
    };
  },

  mounted() {
    // generate page when first load
    axios.get("/api/init_person")
          .then(response => (this.personal_info = response.data));
    axios.get("/api/init_time")
          .then(response => (this.time_info = response.data));
  },

  methods: {
    searchRange: async function(){
      if(this.start_date == ""){
        alert("Please Input Date");
      }else{
        let time_start = "14-1-" + this.start_date + " " + this.start_hour + ":" + this.start_minute
        let time_end = "14-1-" + this.end_date + " " + this.end_hour + ":" + this.end_minute
        console.log(time_start);
        console.log(time_end);
        let firstname;
        let lastname;
        if(this.name == "All Employee"){
          firstname = "";
          lastname = "";
        }else{
          firstname = this.name.split(' ', 1)[0];
          lastname = this.name.slice(this.name.indexOf(' ')+1);
        }
        const res = await axios.get('api/search_gps', {
          params: {
            firstname: firstname,
            lastname: lastname,
            time_start: time_start,
            time_end: time_end
            }
          }
        );
        const res_card = await axios.get('api/search_card', {
          params: {
            firstname: firstname,
            lastname: lastname,
            time_start: time_start,
            time_end: time_end
            }
          }
        );
        const res_date = await axios.get('api/search_hist', {
          params: {
              time_start: time_start
            }
          }
        );
        // this.gps_info = JSON.stringify(res.data);
        this.gps_info = res.data;
        this.card_info = res_card.data;
        this.slot_info = res_date.data;
        let present = "14/1/" + this.start_date
        this.render();
        this.histplot(present);
      }
    },

    histplot: function(present){
      var delete_svg = document.getElementById("hist")
      if(delete_svg != null){
        delete_svg.remove();
      }
      let histset = [];
      histset = this.slot_info;

      let title = present + " " + "GPS Track distribution"
      var margin = {top: 10, right: 30, bottom: 30, left: 40}
      var width = 600 - margin.left - margin.right;
      var height = 320 - margin.top - margin.bottom;
      var binwidth = width/12;

      var yScale = d3.scaleLinear()
        .domain([0, d3.max(histset, function(d,i){return d.number})])
        .range([height, 0]);
      var xScale = d3.scaleLinear()
        .domain([0, d3.max(histset, function(d,i){return d.slot})])
        .range([0, width]);

      var histogram = d3.histogram()
        .value(function(d) { return d.number; })   // I need to give the vector of value
        .domain(xScale.domain())  // then the domain of the graphic
        .thresholds(xScale.ticks(4)); // then the numbers of bins

      var svg = d3.select("#histogram")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        
      var bar = svg.selectAll(".bar")
        .data(histset)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return xScale(d.slot-2); })
        .attr("width", binwidth)
        .attr("y", function(d) { return yScale(d.number); })
        .attr("height", function(d) { return height - yScale(d.number); })
        
      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));
      svg.append("g")
        .call(d3.axisLeft(yScale));

      // Add axis labels
      svg.append("text")
          .attr("class", "x label")
          .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.bottom - 15) + ")")
          //.attr("dy", "1em")
          .attr("text-anchor", "middle")
          .text("Every 2 hours");
          
      svg.append("text")
          .attr("class", "y label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - margin.left)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .attr("text-anchor", "middle")
          .text("Count");
          
      // Add title to chart
      svg.append("text")
          .attr("class", "title")
          .attr("transform", "translate(" + (width / 2) + " ," + (-20) + ")")
          //.attr("dy", "1em")
          .attr("text-anchor", "middle")
          .text(title);
    },




    render: function(){
      var delete_svg = document.getElementById("canvas")
      if(delete_svg != null){
        delete_svg.remove();
      }
      //Create SVG element
      let w = 600;
      let h = 300;
      let svg = d3.select("#point")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h)
                  .attr("id", "canvas");
      
      let tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html(function(d) {
                return "<span style='color:violet'>" + d.firstname + " " + d.lastname + 
                "</span><br>TimeStamp:<span style='color:pink'>" + d.timestamp
        })

      let x = d3.scaleLinear()
        .domain([24.82508806, 24.90848537])
        .range([0, w]);         
      let y = d3.scaleLinear()
        .domain([36.04802098, 36.08995956])
        .range([h, 0]);
      let dataset = [];
      dataset = this.gps_info;

      svg.call(tip)
      svg.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr('r', 1)
        .attr('cx', function(d) { return x(d['longtitude']) })
        .attr('cy', function(d) { return y(d['latitude']) })
        .attr("width", 2)
        .attr("height", 2)
        .attr("fill", function(d, index){
          return "gray"
        })
        .attr("x", (d) => x(d.longtitude))
        .attr("y", (d) => y(d.latitude))
        .attr("stroke", "black")
		    .attr("stroke-width",0.2)
        .on('mouseover', function(d){
          d3.select(this)
          .attr("fill", "#1E90FF")
          .attr("r", 5)
          .style("opacity", 0.9);
          tip.show(d);
        })
        .on('mouseout', function(d){
          d3.select(this)
          .attr("fill", "gray")
          .attr("r", 1);
          tip.hide(d);
        })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  text-align: center;
}

h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}




#search {
  height: 100px;
  text-align: center;
}

#map {
  background-image: url(../../../backend/patterns/A2_Data/MC2-tourist.jpg);
  background-size: 600px 320px;
  background-repeat: no-repeat;
  opacity: 0.7;
  width: 600px;
  height: 350px;
  position: absolute;
  top: 230px;
  z-index: -1;
}

#point {
  width: 600px;
  height: 300px;
  position: absolute;
  top: 230px;
  z-index: 0;
}

#card {
  position: absolute;
  left: 55%;
  height: 320px;
  top: 230px;
  width: 500px;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
  font-size: 12px;
}

#histogram {
  position: absolute;
  height: 320px;
  top: 600px;
  width: 600px;
  border: 1px solid black;
  border-radius: 2px;
  /* font-size: 12px; */
}

#wordcloud {
  position: absolute;
  left: 55%;
  height: 320px;
  top: 600px;
  width: 500px;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
  font-size: 12px;
}

#bottom {
  position: absolute;
  height: 20px;
  width: 200px;
  top: 1000px;
}

.d3-tip {
    line-height: 1;
    font-weight: bold;
    padding: 12px;
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    border-radius: 2px;
    z-index: 1;
  }
</style>
