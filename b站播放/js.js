function b_lsid() {
    var e = splitDate()
      , t = f_b(e.millisecond)
      , t = "".concat(f_c(8), "_").concat(t);
  return t
}
function splitDate(e) {
    var t = new Date(e || Date.now())
      , n = t.getDate()
      , r = t.getHours()
      , e = t.getMinutes()
      , t = t.getTime();
    return {
        day: n,
        hour: r,
        minute: e,
        second: Math.floor(t / 1e3),
        millisecond: t
    }
}
function f_b(e) {
    return Math.ceil(e).toString(16).toUpperCase()
}
function f_c(e) {
    for (var t = "", n = 0; n < e; n++)
        t += o(16 * Math.random());
    return s(t, e)
}
function o(e) {
    return Math.ceil(e).toString(16).toUpperCase()
}
function s(e, t) {
    var n = "";
    if (e.length < t)
        for (var r = 0; r < t - e.length; r++)
            n += "0";
    return n + e
}


function uuid(){
 var e = a(8)
      , t = a(4)
      , n = a(4)
      , r = a(4)
      , o = a(12)
      , i = (new Date).getTime();
    return e + "-" + t + "-" + n + "-" + r + "-" + o + s((i % 1e5).toString(), 5) + "infoc"

}

function a(e) {
    for (var t = "", n = 0; n < e; n++)
        t += o(16 * Math.random());
    return s(t, e)
}


function u(){
    return uuid();
}
function b(){
    return b_lsid()
}
// console.log(b_lsid())
// console.log(uuid())

