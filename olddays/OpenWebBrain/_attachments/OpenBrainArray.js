function OBmax(a){
    m = -999999999;
    for (var i=0; i < a.length; i ++)
        m = Math.max(m, a[i]);
    return m
}

function OBmin(a){
    m = +999999999;
    for (var i=0; i < a.length; i ++)
        m = Math.min(m, a[i]);
    return m
}

function OBmean(a){
    m = 0.0;
    for (var i=0; i < a.length; i ++)
        m += a[i];
    m = m / a.length;
    return m
}

function OBnormalize(a){
    var b = new Array();
    mx = OBmax(a) * 1.0;
    mn = OBmin(a) * 1.0;
    d = (mx - mn) * 1.0;
    mm = OBmean(a);
    for(var i=0; i<a.length; i ++)
        b[i] = 1.0 * (a[i] - mm) / d;
                
    return b;
}