// All the charts for the app

// Plotly API https://plot.ly/javascript/reference/
const scatterLineColor = "#5A8C7A";
const scatterHoverBgColor = "#393E40";
const scatterFontColor = "#F2F2F2";
const scatterFontFamily = '"Noto Sans SC", sans-serif';
const scatterMarkerType = "circle-open";
const scatterLineMarkerWidth = 4;
const scatterMarkerSize = 20;

// Age
function ageChart() {
  ageURL = "/charts/age";
  d3.json(ageURL).then(function(response) {
    var trace = {
      type: "scatter",
      name: "Audience Count by Age",
      x: response.map(data => data.AgeBin),
      y: response.map(data => data.AudienceCount),
      line: {
        color: scatterLineColor,
        width: scatterLineMarkerWidth
      },
      marker: {
        symbol: scatterMarkerType,
        size: scatterMarkerSize,
        line: {
          width: scatterLineMarkerWidth
        }
      },
      font: {
        family: scatterFontFamily,
        color: scatterFontColor
      },
      hoverlabel: {
        bgcolor: scatterHoverBgColor,
        font: {
          family: scatterFontFamily,
          color: scatterFontColor
        }
      }
    };
    var data = [trace];
    var layout = {
      title: "Audience Count by Age"
    };
    Plotly.newPlot("ageChart", data, layout);
  });
}

// Gender
function genderChart() {
  genderURL = "/charts/gender";
  d3.json(genderURL).then(function(response) {
    var trace = {
      type: "scatter",
      name: "Audience Count by Gender",
      x: response.map(data => data.Gender),
      y: response.map(data => data.AudienceCount),
      line: {
        color: scatterLineColor,
        width: scatterLineMarkerWidth
      },
      marker: {
        symbol: scatterMarkerType,
        size: scatterMarkerSize,
        line: {
          width: scatterLineMarkerWidth
        }
      },
      font: {
        family: scatterFontFamily,
        color: scatterFontColor
      },
      hoverlabel: {
        bgcolor: scatterHoverBgColor,
        font: {
          family: scatterFontFamily,
          color: scatterFontColor
        }
      }
    };
    var data = [trace];
    var layout = {
      title: "Audience Count by Gender"
    };
    Plotly.newPlot("genderChart", data, layout);
  });
}

// Credit score
function creditScoreChart() {
  creditScoreURL = "/charts/credit-score";
  d3.json(creditScoreURL).then(function(data) {
    var data = [data];
    var layout = {
      title: "Audience Count by Credit Score"
    };
    Plotly.plot("creditScoreChart", data, layout);
  });
}

// Household income
function houseHoldChart() {
  houseHoldURL = "/charts/household-income";
  d3.json(houseHoldURL).then(function(data) {
    var data = [data];
    var layout = {
      title: "Audience Count by Household Income"
    };
    Plotly.plot("householdIncomeChart", data, layout);
  });
}

// Build all the charts
ageChart();
genderChart();
creditScoreChart();
houseHoldChart();
