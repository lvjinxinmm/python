function s(t) {
    var a, i, n = Math.abs(parseInt((new Date).getTime() * Math.random() * 1e4)).toString(), o = 0;
    for (a = 0; a < n.length; a++)
        o += parseInt(n[a]);
    return i = function(t) {
        return function(a, i) {
            return i - "" + a.length <= 0 ? a : (t[i] || (t[i] = Array(i + 1).join(0))) + a
        }
    }([]),
    o += n.length,
    o = i(o, 3 - o.toString().length),
    t.toString() + n + o
}
function fn(){
    return s(1)
}