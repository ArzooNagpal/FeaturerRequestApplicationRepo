//featureRequestDetails js file is used to display features in the form of table using Jquery data tables
$(document).ready(function () {
    //Ajax get call from the below url to retrieve all feaures
    $.ajax({
        url: '/retrievefeature',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            console.log("json" + data.ListFeature);
            // Prints the retrieved JSON data into a table
            $('#Featurestable').DataTable({
                pageLength: 5,
                lengthMenu: [5, 10, 25, 50, 75, 100],
                responsive: true,
                data: data.ListFeature,
                columns: [
                    { 'data': 'title' },
                    { 'data': 'description' },
                    { 'data': 'client' },
                    { 'data': 'client_priority' },
                    { 'data': 'target_date' },
                    { 'data': 'product_area' }
                ]
            });
        }
    });
});
