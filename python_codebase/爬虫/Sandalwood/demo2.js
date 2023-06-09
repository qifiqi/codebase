var t = {
    "functionId": "unionSearch",
    "params": {
        "funName": "search",
        "version": "v3",
        "source": 20310,
        "param": {
            "pageNo": 5,
            "pageSize": 60,
            "searchUUID": "6b1d113b988148978a2115e581e21956",
            "bonusIds": null,
            "category1": 16750,
            "category2": 16755,
            "category3": 16806,
            "deliveryType": null,
            "wlRate": null,
            "maxWlRate": null,
            "fromPrice": null,
            "toPrice": null,
            "hasCoupon": null,
            "isHot": null,
            "isNeedPreSale": null,
            "isPinGou": null,
            "isZY": null,
            "isCare": null,
            "lock": null,
            "orientationFlag": null,
            "sort": null,
            "sortName": null,
            "keyWord": "",
            "searchType": "st3",
            "keywordType": "kt0"
        }
    }
}
var self = this
var u = {Z:''};
!function () {
    "use strict";
    var e, n, t, o = {}, a = {};

    function r(e) {
        var n = a[e];
        if (void 0 !== n)
            return n.exports;
        var t = a[e] = {
            id: e,
            loaded: !1,
            exports: {}
        };
        return o[e].call(t.exports, t, t.exports, r),
            t.loaded = !0,
            t.exports
    }

    r.m = o,
        e = [],
        r.O = function (n, t, o, a) {
            if (!t) {
                var c = 1 / 0;
                for (u = 0; u < e.length; u++) {
                    t = e[u][0],
                        o = e[u][1],
                        a = e[u][2];
                    for (var i = !0, d = 0; d < t.length; d++)
                        (!1 & a || c >= a) && Object.keys(r.O).every((function (e) {
                                return r.O[e](t[d])
                            }
                        )) ? t.splice(d--, 1) : (i = !1,
                        a < c && (c = a));
                    if (i) {
                        e.splice(u--, 1);
                        var f = o();
                        void 0 !== f && (n = f)
                    }
                }
                return n
            }
            a = a || 0;
            for (var u = e.length; u > 0 && e[u - 1][2] > a; u--)
                e[u] = e[u - 1];
            e[u] = [t, o, a]
        }
        ,
        r.n = function (e) {
            var n = e && e.__esModule ? function () {
                        return e.default
                    }
                    : function () {
                        return e
                    }
            ;
            return r.d(n, {
                a: n
            }),
                n
        }
        ,
        r.d = function (e, n) {
            for (var t in n)
                r.o(n, t) && !r.o(e, t) && Object.defineProperty(e, t, {
                    enumerable: !0,
                    get: n[t]
                })
        }
        ,
        r.f = {},
        r.e = function (e) {
            return Promise.all(Object.keys(r.f).reduce((function (n, t) {
                    return r.f[t](e, n),
                        n
                }
            ), []))
        }
        ,
        r.u = function (e) {
            return {
                34: "biservicefee",
                81: "promotion",
                378: "user",
                410: "marketActivities",
                621: "entire",
                685: "lineReport",
                869: "createShop",
                917: "agreement",
                929: "common-731babaf",
                973: "common-43dd7041",
                1131: "appMng",
                1276: "shopActPromotion",
                1288: "myApi",
                1621: "investmentEffect",
                1666: "planDetails",
                1806: "officalPromotion",
                1884: "taskDetail",
                1913: "jdauthentication",
                1970: "newWithdraw",
                1992: "cashDetail",
                2337: "withdraw",
                2412: "socialMediaMng",
                2479: "marketingCalendar",
                2481: "realTimeScreen",
                2527: "withdrawRecord",
                2690: "couponList",
                2795: "cashGiftCreate",
                2832: "taskSquare",
                2951: "RewardActivity",
                2970: "articlePromotion",
                2992: "myTask",
                3012: "subCommission",
                3386: "cashGiftDeposit",
                3513: "trafficMediaMng",
                3579: "common-0e3dda97",
                3583: "webExtension",
                3712: "openplatform-9a53bcac",
                3756: "shopPromotion",
                3765: "skuAnalyse",
                3779: "active",
                3888: "external",
                3940: "cashCoupon",
                4163: "InterfaceManagement",
                4256: "channel",
                4565: "common-d91a9049",
                4738: "cpcMedia",
                4843: "openplatform-d91a9049",
                4962: "common-8912b8e4",
                5001: "groupList",
                5075: "planList",
                5142: "reverseInvestment",
                5177: "home",
                5313: "myStarEnlist2",
                5413: "recommendMng",
                5512: "accounting",
                5549: "jingPlanMng",
                5724: "common-69b0bd4f",
                5769: "appMedia",
                5847: "socialMediaExtension",
                5863: "projectDetail",
                6026: "InvestmentData",
                6419: "batchMng",
                6596: "404",
                6653: "DataPromotion",
                6682: "appExtension",
                6810: "common-c7713fe4",
                7012: "shopPromotionDetail",
                7066: "secretOrder",
                7253: "shopAnalyse",
                7468: "openOrder",
                7815: "chatExtension",
                7899: "custompromotion",
                7991: "webMng",
                8022: "cashGiftDepositResult",
                8273: "actAnalyse",
                8277: "cashGift",
                8300: "msg",
                8429: "helpcenter",
                8442: "moreProductList",
                8608: "channelPromotion",
                8722: "common-fb051ecb",
                8924: "initRevGroup",
                8983: "report",
                8989: "common-a07e9f05",
                9206: "trafficMediaExtension",
                9223: "initiate",
                9405: "common-bcec5985",
                9557: "couponPromotion",
                9621: "myInvoice",
                9664: "taskEffectData",
                9704: "batchDetail",
                9734: "myShop",
                9830: "darenBank",
                9851: "common-c0d952d5",
                9920: "operate",
                9940: "promotionSite",
                9974: "myStarEnlist"
            }[e] + "." + {
                34: "0173ff8f",
                81: "51e4d552",
                378: "a775504f",
                410: "f3b3ce65",
                621: "0ed1dbdb",
                685: "635b41c3",
                869: "5910e459",
                917: "b30a0d80",
                929: "126e8f02",
                973: "dd604fd9",
                1131: "5c758086",
                1276: "4afef4b0",
                1288: "efd9ca56",
                1621: "dd68ef97",
                1666: "eef150ee",
                1806: "ab7e517e",
                1884: "e633dcbf",
                1913: "d53aa0a2",
                1970: "e991c752",
                1992: "36ef2f28",
                2337: "3c8a21db",
                2412: "35ff0de8",
                2479: "36091181",
                2481: "fa3a465d",
                2527: "33415127",
                2690: "64ddf7cc",
                2795: "89bc9931",
                2832: "b4273770",
                2951: "aadb3ac0",
                2970: "83785627",
                2992: "164ee1c0",
                3012: "2347219c",
                3386: "1a1f7d84",
                3513: "bc094fa7",
                3579: "40c1c3b1",
                3583: "f5d3ef48",
                3712: "0c622f83",
                3756: "3516c499",
                3765: "4ad5d82d",
                3779: "70117dd8",
                3888: "2ed151fe",
                3940: "6e0a2517",
                4163: "77729184",
                4256: "2635c4c9",
                4565: "dc44e106",
                4738: "d5a92ea5",
                4843: "353c8190",
                4962: "ef81a2f9",
                5001: "d44c4832",
                5075: "7caafb6f",
                5142: "81bc023b",
                5177: "ba7d0e4c",
                5313: "37f84ab7",
                5413: "c7fd2e9a",
                5512: "1cc72436",
                5549: "981dd4c5",
                5724: "fae8a443",
                5769: "3026d89e",
                5847: "88f445a5",
                5863: "d512042d",
                6026: "676ef5c5",
                6419: "f1f7b477",
                6596: "43477835",
                6653: "c73c0500",
                6682: "9a980d14",
                6810: "3b98e9f1",
                7012: "c75bcc5e",
                7066: "7355632a",
                7253: "99e5f2be",
                7468: "2f63401c",
                7815: "7176c4b5",
                7899: "cfe36c2c",
                7991: "65730e93",
                8022: "0b3b8d2b",
                8273: "e60fd548",
                8277: "db05eb0f",
                8300: "2cc324f3",
                8429: "7479bfd9",
                8442: "9a426cc3",
                8608: "ce7516bf",
                8722: "d3db8be6",
                8924: "e678bf90",
                8983: "9d315bec",
                8989: "fa829613",
                9206: "178b940f",
                9223: "96bde6c9",
                9405: "291ee58a",
                9557: "a25c4ce7",
                9621: "ece2b2a0",
                9664: "3b9df2cc",
                9704: "1a69ae78",
                9734: "74dcc744",
                9830: "de870bad",
                9851: "bd3ece3d",
                9920: "f0359e40",
                9940: "eb35820c",
                9974: "48942a10"
            }[e] + ".js"
        }
        ,
        r.g = function () {
            if ("object" == typeof globalThis)
                return globalThis;
            try {
                return this || new Function("return this")()
            } catch (e) {
                if ("object" == typeof window)
                    return window
            }
        }(),
        r.o = function (e, n) {
            return Object.prototype.hasOwnProperty.call(e, n)
        }
        ,
        n = {},
        t = "JDUnion:",
        r.l = function (e, o, a, c) {
            if (n[e])
                n[e].push(o);
            else {
                var i, d;
                if (void 0 !== a)
                    for (var f = document.getElementsByTagName("script"), u = 0; u < f.length; u++) {
                        var b = f[u];
                        if (b.getAttribute("src") == e || b.getAttribute("data-webpack") == t + a) {
                            i = b;
                            break
                        }
                    }
                i || (d = !0,
                    (i = document.createElement("script")).charset = "utf-8",
                    i.timeout = 120,
                r.nc && i.setAttribute("nonce", r.nc),
                    i.setAttribute("data-webpack", t + a),
                    i.src = e),
                    n[e] = [o];
                var s = function (t, o) {
                    i.onerror = i.onload = null,
                        clearTimeout(l);
                    var a = n[e];
                    if (delete n[e],
                    i.parentNode && i.parentNode.removeChild(i),
                    a && a.forEach((function (e) {
                            return e(o)
                        }
                    )),
                        t)
                        return t(o)
                }
                    , l = setTimeout(s.bind(null, void 0, {
                    type: "timeout",
                    target: i
                }), 12e4);
                i.onerror = s.bind(null, i.onerror),
                    i.onload = s.bind(null, i.onload),
                d && document.head.appendChild(i)
            }
        }
        ,
        r.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(e, "__esModule", {
                    value: !0
                })
        }
        ,
        r.nmd = function (e) {
            return e.paths = [],
            e.children || (e.children = []),
                e
        }
        ,
        r.p = "//storage.360buyimg.com/pubfree-bucket/unionpc/c3a1b41eb/",
        function () {
            var e = {
                6700: 0
            };
            r.f.j = function (n, t) {
                var o = r.o(e, n) ? e[n] : void 0;
                if (0 !== o)
                    if (o)
                        t.push(o[2]);
                    else if (6700 != n) {
                        var a = new Promise((function (t, a) {
                                o = e[n] = [t, a]
                            }
                        ));
                        t.push(o[2] = a);
                        var c = r.p + r.u(n)
                            , i = new Error;
                        r.l(c, (function (t) {
                                if (r.o(e, n) && (0 !== (o = e[n]) && (e[n] = void 0),
                                    o)) {
                                    var a = t && ("load" === t.type ? "missing" : t.type)
                                        , c = t && t.target && t.target.src;
                                    i.message = "Loading chunk " + n + " failed.\n(" + a + ": " + c + ")",
                                        i.name = "ChunkLoadError",
                                        i.type = a,
                                        i.request = c,
                                        o[1](i)
                                }
                            }
                        ), "chunk-" + n, n)
                    } else
                        e[n] = 0
            }
                ,
                r.O.j = function (n) {
                    return 0 === e[n]
                }
            ;
            var n = function (n, t) {
                var o, a, c = t[0], i = t[1], d = t[2], f = 0;
                if (c.some((function (n) {
                        return 0 !== e[n]
                    }
                ))) {
                    for (o in i)
                        r.o(i, o) && (r.m[o] = i[o]);
                    if (d)
                        var u = d(r)
                }
                for (n && n(t); f < c.length; f++)
                    a = c[f],
                    r.o(e, a) && e[a] && e[a][0](),
                        e[a] = 0;
                return r.O(u)
            }
                , t = self.webpackChunkJDUnion = self.webpackChunkJDUnion || [];
            t.forEach(n.bind(null, 0)),
                t.push = n.bind(null, t.push.bind(t))
        }(),
        r.nc = void 0
}();




        function e(t) {
            var n, o, a, i, r, l, s, c, d, u, p, f, g, v, m, b, x, w, _, y, C;
            return h().wrap((function (e) {
                    for (; ;)
                        switch (e.prev = e.next) {
                            case 0:
                                return n = t.functionId,
                                    o = t.method,
                                    a = void 0 === o ? "GET" : o,
                                    i = t.params,
                                    r = t.isEncode,
                                    l = void 0 === r || r,
                                    s = t.needCode,
                                    c = void 0 !== s && s,
                                    d = t.appid,
                                    u = void 0 === d ? Z.ZP.APP_ID.UNION_PC : d,
                                    p = t.payload,
                                    f = void 0 === p ? {} : p,
                                    g = "https://api.m.jd.com/api?",
                                    v = D().get("__jda"),
                                    m = null == v ? void 0 : v.split(".")[1],
                                    b = {
                                        functionId: n,
                                        appid: u,
                                        _: Date.now(),
                                        loginType: "3",
                                        uuid: m,
                                        "x-api-eid-token": W
                                    },
                                    e.prev = 5,
                                    x = new L.Z({
                                        appId: "586ae"
                                    }),
                                    i = J(J({}, i), {}, {
                                        clientPageId: "jingfen_pc"
                                    }),
                                    w = {
                                        functionId: n,
                                        appid: u,
                                        body: K()(k()(i)).toString()
                                    },
                                    e.next = 12,
                                    x.sign(w);
                            case 12:
                                _ = e.sent,
                                    y = _.h5st,
                                    b = J(J({}, b), {}, {
                                        h5st: encodeURI(y)
                                    }),
                                    e.next = 20;
                                break;
                            case 17:
                                e.prev = 17,
                                    e.t0 = e.catch(5),
                                    console.log(e.t0);
                            case 20:
                                "POST" === a ? (C = "body=".concat(l ? encodeURIComponent(k()(i)) : k()(i)),
                                    f.data = C) : b.body = l ? encodeURIComponent(k()(i)) : i,
                                    g += (0,
                                        M.L7)(b),
                                f.extendParams || (f.extendParams = {});
                                try {
                                    n && (f.extendParams.functionId = n),
                                    i && i.funName && (f.extendParams.funName = i.funName)
                                } catch (e) {
                                    console.log("error: ", e)
                                }
                                return e.next = 26,
                                    G(J(J({
                                        method: a,
                                        url: g
                                    }, f), {}, {
                                        withCredentials: !0,
                                        needCode: c
                                    })).then((function (e) {
                                            return !e.page && e.pageNo && (e.page = {
                                                pageNo: e.pageNo,
                                                pageSize: e.pageSize,
                                                hasNext: e.hasNext,
                                                totalCount: e.total || e.totalNum
                                            }),
                                                e
                                        }
                                    ));
                            case 26:
                                return e.abrupt("return", e.sent);
                            case 27:
                            case "end":
                                return e.stop()
                        }
                }
            ), e, null, [[5, 17]])
        }

console.log(ee())