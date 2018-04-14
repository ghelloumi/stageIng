function fn1(){
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("_appendHere");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("tr");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[0];
            y = rows[i + 1].getElementsByTagName("td")[0];

            if (Number(y.innerHTML.substring(6, 8)) > Number(x.innerHTML.substring(6, 8))) {
                shouldSwitch = true;
                break;
            } else if (Number(y.innerHTML.substring(6, 8)) == Number(x.innerHTML.substring(6, 8))) {
                if (Number(y.innerHTML.substring(3, 5)) > Number(x.innerHTML.substring(3, 5))) {
                    shouldSwitch = true;
                    break;
                } else if (Number(y.innerHTML.substring(3, 5)) == Number(x.innerHTML.substring(3, 5))) {
                    if (Number(y.innerHTML.substring(0, 2)) > Number(x.innerHTML.substring(0, 2))) {
                        shouldSwitch = true;
                        break;
                    }else if(Number(y.innerHTML.substring(0, 2)) == Number(x.innerHTML.substring(0, 2))){
                        if (Number(y.innerHTML.substring(9, 11)) > Number(x.innerHTML.substring(9, 11))) {
                            shouldSwitch = true;
                            break;
                        }else if(Number(y.innerHTML.substring(9, 11)) == Number(x.innerHTML.substring(9, 11))){
                            if (Number(y.innerHTML.substring(12, 14)) > Number(x.innerHTML.substring(12, 14))) {
                                shouldSwitch = true;
                                break;
                            }
                        }
                    }
                }
            }
        }
        if (shouldSwitch) {
            console.log('done');
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}
window.onload = fn1()

$('#event').submit(function(e){
    e.preventDefault();
    url = $(this).attr('action')
    data = $(this).serialize();
    $.post(url, data, function(response){
    })
})