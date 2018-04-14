$(window).load(function () {
    function autoResizeDiv() {
        document.getElementById('double-scroll').style.height = window.innerHeight + 'px';
        document.getElementById('double-scroll').style.overflowY = 'hidden';
    }

    window.onresize = autoResizeDiv;
    autoResizeDiv();

});

$(function () {
    $(".wmd-view").scroll(function () {
        $(".wmd-view-topscroll")
            .scrollLeft($(".wmd-view").scrollLeft());
    });
});

function myFunctionSearch(n, s) {
    // Declare variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput" + s);
    filter = input.value.toUpperCase();

    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[n];

        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function fnTriDown(n) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("table");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("tr");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];

            if (Number(y.innerHTML.substring(0, 4)) > Number(x.innerHTML.substring(0, 4))) {
                shouldSwitch = true;
                break;
            } else if (Number(y.innerHTML.substring(0, 4)) == Number(x.innerHTML.substring(0, 4))) {
                if (Number(y.innerHTML.substring(5, 7)) > Number(x.innerHTML.substring(5, 7))) {
                    shouldSwitch = true;
                    break;
                } else if (Number(y.innerHTML.substring(5, 7)) == Number(x.innerHTML.substring(5, 7))) {
                    if (Number(y.innerHTML.substring(8, 10)) > Number(x.innerHTML.substring(8, 10))) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function fnTriUp(n) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("table");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("tr");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];

            if (Number(y.innerHTML.substring(0, 4)) < Number(x.innerHTML.substring(0, 4))) {
                shouldSwitch = true;
                break;
            } else if (Number(y.innerHTML.substring(0, 4)) == Number(x.innerHTML.substring(0, 4))) {
                if (Number(y.innerHTML.substring(5, 7)) < Number(x.innerHTML.substring(5, 7))) {
                    shouldSwitch = true;
                    break;
                } else if (Number(y.innerHTML.substring(5, 7)) == Number(x.innerHTML.substring(5, 7))) {
                    if (Number(y.innerHTML.substring(8, 10)) < Number(x.innerHTML.substring(8, 10))) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

$(function () {
    var a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
    var tbl = jQuery('table');
    $('#all_show').prop('disabled', true);

    $('#comitee').click(function () {
        var arr= ['ID', 'Type', 'Type of change', 'Impact Scope',
                'Accountable', 'Incident/BT/Jira reference', 'Area', 'Project description', 'External constraint',
                'Status', 'Required Changes', 'Status and current task list','Remove'],
        tr= $('#table > tbody > tr, #table > thead > tr');
              $('> th, > td', tr).hide();
              $.each(arr, function(_, val) {
                var col=  $('> th', tr)
                            .filter(function() {
                              return $(this).valueOf()[0].getElementsByTagName('span')[0].innerHTML===val;
                            })
                            .index();
                console.log(col)
                $(tr).append(function() {
                  return $('> td, > th', this).eq(col).show();
                });
              });

        $('#comitee').prop('disabled', true);
        $('#sgn_changes').prop('disabled', false);
        $('#all_show').prop('disabled', false);
    });

    $('#sgn_changes').click(function () {
        var arr= ['Type of change', 'Impact Date',
                'Description', 'Priority', 'External Go Live', 'Change Implem. Date', 'Binary Availability',
                'Post Impl. Incident', 'RCA','Remove'],
        tr= $('#table > tbody > tr, #table > thead > tr');
              $('> th, > td', tr).hide();
              $.each(arr, function(_, val) {
                var col=  $('> th', tr)
                            .filter(function() {
                              return $(this).valueOf()[0].getElementsByTagName('span')[0].innerHTML===val;
                            })
                            .index();
                console.log(col)
                $(tr).append(function() {
                  return $('> td, > th', this).eq(col).show();
                });
              });



        $('#sgn_changes').prop('disabled', true);
        $('#comitee').prop('disabled', false);
        $('#all_show').prop('disabled', false);

    });

    $('#all_show').click(function () {

        location.reload()

        $('#comitee').prop('disabled', false);
        $('#sgn_changes').prop('disabled', false);
        $('#all_show').prop('disabled', true);
    });
});

jQuery(function ($) {
    $("a.drop_down_choosen_SGN").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                if (td.innerHTML.toUpperCase() == 'SGN') {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    });

    $("a.drop_down_choosen_MM").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                if (td.innerHTML == 'MarketMap') {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    });

    $("a.drop_down_choosen_All").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            tr[i].style.display = "";
        }
    });
});

jQuery(function ($) {
    $("a.drop_down_choosen_Ops").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[4];
            if (td) {
                if (td.innerHTML == 'Ops') {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    });

    $("a.drop_down_choosen_SDM").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[4];
            if (td) {
                if (td.innerHTML == 'SDM') {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    });

    $("a.drop_down_choosen_SGN_All").click(function () {
        var table, tr, td, i;
        table = document.getElementById("table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            tr[i].style.display = "";
        }
    });
});


window.onload = fnTriDown(11);
function dateDiff(date1, date2){
    var diff = {}                           // Initialisation du retour
    var tmp = date2 - date1;

    tmp = Math.floor(tmp/1000);             // Nombre de secondes entre les 2 dates
    diff.sec = tmp % 60;                    // Extraction du nombre de secondes

    tmp = Math.floor((tmp-diff.sec)/60);    // Nombre de minutes (partie entière)
    diff.min = tmp % 60;                    // Extraction du nombre de minutes

    tmp = Math.floor((tmp-diff.min)/60);    // Nombre d'heures (entières)
    diff.hour = tmp % 24;                   // Extraction du nombre d'heures

    tmp = Math.floor((tmp-diff.hour)/24);   // Nombre de jours restants
    diff.day = tmp;

    return diff;
}
function fnBinaryAvailColor() {
    var type, table, rows, i, x, y ;
    table = document.getElementById("table");
    rows = table.getElementsByTagName("tr");
    for (i = 1; i < (rows.length); i++) {
        x = rows[i].getElementsByTagName("td")[23].innerHTML;
        y = rows[i].getElementsByTagName("td")[24].innerHTML;

        if (x == '') {
            rows[i].getElementsByTagName("td")[23].style.backgroundColor = "white"
            rows[i].getElementsByTagName("td")[23].style.color = "black"
        } else {
            if (x[4] == '-' && x[7] == '-' && x.length == 10 && !isNaN(x.substr(0, 4)) && !isNaN(x.substr(5, 2)) && !isNaN(x.substr(8, 2))) {
                type = 'date';
            } else type = 'text';

            if (type == 'date') {
                date2 = new Date(y);
                date1 = new Date(x);
                diff = dateDiff(date1, date2);
                if (Number(diff.day) <= 14) {
                    rows[i].getElementsByTagName("td")[23].style.backgroundColor = "red";
                    rows[i].getElementsByTagName("td")[23].style.color = "white"
                } else if (Number(diff.day) <= 30 && Number(diff.day) > 14) {
                    rows[i].getElementsByTagName("td")[23].style.backgroundColor = "orange";
                    rows[i].getElementsByTagName("td")[23].style.color = "white"
                } else if (Number(diff.day) > 30) {
                    rows[i].getElementsByTagName("td")[23].style.backgroundColor = "green";
                    rows[i].getElementsByTagName("td")[23].style.color = "white"
                }
            } else {
                    rows[i].getElementsByTagName("td")[23].style.backgroundColor = "red"
                    rows[i].getElementsByTagName("td")[23].style.color = "white"
            }

        }
    }
}
window.onload = fnBinaryAvailColor();



