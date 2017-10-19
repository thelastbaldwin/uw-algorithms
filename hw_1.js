function base62toBase10(numToConvert){
    var base62Lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    var convertedNumber = 0;
    var base = 62;

    // move backwards through the base62 number string and
    // use a varible starting at 0 to compute the power
    // of 62 at that place
    for (var i = numToConvert.length - 1, j = 0; i >= 0; i--, j++){
        var currentLetter = numToConvert[i];
        var decimalValue = base62Lookup.indexOf(currentLetter);
        convertedNumber += decimalValue * base ** j;
    }

    return convertedNumber;
}

// 18327995462734720000
console.log(base62toBase10("LpuPe81bc2w"));
