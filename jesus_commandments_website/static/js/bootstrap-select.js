$(document).ready(function() {
  $('#multiselect').multiselect({
    buttonWidth : '100%',
    includeSelectAllOption : true,
    nonSelectedText: 'Select Resource Language',
    buttonClass: "btnMultiSelect",
    enableFiltering: true,
    enableFullValueFiltering: true,
    enableCaseInsensitiveFiltering: true
  });
});