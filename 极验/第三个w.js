var {RSAKey} = require("node-jsencrypt")
const CryptoJS = require("crypto-js");

function $_CCCG(){
    var now = new Date().getTime();
    return {
        "v": "7.8.9",
        "$_BIB": false,
        "me": true,
        "tm": {
            "a": now - 2367,
            "b": now - 2367 + 168,
            "c": now - 2367 + 168,
            "d": 0,
            "e": 0,
            "f": now - 2367 + 168 + 167,
            "g": now - 2367 + 168 + 167 + 4,
            "h": now - 2367 + 168 + 167 + 4+ 6,
            "i": now - 2367 + 168 + 167 + 4+ 6 ,
            "j": now - 2367 + 168 + 167 + 4+ 6 + 35,
            "k": now - 2367 + 168 + 167 + 4+ 6 + 15,
            "l": now - 2367 + 168 + 167 + 4+ 6 + 35,
            "m": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16,
            "n": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2,
            "o": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12,
            "p": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3,
            "q": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3,
            "r": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18,
            "s": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65,
            "t": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65,
            "u": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65
        },
        "td": -1
    }
}

function H(t, e) {
    for (var n = e['slice'](-2), r = [], i = 0; i < n['length']; i++) {
        var o = n['charCodeAt'](i);
        r[i] = 57 < o ? o - 87 : o - 48;
    }
    n = 36 * r[0] + r[1];
    var s, a = Math['round'](t) + n, _ = [[], [], [], [], []], c = {}, u = 0;

    i = 0;
    for (var l = (e = e['slice'](0, -2))['length']; i < l; i++)
        c[s = e['charAt'](i)] || (c[s] = 1,
        _[u]['push'](s),
        u = 5 == ++u ? 0 : u);
    var h, f = a, d = 4, p = '', g = [1, 2, 5, 10, 50];

    while (0 < f)
        0 <= f - g[d] ? (h = parseInt(Math['random']() * _[d]['length'], 10),
        p += _[d][h],
        f -= g[d]) : (_['splice'](d, 1),
        g['splice'](d, 1),
        d -= 1);
    return p;
}


function ct(t) {
    this['$_BCAJ'] = t || [];
}

ct.prototype.$_CAQ = function(t) {
    var e = this['$_BCAJ'];
    if (e['map'])
        return new ct(e['map'](t));
    for (var n = [], r = 0, i = e['length']; r < i; r += 1)
        n[r] = t(e[r], r, this);
    return new ct(n);
}

function $_FDU(gui){
    function n(t) {
        var e = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
          , n = e['length']
          , r = ''
          , i = Math['abs'](t)
          , o = parseInt(i / n);
        n <= o && (o = n - 1),
        o && (r = e['charAt'](o));

        var s = '';
        return t < 0 && (s += '!'),
        r && (s += '$'),
        s + r + e['charAt'](i %= n);
    }
    var t = function(t) {
        for (var e, n, r, i = [], o = 0, s = 0, a = t['length'] - 1; s < a; s++)
            e = Math['round'](t[s + 1][0] - t[s][0]),
            n = Math['round'](t[s + 1][1] - t[s][1]),
            r = Math['round'](t[s + 1][2] - t[s][2]),
            0 == e && 0 == n && 0 == r || (0 == e && 0 == n ? o += r : (i['push']([e, n, r + o]),
            o = 0));
        return 0 !== o && i['push']([e, n, o]),
        i;
    }(gui)
      , r = []
      , i = []
      , o = [];
    return new ct(t)['$_CAQ'](function(t) {
        var e = function(t) {
            for (var e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], n = 0, r = e['length']; n < r; n++)
                if (t[0] == e[n][0] && t[1] == e[n][1])
                    return 'stuvwxyz~'[n];
            return 0;
        }(t);
        e ? i['push'](e) : (r['push'](n(t[0])),
        i['push'](n(t[1]))),
        o['push'](n(t[2]));
    }),
    r['join']('') + '!!' + i['join']('') + '!!' + o['join']('');
}

function $_BBEM(t, e, n) {
    if (!e || !n)
        return t;
    var r, i = 0, o = t, s = e[0], a = e[2], _ = e[4];
    while (r = n['substr'](i, 2)) {
        i += 2;
        var c = parseInt(r, 16)
          , u = String['fromCharCode'](c)
          , l = (s * c * c + a * c + _) % t['length'];
        o = o['substr'](0, l) + u + o['substr'](l);
    }
    return o;
}


function X(t) {

            function _(t, e) {

                        return t << e | t >>> 32 - e;

            }
            function c(t, e) {

                        var n, r, i, o, s;

                        return i = 2147483648 & t,
                        o = 2147483648 & e,
                        s = (1073741823 & t) + (1073741823 & e),
                        (n = 1073741824 & t) & (r = 1073741824 & e) ? 2147483648 ^ s ^ i ^ o : n | r ? 1073741824 & s ? 3221225472 ^ s ^ i ^ o : 1073741824 ^ s ^ i ^ o : s ^ i ^ o;

            }
            function e(t, e, n, r, i, o, s) {

                        return c(_(t = c(t, c(c(function a(t, e, n) {

                            return t & e | ~t & n;
                        }(e, n, r), i), s)), o), e);

            }
            function n(t, e, n, r, i, o, s) {

                        return c(_(t = c(t, c(c(function a(t, e, n) {

                            return t & n | e & ~n;
                        }(e, n, r), i), s)), o), e);

            }
            function r(t, e, n, r, i, o, s) {

                        return c(_(t = c(t, c(c(function a(t, e, n) {

                            return t ^ e ^ n;
                        }(e, n, r), i), s)), o), e);

            }
            function i(t, e, n, r, i, o, s) {

                        return c(_(t = c(t, c(c(function a(t, e, n) {

                            return e ^ (t | ~n);
                        }(e, n, r), i), s)), o), e);

            }
            function o(t) {

                        var e, n = '', r = '';

                        for (e = 0; e <= 3; e++)
                            n += (r = '0' + (t >>> 8 * e & 255)['toString'](16))['substr'](r['length'] - 2, 2);

                        return n;

            }
            var s, a, u, l, h, f, d, p, g, v;
            for (s = function m(t) {

                var e, n = t['length'], r = n + 8, i = 16 * (1 + (r - r % 64) / 64), o = Array(i - 1), s = 0, a = 0;
                while (a < n)
                    s = a % 4 * 8,
                    o[e = (a - a % 4) / 4] = o[e] | t['charCodeAt'](a) << s,
                    a++;
                return s = a % 4 * 8,
                o[e = (a - a % 4) / 4] = o[e] | 128 << s,
                o[i - 2] = n << 3,
                o[i - 1] = n >>> 29,
                o;
            }(t = function y(t) {

                t = t['replace'](/\r\n/g, '\n');
                for (var e = '', n = 0; n < t['length']; n++) {
                    var r = t['charCodeAt'](n);
                    r < 128 ? e += String['fromCharCode'](r) : (127 < r && r < 2048 ? e += String['fromCharCode'](r >> 6 | 192) : (e += String['fromCharCode'](r >> 12 | 224),
                    e += String['fromCharCode'](r >> 6 & 63 | 128)),
                    e += String['fromCharCode'](63 & r | 128));
                }
                return e;
            }(t)),
            d = 1732584193,
            p = 4023233417,
            g = 2562383102,
            v = 271733878,
            a = 0; a < s['length']; a += 16)
                p = i(p = i(p = i(p = i(p = r(p = r(p = r(p = r(p = n(p = n(p = n(p = n(p = e(p = e(p = e(p = e(l = p, g = e(h = g, v = e(f = v, d = e(u = d, p, g, v, s[a + 0], 7, 3614090360), p, g, s[a + 1], 12, 3905402710), d, p, s[a + 2], 17, 606105819), v, d, s[a + 3], 22, 3250441966), g = e(g, v = e(v, d = e(d, p, g, v, s[a + 4], 7, 4118548399), p, g, s[a + 5], 12, 1200080426), d, p, s[a + 6], 17, 2821735955), v, d, s[a + 7], 22, 4249261313), g = e(g, v = e(v, d = e(d, p, g, v, s[a + 8], 7, 1770035416), p, g, s[a + 9], 12, 2336552879), d, p, s[a + 10], 17, 4294925233), v, d, s[a + 11], 22, 2304563134), g = e(g, v = e(v, d = e(d, p, g, v, s[a + 12], 7, 1804603682), p, g, s[a + 13], 12, 4254626195), d, p, s[a + 14], 17, 2792965006), v, d, s[a + 15], 22, 1236535329), g = n(g, v = n(v, d = n(d, p, g, v, s[a + 1], 5, 4129170786), p, g, s[a + 6], 9, 3225465664), d, p, s[a + 11], 14, 643717713), v, d, s[a + 0], 20, 3921069994), g = n(g, v = n(v, d = n(d, p, g, v, s[a + 5], 5, 3593408605), p, g, s[a + 10], 9, 38016083), d, p, s[a + 15], 14, 3634488961), v, d, s[a + 4], 20, 3889429448), g = n(g, v = n(v, d = n(d, p, g, v, s[a + 9], 5, 568446438), p, g, s[a + 14], 9, 3275163606), d, p, s[a + 3], 14, 4107603335), v, d, s[a + 8], 20, 1163531501), g = n(g, v = n(v, d = n(d, p, g, v, s[a + 13], 5, 2850285829), p, g, s[a + 2], 9, 4243563512), d, p, s[a + 7], 14, 1735328473), v, d, s[a + 12], 20, 2368359562), g = r(g, v = r(v, d = r(d, p, g, v, s[a + 5], 4, 4294588738), p, g, s[a + 8], 11, 2272392833), d, p, s[a + 11], 16, 1839030562), v, d, s[a + 14], 23, 4259657740), g = r(g, v = r(v, d = r(d, p, g, v, s[a + 1], 4, 2763975236), p, g, s[a + 4], 11, 1272893353), d, p, s[a + 7], 16, 4139469664), v, d, s[a + 10], 23, 3200236656), g = r(g, v = r(v, d = r(d, p, g, v, s[a + 13], 4, 681279174), p, g, s[a + 0], 11, 3936430074), d, p, s[a + 3], 16, 3572445317), v, d, s[a + 6], 23, 76029189), g = r(g, v = r(v, d = r(d, p, g, v, s[a + 9], 4, 3654602809), p, g, s[a + 12], 11, 3873151461), d, p, s[a + 15], 16, 530742520), v, d, s[a + 2], 23, 3299628645), g = i(g, v = i(v, d = i(d, p, g, v, s[a + 0], 6, 4096336452), p, g, s[a + 7], 10, 1126891415), d, p, s[a + 14], 15, 2878612391), v, d, s[a + 5], 21, 4237533241), g = i(g, v = i(v, d = i(d, p, g, v, s[a + 12], 6, 1700485571), p, g, s[a + 3], 10, 2399980690), d, p, s[a + 10], 15, 4293915773), v, d, s[a + 1], 21, 2240044497), g = i(g, v = i(v, d = i(d, p, g, v, s[a + 8], 6, 1873313359), p, g, s[a + 15], 10, 4264355552), d, p, s[a + 6], 15, 2734768916), v, d, s[a + 13], 21, 1309151649), g = i(g, v = i(v, d = i(d, p, g, v, s[a + 4], 6, 4149444226), p, g, s[a + 11], 10, 3174756917), d, p, s[a + 2], 15, 718787259), v, d, s[a + 9], 21, 3951481745),
                d = c(d, u),
                p = c(p, l),
                g = c(g, h),
                v = c(v, f);
            return (o(d) + o(p) + o(g) + o(v))['toLowerCase']();

}


// t: 横向拖动距离
// e: 被加密后的轨迹
// n: 滑动的时间
function third_w(gt, challenge, s, c, x_jvli, guiji, tuodongshijian) {

    var l = cul_l(guiji, c, s);
    var i = {
        "gt": gt,
        "challenge": challenge,
    }

    var o = {
        'lang': 'zh-cn',
        'userresponse': H(x_jvli, i['challenge']),
        'passtime': tuodongshijian,
        'imgload': 3268,
        'aa': l,
        'ep': $_CCCG()
    };

    o["h9s9"] = "1816378497";  // 直接给了一个值... 经过测试之后. 你能发现.这个值毛用没有...

    o['rp'] = X(i['gt'] + i['challenge']['slice'](0, 32) + o['passtime']);

    var u = $_CCDH() // rsa
        , l = encrypt(JSON['stringify'](o), $_CCIT()) // AES
        , h = $_HEm(l)  // 处理成类似b64的东西

        , f = {
        'gt': i['gt'],
        'challenge': i['challenge'],
        'lang': 'zh-cn',
        '$_BCw': 0,
        'client_type': 'web',
        'w': h + u
    };
    return f
}

function encrypt(e, t, n) { // 猜测是aes加密, CryptoJS.
    var key = t;
    var iv  = "0000000000000000";
    key = CryptoJS.enc.Utf8.parse(key);
    iv = CryptoJS.enc.Utf8.parse(iv);

    var r = CryptoJS.AES.encrypt(e, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC
    });

    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var a = [];
    for (var s = 0; s < i; s++) {
        var c = o[s >>> 2] >>> 24 - s % 4 * 8 & 255;
        a['push'](c);
    }
    return a;
}

function $_HEm(e){
    var t = $_HCX(e);
   return t['res'] + t['end'];
}

function $_HCX(e, o){
    var i = this;
    o || (o = i);
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HBO(t, r) && (n = (n << 1) + $_HBO(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var c;
        if (a + 2 < s)
            c = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)) + $_GJF(t(c, 235));
        else {
            var _ = s % 3;
            2 == _ ? (c = (e[a] << 16) + (e[a + 1] << 8),
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)),
            r = '.') : 1 == _ && (c = e[a] << 16,
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)),
            r = '.' + '.');
        }
    }
    return {
        "\u0072\u0065\u0073": n,
        "\u0065\u006e\u0064": r
    };

}

function $_HBO(e, t) {
    return e >> t & 1;
}

function $_GJF(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}


function $_CCDH(e){
    // 你可以选择用python去做. 别抠代码...
    // 你知道它用的rsa. 并且. 你知道它用的是JSEncrypt  但是. JSEncrypt没有给两个数字的功能
    var rsa = new RSAKey(); // 如果你受不了这个方案. 你可以选择使用python来完成该算法
    rsa.setPublic('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    var t = rsa['encrypt']($_CCIT(e)); // 对aeskey进行加密
    while (!t || 256 !== t['length'])
        t = rsa['encrypt']($_CCIT(!0));
    return t;
}

var quanjv = {
    $_EIf:{}
}

function $_CCIT(e){
    return quanjv['$_EIf']['aeskey'] && !e || (quanjv['$_EIf']['aeskey'] = te()),
    quanjv['$_EIf']['aeskey']; // 返回aeskey
}

function te(){
    return e() + e() + e() + e();
}

function e(){
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function cul_l(gui, c, s){
    var r = $_FDU(gui);  // $_FDU 是正确的
    var l = $_BBEM(r, c, s)
    return l
}



