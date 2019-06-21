// Data route
const url = "/data";

// Grab only the data from our client
// Mercedes-Benz of Edison Service - A Ray Catena Dealership
// 123 Main St, Edison, NJ 08817

// Reference to the table body
const tbody = d3.select("tbody");

// Filter table button
const filterButton = d3.select("#filter-data");

// Data for client
const client_state = "/data/nj";

// Fetch the JSON data and console log it
d3.json(client_state).then(function(data, error) {
  // If there is an error, throw the error (console)
  if (error) {
    throw error;
  }

  // console.log(data);

  // Render the table onto the webpage
  function rendertable() {
    tbody.text("");
    data.forEach(function(client) {
      let row = tbody.append("tr");

      Object.entries(client).forEach(function([key, value]) {
        let cell = row.append("td").text(value);
        cell.text(value);
      });
    });
  }

  // onClick handler
  filterButton.on("click", function() {
    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input from all the filters available
    let inputZip = d3.select("#zip");
    let inputGender = d3.select("#gender");
    let inputAge = d3.select("#age");
    let inputStatus = d3.select("#status");
    let inputGroup = d3.select("#group");
    let inputKids = d3.select("#kids");

    // Get the value property from the inputs and change it to lowercase to match the dataset
    let inputZipValue = inputZip.property("value");
    let inputGenderValue = inputGender.property("value");
    let inputAgeValue = Number(inputAge.property("value"));
    let inputStatusValue = inputStatus.property("value");
    let inputGroupValue = inputGroup.property("value");
    let inputKidsValue = inputKids.property("value");

    // Filter the data and extract the variables needed from the data
    data = data.filter(function(datum) {
      let datumZip = datum.Zip;
      let datumGender = datum.Gender;
      let datumAge = datum.Age;
      let datumStatus = datum.MaritalStatus;
      let datumGroup = datum.EthnicGroup;
      let datumKids = datum.Kids;

      // Conduct an if statement to be able to filter on multiple categories on the webpage
      if (
        (datumZip === inputZipValue || inputZipValue === 0) &&
        (datumGender === inputGenderValue || inputGenderValue === "") &&
        (datumAge === inputAgeValue || inputAgeValue === 0) &&
        (datumStatus === inputStatusValue || inputStatusValue === "") &&
        (datumGroup === inputGroupValue || inputGroupValue === "") &&
        (datumKids === inputKidsValue || inputKidsValue === "")
      ) {
        return true;
      }
      return false;
    });

    // Re-rendering the table
    rendertable();
  });

  // Initial table rendering
  rendertable();
});
