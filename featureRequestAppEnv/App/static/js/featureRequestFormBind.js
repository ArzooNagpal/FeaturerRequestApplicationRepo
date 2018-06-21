//function featureRequestViewModel() consists of title, description, client, client priority,target date and product area fields.
var featureRequestViewModel = {
  title: ko.observable(""),
  description: ko.observable(""),
  client: ko.observable(""),
  clientPriority: ko.observable(""),
  targetDate: ko.observable(""),
  productArea: ko.observable("")
};
self.onSubmit = function () {
  //Performs a ajax POST call to below url with JSON data from featureReuqestViewModel
  $.ajax({
    url: '/createfeature',
    type: 'POST',
    data: ko.toJSON(featureRequestViewModel),
    contentType: 'application/json',
    success: function (result) {
      //Resoponse from ajax POST call is stored in result variable
      if (result == "success") {
        alert("Record inserted Sucessfully");
        window.location = "/featureRequestDetails";
      }
      else {
        alert(result)
      }
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      alert("Error Occured. Please contact your administrator");
    }
  });
};
//Apply bindings to featureRequestViewModel
ko.applyBindings(featureRequestViewModel);
//Script for restricting to enter past dates
var now = new Date(), minDate = now.toISOString().substring(0, 10);
$('#TargetDate').prop('min', minDate);