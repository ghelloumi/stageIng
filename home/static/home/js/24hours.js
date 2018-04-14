function isNumber(evt,num) {
    // get keyboard event and then look its keyCode
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    //check the event is numeric
    if (charCode > 31 && (charCode < 48 || charCode > 57) &&charCode!=186) {
        return false;
    }
	  
    // Check accordingly every new number must include regular date format
    if(num.value.length == 0 && (charCode==48 || charCode==49 || charCode==50))
    {
    	return true;
    }
    else if(num.value.length == 1 && (charCode>=48 && charCode<=51))
    {
    	return true;
    }
    else if(num.value.length == 2 && (charCode>=48 && charCode<=53))
    {
    	num.value=num.value+":";
    	return true;
    }
    else if(num.value.length == 3 && (charCode>=48 && charCode<=53))
    {

    	return true;
    }
    else if(num.value.length == 4 && (charCode>=48 && charCode<=57))
    {
    	return true;
    }
    else
    {
    	return false;
    }

    return true;
}
