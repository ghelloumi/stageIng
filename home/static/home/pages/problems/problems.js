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
    $("button.decroi").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("table");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("tr");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[2];
                y = rows[i + 1].getElementsByTagName("td")[2];

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
    });

    $("button.accroi").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("table");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("tr");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[2];
                y = rows[i + 1].getElementsByTagName("td")[2];

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
    });
});

jQuery(function ($) {
    $("button.decroiPrio").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById('table')
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName('tr');
            //rows = table.querySelectorAll('div.pb');
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[4];
                y = rows[i + 1].getElementsByTagName("td")[4];

                if (Number(y.getElementsByTagName("div")[0].innerHTML) > Number(x.getElementsByTagName("div")[0].innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    });

    $("button.accroiPrio").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("table");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("tr");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[4];
                y = rows[i + 1].getElementsByTagName("td")[4];

                if (Number(y.getElementsByTagName("div")[0].innerHTML) < Number(x.getElementsByTagName("div")[0].innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }

    });
});

function myFunctionStatus() {
    // Declare variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInputStat");
    filter = input.value.toUpperCase();

    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[7];

        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

jQuery(function ($) {
    $("a.drop_down_choosen_title1").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("table");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("tr");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[9];
                y = rows[i + 1].getElementsByTagName("td")[9];
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    });

    $("a.drop_down_choosen_title2").click(function () {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("table");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("tr");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[9];
                y = rows[i + 1].getElementsByTagName("td")[9];
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    });
});

function myFunctionOwner() {
    // Declare variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInputOwner");
    filter = input.value.toUpperCase();

    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");


    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[9];
        a = td.getElementsByTagName("a")[0].getElementsByTagName("span")[0]
        if (a) {
            if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function autoSize(ele) {
   ele.style.height = 'auto';
   var newHeight = (ele.scrollHeight > 32 ? ele.scrollHeight : 32);
   ele.style.height = newHeight.toString() + 'px';
}

function sortingProblemList(){
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("table");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("tr");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[1].getElementsByTagName('a')[0].getElementsByTagName('span')[0].innerHTML;
            y = rows[i + 1].getElementsByTagName("td")[1].getElementsByTagName('a')[0].getElementsByTagName('span')[0].innerHTML;

            if (Number(y.substring(3, 5)) > Number(x.substring(3, 5))) {
                shouldSwitch = true;
                break;
            } else if (Number(y.substring(3, 5)) == Number(x.substring(3, 5))) {
                if (Number(y.substring(5, 7)) > Number(x.substring(5, 7))) {
                    shouldSwitch = true;
                    break;
                } else if (Number(y.substring(5, 7)) == Number(x.substring(5, 7))) {
                    if (Number(y.substring(8, 10)) > Number(x.substring(8, 10))) {
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
window.onload = sortingProblemList();