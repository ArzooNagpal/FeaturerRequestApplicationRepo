

$(document).ready(function () {
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
