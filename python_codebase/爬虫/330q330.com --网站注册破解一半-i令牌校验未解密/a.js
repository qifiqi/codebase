window = this
var t = {
    "username": "22wwssxx",
    "password": "123qweasdzxc",
    "confirm_password": "123qweasdzxc",
    "realname": "",
    "r_type": 2,
    "tel": "",
    "type": 1,
    "token": "CN31_X4etLB7zduhrlVFe8IOgNadSG1aWvcUioPqVvUao7LFpkuaw0g2CiwAkOn_JaFr6lfLFMZRZkYUoaQWSLpsgD2uCVqOsfMk.MNYJbr5YW9Wl0zRO49xrDyJ0FuHFkEqxleMxUW9LMwfIbFerECj4u9jRzfvsXux2k1vINR-PjgNtldXlcg41vnlw6HjiXSqBbbJfycGZ-kiYyGulUslz9ubYwea72lFeeouAS2VV0-lR6NhbGVQxi4eChx-NzQtI6mU-NcvC1O2ry-CgzJ-T4VrsIinaC0Tbexbm96DTCSbs.yMXPJcqzVN8UT-To0bMhSf9Ma-z9hUd.bGQEODgW0OQcim9EKqjYp4hrpFkUXkL1-bU7mOqM_hKlJenF7BL.LV9eWXGCp.X1K4n8ONx0xnya4GfKe9U9BYQYEa_f4QRmc5R2n0TGU72uuYrqvNeeX218ZErfMAjKMRqw59-MsZIKQ0RiOqmp0fHEw6_nsv-mSxzimJrb2tq8gN3",
    "tpl": 5
}


var s = !function(e) {
    function n(t) {
        if (r[t])
            return r[t].exports;
        var o = r[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(o.exports, o, o.exports, n),
        o.l = !0,
        o.exports
    }
    var t = window.webpackJsonp;
    window.webpackJsonp = function(r, a, c) {
        for (var i, u, f, s = 0, l = []; s < r.length; s++)
            u = r[s],
            o[u] && l.push(o[u][0]),
            o[u] = 0;
        for (i in a)
            Object.prototype.hasOwnProperty.call(a, i) && (e[i] = a[i]);
        for (t && t(r, a, c); l.length; )
            l.shift()();
        if (c)
            for (s = 0; s < c.length; s++)
                f = n(n.s = c[s]);
        return f
    }
    ;
    var r = {}
      , o = {
        2: 0
    };
    n.e = function(e) {
        function t() {
            i.onerror = i.onload = null,
            clearTimeout(u);
            var n = o[e];
            0 !== n && (n && n[1](new Error("Loading chunk " + e + " failed.")),
            o[e] = void 0)
        }
        var r = o[e];
        if (0 === r)
            return new Promise(function(e) {
                e()
            }
            );
        if (r)
            return r[2];
        var a = new Promise(function(n, t) {
            r = o[e] = [n, t]
        }
        );
        r[2] = a;
        var c = document.getElementsByTagName("head")[0]
          , i = document.createElement("script");
        i.type = "text/javascript",
        i.charset = "utf-8",
        i.async = !0,
        i.timeout = 12e4,
        n.nc && i.setAttribute("nonce", n.nc),
        i.src = n.p + "static/js/" + e + "." + {
            0: "9fdaae2269ad3da42d5f",
            1: "00dc810af42721bf6203"
        }[e] + ".1682776535598.js";
        var u = setTimeout(t, 12e4);
        return i.onerror = i.onload = t,
        c.appendChild(i),
        a
    }
    ,
    n.m = e,
    n.c = r,
    n.i = function(e) {
        return e
    }
    ,
    n.d = function(e, t, r) {
        n.o(e, t) || Object.defineProperty(e, t, {
            configurable: !1,
            enumerable: !0,
            get: r
        })
    }
    ,
    n.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return n.d(t, "a", t),
        t
    }
    ,
    n.o = function(e, n) {
        return Object.prototype.hasOwnProperty.call(e, n)
    }
    ,
    n.p = "/",
    n.oe = function(e) {
        throw e
    }
}([]);
function aa(t, e, s) {
    "use strict";
    var i = s(86)
      , a = s.n(i)
      , n = s(455)
      , o = s(1133)
      , r = s.n(o)
      , l = s(55)
      , c = s.n(l);
    e.a = {
        aes_iv: "12345678ABCDEFGH",
        dataEncode: function(t, e, i) {
            var o = (new Date).getTime()
              , r = {
                t: o,
                s: "",
                d: "",
                k: ""
            }
              , l = this.sign(t, o, i, e, !1);
            r.s = l;
            var c = s.i(n.a)(a()(t), i, this.aes_iv);
            r.d = c;
            var u = "";
            u = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+/jm7adLHn/cUaIsuuAQDlWmp5TsCdBrsrGZi/FnVVnMG0pep8Ph4sycEow8e23bRbWIjMBGSSRg4DScPPNN/ZO6NmZd9WWuNFMZ8A8Dv0TB0T78nWWtDkJ12lyRwnV75gGewlc/hR61z9OFtMk5wtOMujsJOGz73mronXW88dQIDAQAB-----END PUBLIC KEY-----",
            "/qianneng/fund-transfer/transfer-api" === e && (u = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9HLND55pcSm5NxZWVyEVl1X9M2eMvXOLEvosoFbnuEAf+oAIWO/rFtSJUPyA3AcwyxPKsYJwmQmpL/9X0ptike7YzEoiEo+wgN6/Tk1KPS/nuh6Dirr8ExC+teZU68Ryeytiecb42AtXah39VdQsDrUMs/HWdEaUoUxi/yV3+JwIDAQAB-----END PUBLIC KEY-----");
            var d = this.rasEncode(u, i);
            return r.k = d,
            a()(r)
        },
        dataDecode: function(t, e) {
            var i = c.a.extend({}, t)
              , a = s.i(n.b)(i.d, e, this.aes_iv);
            return i.d = JSON.parse(a),
            i
        },
        sign: function(t, e, i, o, r) {
            if (!c.a.isPlainObject(t) && "array" !== c.a.type(t))
                return !1;
            "boolean" !== c.a.type(r) && (r = !1);
            var l = c.a.extend({}, t, {
                sign_timestamp: e,
                sign_aeskey: i,
                sign_uri: o
            })
              , u = this.sort(l)
              , d = []
              , v = "";
            return c.a.each(u, function(t, e) {
                (c.a.isPlainObject(e) || c.a.isArray(e)) && (e = a()(e)),
                d.push(t + "=" + e)
            }),
            v = d.join("&"),
            v = this.urlencode(v),
            v = s.i(n.c)(v)
        },
        signVerify: function(t, e, s, i, a) {
            return this.sign(t, e, a, i, !1) === s
        },
        sort: function(t) {
            var e = []
              , s = 0;
            for (var i in t)
                e[s] = i,
                s++;
            var a = e.sort()
              , n = {};
            for (var o in a)
                n[a[o]] = t[a[o]];
            return n
        },
        urlencode: function(t) {
            return window.encodeURIComponent(t).replace(/[!'()*]/g, function(t) {
                return "%" + t.charCodeAt(0).toString(16).toUpperCase()
            })
        },
        random: function(t) {
            t = t || 32;
            for (var e = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", s = e.length, i = "", a = 0; a < t; a++)
                i += e.charAt(Math.floor(Math.random() * s));
            return i
        },
        rasEncode: function(t, e) {
            var s = new r.a;
            return s.setPublicKey(t),
            s.encryptLong(a()(e))
        }
    }
}

var e = "/member/user/register"

console.log(aa(t, e, s));


