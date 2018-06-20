//function appViewModel() consists of title, description, client, client priority,target date and product area fields
  
    var appViewModel = function () {
      var self = this;
      self.title = ko.observable("");
      self.description = ko.observable("");
      self.client = ko.observable("");
      self.clientPriority = ko.observable("");
      self.targetDate = ko.observable("");
      self.productArea = ko.observable("");
    };
    self.Done = function () {
      console.log("inside update");
      $.ajax({
        url: '/createfeature',
        type: 'POST',
        data: JSON.stringify({
          title: title(),
          description: description(),
          client: client(),
          clientPriority: clientPriority(),
          targetDate: targetDate(),
          productArea: productArea()
        }),
        contentType: 'application/json',
        success: function (result) {
          alert("Record inserted Sucessfully");

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {

          alert("some error");

        }
      });
    };

    ko.applyBindings(appViewModel);


