function computeAntiAbuseHeader() {
    const e = Date.now() / 1e3;
    return Buffer.from(`${(() => {
            const e = 1e10 * (1 + Math.random() % 5e4);
            return e < 50 ? "-1" : e.toFixed(0)
        }
    )()}-ZG9udCBiZSBldmls-${e}`).toString("base64")
}