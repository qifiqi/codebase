


function aa(t) {
    return CryptoJS.AES.decrypt(
        CryptoJS.enc.Base64url.parse(t)
    , CryptoJS.enc.Hex.parse("aaad3e4fd540b0f79dca95606e72bf93"), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)
}
var t= 'pX7rCko1ZPLJXbyU3qjcDqAp042BK5yCrhhNlUZEBd6lHKILemhbvHD1YkhQ7FDbOO67LXHsECLhREpE4EgC33ovLqy1dbR8KcUTJs_JYGnTdumkV_DRl_Om8A1NRl-ziFO-iM0ZddbzKSkJTRyhMe6O-LItLdIOsdwDAC7pg0Gytc6RjMgYN45LR4_kNS6O12w6kgBSpzEdKkiEtKZCq2_pp9Vb9GgSgezuKF1AZhPPLCpE91s3VID0y81dRzVXmAN_zJb1vTxiDHxx8Jtt7zwUeNYZMKGk90s7icmJF38'
console.log(aa(t))

// console.log(CryptoJS.enc.Hex.parse("aaad3e4fd540b0f79dca95606e72bf93"))