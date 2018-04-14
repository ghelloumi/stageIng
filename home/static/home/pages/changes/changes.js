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

function SearchDate(str) {
    // Declare variables
    var input, filter, table, tr, td, i;

    if (str == 'yes') {
        d = new Date(document.getElementById("myInputType").value);
    } else {
        d = new Date(str)
    }
    dt = '' + (d.getUTCDate());
    mn = (d.getUTCMonth());
    mn++;
    mn = '' + mn
    yy = ('' + (d.getUTCFullYear())).substr(2, 2);
    if (dt.length == 1)
        dt = '0' + dt
    if (mn.length == 1)
        mn = '0' + mn
    if (yy.length == 1)
        yy = '0' + yy

    input = yy + mn + dt;
    filter = input;

    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];

        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


 // convert date
function convertDateToChId(d){
    dt = '' + (d.getUTCDate());
    mn = (d.getUTCMonth());
    mn++;
    mn = '' + mn
    yy = ('' + (d.getUTCFullYear())).substr(2, 2);
    if (dt.length == 1)
        dt = '0' + dt
    if (mn.length == 1)
        mn = '0' + mn
    if (yy.length == 1)
        yy = '0' + yy
    return 'CH-'+yy + mn + dt;
}
function datesArray(startDate, endDate) {
      var dates = [],
      currentDate = startDate,
      addDays = function(days) {
        var date = new Date(this.valueOf());
        date.setDate(date.getUTCDate() + days);
        return date;
      };

      while (currentDate <= endDate) {
        dates.push(currentDate);
        currentDate = addDays.call(currentDate, 1);
      }


    for(i=0;i<dates.length;i++){
        dates[i] = convertDateToChId(dates[i]);
    }

    return dates;
}

//filter Date fonction
function filterDate(){
    d1 = new Date(document.getElementById("filterDate1").value);
    d2 = new Date(document.getElementById("filterDate2").value);

    var table, tr, td, i;

    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0].getElementsByTagName('a')[0].getElementsByTagName('span')[0];
        if (td) {
            if (datesArray(d1,d2).indexOf(td.innerHTML.substr(0,9)) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


d = new Date()
dt = '' + d.getUTCDate();
mn = d.getUTCMonth();
mn++;
mn = '' + mn
yy = '' + d.getUTCFullYear();
if (dt.length == 1)
    dt = '0' + dt
if (mn.length == 1)
    mn = '0' + mn
da = yy + '-' + mn + '-' + dt

document.getElementById('myInputType').value = da;

window.onload = SearchDate(da)

function fn5(){
var table, rows, switching, i, x, y, shouldSwitch;
table = document.getElementById("table");
switching = true;
while (switching) {
    switching = false;
    rows = table.getElementsByTagName("tr");
    for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("td")[0];
        y = rows[i + 1].getElementsByTagName("td")[0];

        if (Number(y.innerHTML.substring(10, 12)) > Number(x.innerHTML.substring(10, 12))) {
            shouldSwitch = true;
            break;
        }
    }
    if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
    }
}

}

window.onload = fn5();

