function buildPlot() {
  url1 = "/Charts/AgeBin"
  d3.json(url1).then(function(response) {

    console.log(response);
    var trace = {
      type: "scatter",
      name: "Audience Count by AgeBins",
      x: response.map(data => data.AgeBin),
      y: response.map(data => data.AudienceCount),
      line: {
        color: "#17BECF"
      }
    };
    var data = [trace];
    var layout = {
        title: "Audience Count by AgeBins"
    };
    Plotly.newPlot("plot", data,layout);

  });
}

function buildPlot1() {
  url2 = "/Charts/Gender"
  d3.json(url2).then(function(response) {

    console.log(response);
    var trace = {
      type: "scatter",
      name: "Audience Count by Gender",
      x: response.map(data => data.Gender),
      y: response.map(data => data.AudienceCount),
      line: {
        color: "#17BECF"
      }
    };
    var data = [trace];
    var layout = {
        title: "Audience Count by Gender"
    };
    Plotly.newPlot("plot1", data,layout);

  });
}

function buildbar1() {
  url3="/Charts/CreditScore"
  d3.json(url3).then(function(data) {
      console.log(data);
      var data = [data];
      var layout = {
          title: "Audience Count by CreditScore"
      };
      Plotly.plot("bar1", data, layout);
  });
}

function buildbar2() {
  url4="/Charts/Household_Income"
  d3.json(url4).then(function(data) {
      console.log(data);
      var data = [data];
      var layout = {
          title: "Audience Count by Household Income"
      };
      Plotly.plot("bar2", data, layout);
  });
}
buildPlot();
buildPlot1();
buildbar1();
buildbar2();